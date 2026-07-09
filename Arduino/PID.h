#ifndef PID_H
#define PID_H

#include <Arduino.h>

class PID{
  // Attributes
  private:
    float kp_;
    float ki_;
    float kd_;

    float previous_error_;

    float integral_;

    unsigned long previous_time_;

    float min_output_;
    float max_output_;

  // Methods
  public:
    PID(float, float, float);

    void setTunnings(float kp, float ki, float kd);

    float compute(float setPoint, float measurement);

    void reset();

    void setOutputLimits(float minOutput, float maxOutput);

    float getKp();

    float getKd();

    float getKi();

};

#endif