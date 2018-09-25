/**
 * General structure of the teaching assistant.
 *
 */

#include "ta.h"
#include <errno.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void *ta_loop(void *param) {
  while (1) {
    printf("I am the TA\n");
    // wait for a student to arrive.
    sem_wait(student_sem);
    // creating a random sleep time
    int time = (int)(random() % MAX_SLEEP_TIME) + 1;
    pthread_mutex_lock(&mutex);
    --waiting;
    pthread_mutex_unlock(&mutex);
    help_student(time);
    // tell the students that the TA is not busy or sleeping.
    sem_post(ta_sem);
  }
}
