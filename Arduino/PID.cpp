#include "PID.h"

PID::PID(float kp, float ki, float kd){
  kp_ = kp;
  ki_ = ki;
  kd_ = kd;

  previous_error_ = 0;
  integral_       = 0;
  previous_time_  = micros();
  min_output_     = -255;
  max_output_     = 255;
}

void PID::setTunnings(float kp, float ki, float kd){
  kp_ = kp;
  ki_ = ki;
  kd_ = kd;
}

float PID::compute(float setPoint, float measurement){
  unsigned long currentTime = micros();

  float deltaTime = (float)(currentTime - previous_time_) / 1000000.0;

  previous_time_ = currentTime;

  if(deltaTime <= 0)
    return 0;

  // Error
  float error = setPoint - measurement;

  // Integral
  integral_ += error * deltaTime;

  // Derivate
  float derivative = (error - previous_error_) / deltaTime;

  // PID
  float output =
      (kp_ * error) +
      (ki_ * integral_) +
      (kd_ * derivative);

  // Store error
  previous_error_ = error;

  // Limit output
  if(output > max_output_)
    output = max_output_;

  if(output < min_output_)
    output = min_output_;

  return output;
}

void PID::reset(){
    previous_error_ = 0;

    integral_ = 0;

    previous_time_ = micros();
}

void PID::setOutputLimits(float minOutput, float maxOutput){
    min_output_ = minOutput;
    max_output_ = maxOutput;
}

float PID::getKp(){
  return kp_;
}

float PID::getKi(){
  return ki_;
}

float PID::getKd(){
  return kd_;
}