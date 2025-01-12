# DexVisio: Computer Vision Based Robotic Arm 🤖

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Arduino](https://img.shields.io/badge/Arduino-IDE-00979D.svg)](https://www.arduino.cc/en/software)

A cutting-edge computer vision-based robotic hand that mimics human hand movements in real-time. DexVisio combines advanced computer vision techniques with affordable hardware to create an intuitive and responsive robotic system.

## 🌟 Features

- Real-time hand tracking and gesture recognition
- Precise finger movement replication
- Low-latency response system
- Web-based control interface
- Distributed and local control options
- Affordable and scalable design
- Educational applications support

## 🛠️ Technology Stack

- **Computer Vision:** MediaPipe, OpenCV
- **Backend:** Flask, Firebase Realtime Database
- **Frontend:** HTML5, JavaScript
- **Hardware:** Arduino, Servo Motors
- **3D Printing:** PLA Filaments
- **Communication:** Serial Interface, WebSockets

## 🔧 Hardware Requirements

- Arduino Board
- 6x Standard Servo Motors
- 3D Printed Hand Components
- Webcam
- Breadboard and Jumper Cables
- Computer for running the software

## 📊 System Architecture

The system operates in two modes:

### Local System
- Direct communication between computer and Arduino
- Minimal latency
- Simplified implementation
- Ideal for standalone applications

### Distributed System
- Web-based interface
- Firebase real-time database integration
- Remote operation capability
- Suitable for collaborative applications

## 🚀 Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/Ashish032002/Computer-Vision-Operated-Robotic-Arm.git
cd Computer-Vision-Operated-Robotic-Arm
```

2. Install Python dependencies
```bash
pip install -r requirements.txt
```

3. Set up Firebase (for distributed system)
- Create a Firebase project
- Download service account credentials
- Update Firebase configuration in the code

4. Upload Arduino code
- Open Arduino IDE
- Load the servo control code
- Upload to your Arduino board

5. Configure serial port
- Update the serial port in Python scripts according to your system

## 💻 Usage

### Local System
```bash
python local_system.py
```

### Distributed System
1. Start Flask server:
```bash
python app.py
```

2. Run Firebase listener:
```bash
python firebase_reader.py
```

3. Open web interface in browser:
```
http://localhost:5000
```

## 📈 Performance

The system demonstrates excellent performance metrics:
- Response time: ~100ms (local) / ~200-300ms (distributed)
- Gesture accuracy: 95%+
- Servo precision: ±1°

## 👥 Contributors

- Subhrajay Changkakoti
- Samarth Gayakhe
- Ashish Singh
- Krishna

## 📚 Documentation

Detailed documentation including system architecture, component specifications, and API references can be found in the [docs](./docs) directory.

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



