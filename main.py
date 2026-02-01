from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def on_connect():
    print("✅ Client connected")

@socketio.on('disconnect')
def on_disconnect():
    print("❌ Client disconnected")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000, debug=True, use_reloader=False)
