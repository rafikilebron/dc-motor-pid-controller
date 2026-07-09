#include "Motor.h"
#include "PID.h"
#include "Encoder.h"

// Object Instances
Motor motor(
  17, // PWM Pin
  4,  // IN1 Pin
  16, // IN2 Pin
  5   // STBY Pin
);

PID pid(
  4.5,    // Kp
  0.008,  // Kd
  0.001   // Ki
);

Encoder encoder(
  14, // A Pin
  27, // B Pin
  495 // PPR (Pulses Per Revolution)
);

String cmd;

void setup(){
  Serial.begin(115200);
  encoder.begin();
  motor.start();
  motor.setSpeed(255);
}

void loop(){
  if (Serial.available()){
    // Read command
    cmd = Serial.readStringUntil('\n');
    cmd.trim();
  }

  processCommand(cmd);
  delay(10);
}

void processCommand(String cmd){
  if (!cmd.startsWith("$"))
    return;

  if (cmd.startsWith("$PID")){
    parsePID(cmd);
  }

  else if (cmd.startsWith("$MOTOR")){
    parseMotor(cmd);
  }
}

void parsePID(String cmd){
  int i1 = cmd.indexOf(',');

  if (i1 == -1)
    return;

  String parameter = cmd.substring(i1 + 1);
  parameter.trim();

  // $PID,REQUEST
  if (parameter == "REQUEST"){
    Serial.print("$PID,");
    Serial.print(pid.getKp());
    Serial.print(",");
    Serial.print(pid.getKi());
    Serial.print(",");
    Serial.println(pid.getKd());

    return;
  }

  // $PID,kp,ki,kd
  int i2 = cmd.indexOf(',', i1 + 1);
  int i3 = cmd.indexOf(',', i2 + 1);

  if (i2 == -1 || i3 == -1)
    return;

  float kp = cmd.substring(i1 + 1, i2).toFloat();
  float ki = cmd.substring(i2 + 1, i3).toFloat();
  float kd = cmd.substring(i3 + 1).toFloat();

  pid.setTunnings(kp, ki, kd);

  // Confirm new parameters
  Serial.print("$PID,");
  Serial.print(pid.getKp());
  Serial.print(",");
  Serial.print(pid.getKi());
  Serial.print(",");
  Serial.println(pid.getKd());
}

void parseMotor(String cmd){
  int comma = cmd.indexOf(',');

  String value = cmd.substring(comma + 1);

  if (value == "STOP"){
    motor.stop();
  }

  else{
    int targetAngle = value.toInt();
    executePidCommand(targetAngle);
  }
}

void executePidCommand(int target){
  uint8_t min_speed = 10;

  target = constrain(target, -360, 360);

  // Read current position
  float position = encoder.getDegrees();
  
  // Calculate PID output
  float out   = pid.compute(target, position);
  uint8_t pwr = fabs(out);

  // Minimum motor speed
  motor.start();
  if (pwr < min_speed){
    pwr = min_speed;
  }
  motor.setSpeed(pwr);

  // Motor direction
  if (out < 0){
    motor.clockwise();
  }

  else{
    motor.counterClockwise();
  }

  // Send current position
  Serial.print("$TEL,");
  Serial.println(position);
}