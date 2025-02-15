# Hand Gesture-Based Motor Control System

## Overview
This project implements a hand gesture-based system to control a motor using Python and Arduino. It detects the number of fingers shown and sends commands via a serial connection to an Arduino Uno. The Arduino then controls the motor speed accordingly.

## Features
- **Hand Tracking:** Uses OpenCV and MediaPipe to detect fingers.
- **Serial Communication:** Sends recognized finger counts to Arduino.
- **Motor Control:** Adjusts motor behavior based on received signals.

## Gesture Commands
| Fingers | Action |
|---------|--------|
| 0       | Stop the motor |
| 1       | Start the motor |
| 2       | Increase speed |
| 3       | Decrease speed |
| 5       | Set speed |

## Hardware Requirements
- Arduino Uno
- Motor Driver
- DC Motor
- External Power Supply
- USB/Serial Cable
- Computer with Python (OpenCV, MediaPipe)

## Software Requirements
- Python 3.x
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE

## Installation & Setup
1. **Python Setup:**
   ```bash
   pip install opencv-python mediapipe pyserial
