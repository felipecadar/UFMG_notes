#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N_THREADS 1

pthread_t threads[N_THREADS];
pthread_mutex_t lock;

long c = 0;

void *rand_points(void *arg){
    double x, y;
    int *n  = (int *)arg;
    for (int i = 0; i < *n; ++ i) {
        x = drand48();
        y = drand48();
        if (x * x + y * y <= 1.0) {
            pthread_mutex_lock(&lock);
            c++;
            pthread_mutex_unlock(&lock);
        }
    }
}


int main(int argc, char* argv[]) {
    int n = atol(argv[1]);
    int n_thread = n/N_THREADS;

    if (pthread_mutex_init(&lock, NULL) != 0)
    {
        printf("\n mutex init failed\n");
        return 1;
    }

    for(int i=0; i < N_THREADS; i++){
        pthread_create(&(threads[i]), NULL, rand_points, &n_thread);
    }

    for(int i=0; i < N_THREADS; i++){
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&lock);
    printf("Pi = %10.8g\n", (c * 4.0)/ (n_thread*N_THREADS) );
}