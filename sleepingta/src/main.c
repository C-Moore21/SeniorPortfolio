/**
 * Comments go here.
 */

#include "ta.h"
#include <errno.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

pthread_t ta;
pthread_t students[NUM_OF_STUDENTS];

/**
 * Initialize all relevant data structures and
 * synchronization objects.
 */
void init() {
  int i;
  waiting = 0;

  // destroy any remanents of the sempahore before intiing
  sem_unlink("student_sem");
  sem_unlink("ta_sem");

  // named semaphore initalization - Initialize to zero because the TA is
  // sleeping and there are no students
  student_sem = sem_open("student_sem", O_CREAT, 0666, 0);
  ta_sem = sem_open("ta_sem", O_CREAT, 0666, 0);
  pthread_mutex_init(&mutex, NULL);
  for (i = 0; i < NUM_OF_STUDENTS; i++)
    student_id[i] = i;
}

/**
 * Create the student threads.
 */
void create_students() {
  int i;

  for (i = 0; i < NUM_OF_STUDENTS; i++) {
    pthread_create(&students[i], 0, student_loop, (void *)&student_id[i]);
  }
}

/**
 * Create the TA thread.
 */
void create_ta() { pthread_create(&ta, 0, ta_loop, 0); }

/**
 * Stuff
 */
int main(void) {
  int i;
  init();
  create_ta();
  create_students();
  for (i = 0; i < NUM_OF_STUDENTS; i++)
    pthread_join(students[i], NULL);

  pthread_join(ta, NULL);

  return 0;
}
