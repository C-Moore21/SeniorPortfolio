/**
 * Simulate helping a student
 */

#include "ta.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void help_student(int sleep_time) {
  printf("Helping a student for %d seconds\n", sleep_time);
  printf("Helping student number: %d\n", number);

  sleep(sleep_time);
}
