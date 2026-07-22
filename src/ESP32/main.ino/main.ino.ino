#include <Arduino.h>
#include "config.h"
#include "motor_control.h"
#include "sensor_read.h"

String command = "";

void setup() {
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, 16, 17); // UART to Raspberry Pi
  
  setupMotors();
  setupSensors();
  
  Serial.println("ESP32 Wheelchair Controller Ready!");
}

void loop() {
  if (Serial2.available()) {
    command = Serial2.readStringUntil('\n');
    command.trim();
    if (command == "FORWARD") moveForward(180);
    else if (command == "BACKWARD") moveBackward(160);
    else if (command == "LEFT") turnLeft(160);
    else if (command == "RIGHT") turnRight(160);
    else if (command == "STOP") stopMotors();
  }

  // Safety
  float dist = readUltrasonic(TRIG1, ECHO1);
  if (dist > 0 && dist < 25) {
    stopMotors();
    Serial2.println("OBSTACLE:" + String(dist));
  }
  if (detectIRObstacle(IR_LEFT) || detectIRObstacle(IR_RIGHT)) {
    stopMotors();
    Serial2.println("IR_OBSTACLE");
  }
  delay(50);
}