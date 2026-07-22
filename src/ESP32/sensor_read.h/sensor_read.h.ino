#ifndef SENSOR_READ_H
#define SENSOR_READ_H

float readUltrasonic(int trigPin, int echoPin);
bool detectIRObstacle(int irPin);
void setupSensors(void);

#endif