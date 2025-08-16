# Smartphone Sensor Risk Classifier

An ML-based Android system for real-time road accident risk detection. This application uses smartphone sensors to monitor driving behaviour and predicts potentially risky events—such as harsh braking or sharp turns—and delivers immediate voice or vibration alerts to help prevent accidents.


## Background & Motivation

Safe driving is invaluable. This project is designed to mitigate road accident risk by leveraging the sensors in a smartphone—such as accelerometers and gyroscopes—to detect risky driving behaviours in real time and proactively alert drivers.

---

## Features

- **Real-Time Risk Detection**: Continuously monitors sensor data to identify signs of dangerous maneuvers.
- **Alert Mechanisms**: Sends voice alerts or vibration notifications upon detecting high-risk events.
- **Lightweight & Mobile-Friendly**: Optimized for low latency and minimal resource usage on Android devices.
- **Versatile Risk Detection**: Captures common hazardous behaviours, including harsh braking and sharp turns.

---

## System Architecture

1. **Data Collection**  
   - Captures raw sensor data (accelerometer, gyroscope) during driving.

2. **Feature Engineering & Processing**  
   - Processes sensor signals, extracts relevant features such as magnitude, direction, or threshold crossings.

3. **Machine Learning Model**  
   - Uses a model (e.g., Naive Bayes, decision trees, or neural networks) trained to classify risky vs non-risky situations.
   - The pre-trained model (e.g., `naive_bayes_model.pkl`) is included for inference.

4. **Android App Integration**  
   - Embeds the model within an Android app.
   - Accepts live data, applies the model to assess current risk, and triggers alerts if danger is detected.

5. **User Alerts**  
   - Alerts delivered via audible voice prompts or haptic vibration, alerting drivers in real-time.
   git clone https://github.com/Engr-Mujeeb-Rahman/smartphone-sensor-risk-classifier.git
   cd smartphone-sensor-risk-classifier
