from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# 📌 أضف هذا
@app.route('/')
def home():
    return "Server is running ✅"

@socketio.on('connect')
def on_connect():
    print("✅ Client connected")

@socketio.on('disconnect')
def on_disconnect():
    print("❌ Client disconnected")

@socketio.on('cmd')
def handle_cmd(data):
    print("📥 CMD received:", data)
    socketio.emit('cmd', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)

