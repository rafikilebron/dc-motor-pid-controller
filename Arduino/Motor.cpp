#include "Motor.h"

Motor::Motor(uint8_t pwm_pin, uint8_t in1_pin, uint8_t in2_pin, uint8_t standby_pin){
  pwm_pin_      = pwm_pin;
  in1_pin_      = in1_pin;
  in2_pin_      = in2_pin;
  standby_pin_  = standby_pin;
  current_pwm_  = "0";
  setup();
}

void Motor::setup(){
  pinMode(pwm_pin_,     OUTPUT);
  pinMode(in1_pin_,     OUTPUT);
  pinMode(in2_pin_,     OUTPUT);
  pinMode(standby_pin_, OUTPUT);
}

void Motor::start(){
  digitalWrite(standby_pin_, HIGH);
}

void Motor::stop(){
  digitalWrite(standby_pin_, LOW);
}

void Motor::setSpeed(int pwm){
  // Limit the PWM value between 0 and 255
  pwm = constrain(pwm, 0, 255);
  current_pwm_ = String(pwm);
  analogWrite(pwm_pin_, pwm);
}

void Motor::clockwise(){
  digitalWrite(in1_pin_, HIGH);
  digitalWrite(in2_pin_, LOW);
}

void Motor::counterClockwise(){
  digitalWrite(in1_pin_, LOW);
  digitalWrite(in2_pin_, HIGH);
}