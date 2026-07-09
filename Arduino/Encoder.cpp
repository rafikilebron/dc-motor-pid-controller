#include "Encoder.h"

Encoder* Encoder::instance_ = nullptr;

Encoder::Encoder(uint8_t pinA, uint8_t pinB, int pulses_per_revolution){
  pinA_ = pinA;
  pinB_ = pinB;

  pulses_per_revolution_ = pulses_per_revolution;
  pulses_ = 0;
}

void Encoder::begin(){
  pinMode(pinA_, INPUT);
  pinMode(pinB_, INPUT);

  instance_ = this;

  attachInterrupt(digitalPinToInterrupt(pinA_), encoderISR, RISING);
}

long Encoder::getPulses(){
  return pulses_;
}

float Encoder::getDegrees(){
  return ((float)pulses_ * 360.0) / pulses_per_revolution_;
}

void Encoder::reset(){
  pulses_ = 0;
}

void IRAM_ATTR Encoder::encoderISR(){
  int b = digitalRead(instance_->pinB_);

  if(b>0){
    instance_->pulses_++;
  }

  else{
    instance_->pulses_--;
  }
}