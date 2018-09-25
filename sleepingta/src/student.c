/**
 * General structure of a student.
 *
 */

#include "ta.h"
#include <errno.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void *student_loop(void *param) {
  while (1) {
    number = *((int *)param);
    int sleep_time;
    printf("I am student %d\n", number);
    // lock before performing any action on 'wait' and unlock immediately after
    // the usage of wait
    pthread_mutex_lock(&mutex);
    if (waiting < NUM_OF_SEATS) {
      ++waiting;
      pthread_mutex_unlock(&mutex);
      printf("I am student %d\n", number);
      // post to TA that there are students available
      sem_post(student_sem);
      printf("student posted\n");
      sem_wait(ta_sem);

    } else {
      pthread_mutex_unlock(&mutex);
      int time = (int)(random() % MAX_SLEEP_TIME) + 1;
      // make the students program if there are no available seats.
      printf("no chairs will program for %d\n", time);
      programming(time);
    }
  }
}
