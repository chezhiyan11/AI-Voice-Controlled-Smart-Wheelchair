#ifndef MOTOR_CONTROL_H
#define MOTOR_CONTROL_H

void setupMotors(void);
void moveForward(int speed);
void moveBackward(int speed);
void turnLeft(int speed);
void turnRight(int speed);
void stopMotors(void);

#endif