import firebase_admin
from firebase_admin import credentials, db
import serial
import time

# Firebase configuration
FIREBASE_CREDENTIALS_PATH = "node-mcu-60ea0-firebase-adminsdk-3fahe-dffeb16432.json"
FIREBASE_DATABASE_URL = "https://node-mcu-60ea0-default-rtdb.asia-southeast1.firebasedatabase.app"

# Serial configuration
SERIAL_PORT = '/dev/cu.usbmodem2101'  # Replace with your Arduino's port
BAUD_RATE = 9600

def initialize_firebase():
    # Initialize Firebase
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DATABASE_URL
    })

def fetch_data_from_firebase():
    # Fetch data from the root of the Firebase database
    ref = db.reference("/")  # Root reference
    data = ref.get()
    return data

def send_data_to_arduino(serial_port, hand_angles):
    angles = [
        hand_angles.get("thumb", 0),
        hand_angles.get("index", 0),
        hand_angles.get("middle", 0),
        hand_angles.get("ring", 0),
        hand_angles.get("pinky", 0)
    ]
    # Convert angles to a comma-separated string
    angles_str = ",".join(map(str, angles))
    serial_port.write((angles_str + "\n").encode())
    print(f"Sent to Arduino: {angles_str}")

def main():
    # Initialize Firebase
    initialize_firebase()
    
    # Set up serial connection to Arduino
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as arduino:
        time.sleep(2)  # Wait for the connection to establish
        print("Connected to Arduino.")
        
        while True:
            try:
                # Fetch data from Firebase
                data = fetch_data_from_firebase()
                if not data:
                    print("No data received from Firebase.")
                    continue
                
                hand_angles = data.get("hand_angles", {})
                if hand_angles:
                    send_data_to_arduino(arduino, hand_angles)
                
                # Optional: Check LED status
                led_status = data.get("led", "off")
                print(f"LED Status: {led_status}")

                time.sleep(1)  # Adjust frequency of data fetch if necessary
                
            except KeyboardInterrupt:
                print("Exiting program.")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
