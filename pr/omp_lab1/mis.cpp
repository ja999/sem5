#include <omp.h>
#include <stdio.h>
#include <iostream>
using namespace std;
int main() {
		int i;
		printf("Hello World\n");
		omp_set_num_threads(4);
#pragma omp parallel
		for(i=0;i<6;i++) {
			printf("omp_get_thread_num(): %d\n",omp_get_thread_num() );
			printf("Iter:%d\n",i);
			}

		printf("GoodBye World\n");
}
