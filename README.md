# DC Motor Position Control using PID and UART(ESP32)

A complete embedded control system for **DC motor position control** using a **PID controller**, featuring a custom **UART communication protocol** and a **Python desktop GUI** built with **PySide6**.

The project demonstrates the integration of embedded software, object-oriented programming, serial communication, multithreading, and real-time visualization.

---

## DEMO (mp4)
[DC Motor PID Controller](https://www.youtube.com/shorts/Vag89rl0xiE)

---

# Features

- PID position controller running on the microcontroller
- Quadrature encoder feedback using hardware interrupts
- Full-duplex UART communication with custom commands
- Interactive Python GUI
- Real-time position visualization
- Real-time control error monitoring
- Runtime PID tuning
- Adjustable target position
- Emergency motor stop
- Object-oriented architecture on both Arduino and Python

---

# System Architecture

```text
                +---------------------------+
                |       Python GUI          |
                |---------------------------|
                | PySide6                   |
                | UART Manager              |
                | Plot Widget               |
                | PID Configuration         |
                | Motor Controls            |
                +-------------+-------------+
                              |
                         UART Serial
                              |
                +-------------+-------------+
                |      Microcontroller      |
                |---------------------------|
                | UART Parser               |
                | PID Controller            |
                | Encoder                   |
                | Motor Driver              |
                +-------------+-------------+
                              |
                    DC Motor + Encoder
```

---

# Project Structure

```text
├── Arduino/
│   ├── Motor.cpp
│   ├── Motor.h
│   ├── Encoder.cpp
│   ├── Encoder.h
│   ├── PID.cpp
│   ├── PID.h
│   └── main.ino
│
├── Python/
│   ├── gui.py
│   ├── gui.ui
│   ├── main.py
│   ├── plot_widget.py
│   └── threads.py
│
└── README.md
```

---

# Technologies

## Embedded

- Arduino Framework
- C++
- Object-Oriented Programming
- Hardware Interrupts
- UART Communication
- PWM Motor Control

## Desktop

- Python
- PySide6
- PySerial
- Multithreading
- Qt Designer

---

# Software Design

The project was developed following an object-oriented architecture to improve readability, scalability, and maintainability.

Each hardware component is encapsulated into an independent class:

- Motor
- Encoder
- PID Controller

This separation allows each module to be tested and modified independently while keeping the application logic clean.

The desktop application follows the same philosophy, separating:

- GUI
- Serial communication
- Background threads
- Data visualization

---

# Encoder Reading

Motor position is measured using a quadrature encoder.

Instead of polling the encoder continuously, hardware interrupts are used to detect every pulse.

Advantages:

- High accuracy
- No missed pulses
- Minimal CPU overhead
- Reliable high-speed measurements

---

# PID Controller

The controller computes the required motor command from the difference between the desired position and the measured position.

Runtime tuning is supported directly from the GUI without reprogramming the microcontroller.

Parameters:

- Kp
- Ki
- Kd

---

# UART Communication Protocol

A lightweight custom protocol was implemented for communication between the PC and the microcontroller.

## PC → Microcontroller

```text
$PID,kp,ki,kd
```

Update PID constants.

```text
$PID,REQUEST
```

Request current PID parameters.

```text
$MOTOR,angle
```

Move the motor to the specified angle.

```text
$MOTOR,STOP
```

Stop the motor.

---

## Microcontroller → PC

```text
$TEL,position
```

Current motor position.

```text
$PID,kp,ki,kd
```

Current PID configuration.

---

A short delay was intentionally added inside the microcontroller main loop to ensure stable UART communication and prevent command corruption during continuous bidirectional transmission.

---

# Data Type Selection

Since the project runs on a resource-constrained microcontroller, memory optimization was considered during development.

Whenever possible, fixed-width integer types such as:

```cpp
uint8_t
```

were used instead of larger integer types.

Benefits:

- Lower RAM usage
- Faster execution
- Explicit variable size
- Better portability across embedded platforms

---

# Graphical User Interface

The desktop application was developed using **PySide6**.

Main features:

- Automatic COM port detection
- Baud rate selection
- UART connection management
- PID parameter tuning
- Target position input
- Motor enable/stop controls
- Real-time motor position
- Real-time position error
- Live position plot

The interface was designed to provide an intuitive workflow for testing and tuning the control system.

---

# Multithreading

UART reception is executed in a dedicated background thread.

This prevents the graphical interface from freezing while continuously receiving serial data.

Advantages:

- Responsive GUI
- Smooth real-time plotting
- Continuous serial reception
- Better user experience

---

# Control Loop

```text
User selects target angle
            │
            ▼
Python GUI sends UART command
            │
            ▼
Microcontroller receives command
            │
            ▼
Encoder measures position
            │
            ▼
PID computes control output
            │
            ▼
Motor driver updates PWM and direction
            │
            ▼
Current position sent back through UART
            │
            ▼
GUI updates plot and error display
```

---

# Future Improvements

- Anti-windup implementation
- Velocity estimation
- Cascaded Position-Speed PID
- Command queue
- Adjustable sampling period
- Automatic PID tuning
- Data logging to CSV
- Real-time parameter plots
- USB communication abstraction
- Closed-loop trajectory generation

---

# License

This project is intended for educational purposes and embedded control experimentation.
