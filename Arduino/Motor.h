#ifndef MOTOR_H
#define MOTOR_H

#include <Arduino.h>

class Motor{
  // Attributes
  private:
    uint8_t   pwm_pin_;
    uint8_t   in1_pin_;
    uint8_t   in2_pin_;
    uint8_t   standby_pin_;
    String    current_pwm_;

  // Methods
  public:
    Motor(uint8_t, uint8_t, uint8_t, uint8_t);
    
    void setup();

    void start();

    void stop();
    
    void setSpeed(int pwm);

    void clockwise();

    void counterClockwise();
};

#endif