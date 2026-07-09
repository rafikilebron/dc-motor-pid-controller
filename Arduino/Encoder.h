#ifndef ENCODER_H
#define ENCODER_h

#include <Arduino.h>

class Encoder{
  // Attributes
  private:
    uint8_t pinA_;
    uint8_t pinB_;

    int pulses_per_revolution_;

    volatile long pulses_;

    static void IRAM_ATTR encoderISR();

    static Encoder* instance_;

  // Methods
  public:
    Encoder(uint8_t pinA, uint8_t pinB, int pulses_per_revolution);

    void begin();

    long getPulses();

    float getDegrees();

    void reset();
};

#endif