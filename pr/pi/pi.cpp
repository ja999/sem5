// pi.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Windows.h>
#include <intrin.h>
#pragma intrinsic(__rdtsc)
#include <omp.h>

#define BILLION 1E9
#define NUM_STEPS 200000000L
#define LINE_LENGTH_SLOTS 30

double test_function(double (*func)(long long num_steps, double step), const char *name, long long num_steps, double step, double sequential_time);
unsigned long long get_time_of_computation(double (*func)(long long num_steps, double step), long long num_steps, double step, double *res);
double sequential(long long num_steps, double step);
double race(long long num_steps, double step);
double atomic(long long num_steps, double step);
double reduction(long long num_steps, double step);
double false_sharing(long long num_steps, double step);
unsigned line_length(long long num_steps, double step, int slots);



int main(int argc, char **argv) {
  long long num_steps = NUM_STEPS;
  double step = 1. / (double)num_steps;
  double sequential_time;
  int slots = 0;

  if (argc > 1) {
    slots = atoi(argv[1]);
  }
  if (slots == 0) {
    slots = LINE_LENGTH_SLOTS;
  }

  sequential_time = test_function(sequential, "Sekwencyjnie", num_steps, step, 0);
  test_function(race, "Wyscig", num_steps, step, sequential_time);
  test_function(atomic, "Atomic", num_steps, step, sequential_time);
  test_function(reduction, "Redukcja", num_steps, step, sequential_time);
  test_function(false_sharing, "Uniewaznianie linii", num_steps, step, sequential_time);

  printf("Dlugosc linii pamieci: %u", line_length(num_steps / 10, 1. / ((double)(num_steps / 10)), slots));

  scanf(" %d", &slots);

  return 0;
}

double test_function(double (*func)(long long num_steps, double step), const char *name, long long num_steps, double step, double sequential_time) {
  double pi, computation_time;

  computation_time = get_time_of_computation(func, num_steps, step, &pi) / BILLION;

  printf("\n%s\n", name);
  printf("PI = %15.12f\n", pi);
  printf("computation time = %f s\n", computation_time);
  if(sequential_time > 0) {
    printf("sequential_time / time = %f\n", sequential_time / computation_time);
  }

  return computation_time;
}

unsigned long long get_time_of_computation(double (*func)(long long num_steps, double step), long long num_steps, double step, double *res) {
  // double computation_time;
  double clock_time;
  unsigned long long start_clock, stop_clock;
  // struct timeval start, stop;

  // gettimeofday(&start, NULL);
  start_clock = __rdtsc();
  *res = func(num_steps, step);
  stop_clock =  __rdtsc();
  // gettimeofday(&stop, NULL);

  // computation_time = (double)(stop.tv_sec - start.tv_sec) + (double)(stop.tv_usec - start.tv_usec) / MILLION;
  clock_time = (stop_clock - start_clock) / 3;
  //printf("clock time = %f s\n", clock_time);
  return clock_time;
}

double sequential(long long num_steps, double step) {
  double x, pi, sum=0.0;
  int i;

  for (i = 0; i < num_steps; ++i) {
    x = (i + .5) * step;
    sum = sum + 4.0 / (1. + x * x);
  }

  pi = sum * step;
  return pi;
}

double race(long long num_steps, double step) {
  double pi, sum = 0.0;
  int i;
  #pragma omp parallel
  {
    double x;
    #pragma omp for
    for (i = 0; i < num_steps; ++i) {
      x = (i + .5) * step;
      sum = sum + 4.0 / (1.+ x * x);
    }
  }
  pi = sum * step;
  return pi;
}

double atomic(long long num_steps, double step) {
  double pi, sum = 0.0;
  int i;
  #pragma omp parallel
  {
    double x;
    #pragma omp for
    for (i = 0; i < num_steps; ++i) {
      x = (i + .5) * step;
      #pragma omp atomic
          sum += 4.0 / (1.+ x * x);
    }
  }
  pi = sum * step;
  return pi;
}

double reduction(long long num_steps, double step) {
  double pi, sum = 0.0;
  int i;
  #pragma omp parallel
  {
    double x;
    #pragma omp for private(i) reduction(+ : sum)
    for (i = 0; i < num_steps; ++i) {
      x = (i + .5) * step;
      sum += 4.0 / (1. + x * x);
    }
  }
  pi = sum * step;
  return pi;
}

#define FALSE_SHARING_THREAD_NUM 4
double false_sharing(long long num_steps, double step) {
  // worked in release mode without volatile; change to Debug/add volatile to sum if
  // it's not substantially slower; compiler might optimize this
  double pi, sum[FALSE_SHARING_THREAD_NUM] = { 0.0, 0.0, 0.0, 0.0 };
  int i;
  #pragma omp parallel num_threads(FALSE_SHARING_THREAD_NUM)
  {
    double x;
    int id = omp_get_thread_num();
    #pragma omp for
    for (i = 0; i < num_steps; ++i) {
      x = (i + .5) * step;
      sum[id] += 4.0 / (1. + x * x);
    }
  }
  for(i = 1; i < FALSE_SHARING_THREAD_NUM; ++i) {
    sum[0] += sum[i];
  }
  pi = sum[0] * step;
  return pi;
}

unsigned line_length(long long num_steps, double step, int slots) {
  // same as L151, volatile/debug if it doesn't work
  double sum[LINE_LENGTH_SLOTS]
    , computation_times[2][LINE_LENGTH_SLOTS - 1];
  int i, j;

  for(j = 0; j < slots - 1; ++j) {
    #pragma omp parallel num_threads(2)
    {
      double x;
      double clock_time;
    unsigned long long start_clock, stop_clock;
    
    start_clock = __rdtsc();
  

      int id = omp_get_thread_num()
        , slot = id + j;
      sum[slot] = 0.0;
      for (i = 0; i < num_steps; ++i) {
        x = (i + .5) * step;
    
        sum[slot] += 4.0 / (1. + x * x);
      }
      sum[slot] *= step;

    stop_clock = __rdtsc();
    clock_time = (double)(stop_clock - start_clock) / (3 * BILLION);
      computation_times[id][j] = clock_time; // (double)(stop.tv_sec - start.tv_sec) + (double)(stop.tv_usec - start.tv_usec) / MILLION;
    }
  printf("\n%d", j);
  for(i = 0; i < 2; ++i) {
      printf("\t%f", computation_times[i][j]);
    }
  }
  printf("\n");

  double avg = 0.0;
  for(j = 0; j < slots - 1; ++j) {
    computation_times[0][j] += computation_times[1][j];
    avg += computation_times[0][j];
  }
  avg /= slots - 1;

  int marker = 0;
  for(j = 0; j < slots - 1; ++j) {
    if(computation_times[0][j] / avg < 0.8) {
      if (marker > slots / 4) {
      return j - marker;
      }
      marker = j;
    }
  }

  return 0;
}
 