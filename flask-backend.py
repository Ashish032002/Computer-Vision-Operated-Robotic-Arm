from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, db
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Firebase Admin SDK
try:
    cred = credentials.Certificate('node-mcu-60ea0-firebase-adminsdk-3fahe-dffeb16432.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://node-mcu-60ea0-default-rtdb.asia-southeast1.firebasedatabase.app'
    })
except Exception as e:
    app.logger.error(f"Failed to initialize Firebase: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_led', methods=['POST'])
def update_led():
    try:
        data = request.get_json()
        led_value = data.get('led')
        
        if led_value is not None:
            ref = db.reference('led')
            ref.set(led_value)
            app.logger.info(f"LED updated to {led_value}")
            return jsonify({"status": "success", "led": led_value}), 200
        else:
            return jsonify({"status": "error", "message": "LED value not provided"}), 400

    except Exception as e:
        app.logger.error(f"Error updating LED: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/update_angles', methods=['POST'])
def update_angles():
    try:
        data = request.get_json()
        angles = data.get('angles')
        
        if angles is not None:
            ref = db.reference('hand_angles')
            ref.set(angles)
            app.logger.info(f"Angles updated: {angles}")
            return jsonify({"status": "success", "angles": angles}), 200
        else:
            return jsonify({"status": "error", "message": "Angle data not provided"}), 400

    except Exception as e:
        app.logger.error(f"Error updating angles: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
