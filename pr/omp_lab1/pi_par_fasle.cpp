#include <stdio.h>
#include <time.h>
#include <omp.h>

long long num_steps = 100000;
double a[100000];
double step;

int main(int argc, char* argv[])
{
  clock_t start, stop;
  double x, pi, sum=0.0;
  int i;
  step = 1./(double)num_steps;
  start = clock();
  #pragma omp parallel for reduction(+:sum)
  for (i=0; i<num_steps; i++)
  {
    x = (i + .5)*step;
    a[i] = a[i-1] + 4.0/(1.+ x*x);
  }

  pi = a[num_steps-1]*step;
  stop = clock();

  printf("Wartosc liczby PI wynosi %15.12f\n",pi);
  printf("Czas przetwarzania wynosi %f sekund\n",((double)(stop - start)/1000.0));
  return 0;
}
