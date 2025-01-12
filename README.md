# Computer-Vision-Operated-Robotic-Arm

DexVisio: Computer Vision Based Robotic Arm 🤖
Show Image
Show Image
Show Image
A cutting-edge computer vision-based robotic hand that mimics human hand movements in real-time. DexVisio combines advanced computer vision techniques with affordable hardware to create an intuitive and responsive robotic system.
🌟 Features

Real-time hand tracking and gesture recognition
Precise finger movement replication
Low-latency response system
Web-based control interface
Distributed and local control options
Affordable and scalable design
Educational applications support

🛠️ Technology Stack

Computer Vision: MediaPipe, OpenCV
Backend: Flask, Firebase Realtime Database
Frontend: HTML5, JavaScript
Hardware: Arduino, Servo Motors
3D Printing: PLA Filaments
Communication: Serial Interface, WebSockets

🔧 Hardware Requirements

Arduino Board
6x Standard Servo Motors
3D Printed Hand Components
Webcam
Breadboard and Jumper Cables
Computer for running the software

📊 System Architecture
The system operates in two modes:
Local System

Direct communication between computer and Arduino
Minimal latency
Simplified implementation
Ideal for standalone applications

Distributed System

Web-based interface
Firebase real-time database integration
Remote operation capability
Suitable for collaborative applications

🚀 Installation & Setup

Clone the repository

bashCopygit clone https://github.com/yourusername/dexvisio.git
cd dexvisio

Install Python dependencies

bashCopypip install -r requirements.txt

Set up Firebase (for distributed system)


Create a Firebase project
Download service account credentials
Update Firebase configuration in the code


Upload Arduino code


Open Arduino IDE
Load the servo control code
Upload to your Arduino board


Configure serial port


Update the serial port in Python scripts according to your system

💻 Usage
Local System
bashCopypython local_system.py
Distributed System

Start Flask server:

bashCopypython app.py

Run Firebase listener:

bashCopypython firebase_reader.py

Open web interface in browser:

Copyhttp://localhost:5000
📈 Performance
The system demonstrates excellent performance metrics:

Response time: ~100ms (local) / ~200-300ms (distributed)
Gesture accuracy: 95%+
Servo precision: ±1°

👥 Contributors

Subhrajay Changkakoti
Samarth Gayakhe
Ashish Singh
Krishna

📚 Documentation
Detailed documentation including system architecture, component specifications, and API references can be found in the docs directory.
🤝 Contributing
We welcome contributions! Please read our Contributing Guidelines before submitting pull requests.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments
Special thanks to:

Prof. Soubhagya Sankar Barpanda
Dr. Ajay Dagar
VIT-AP University
The MediaPipe and OpenCV communities
