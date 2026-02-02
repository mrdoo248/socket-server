from flask import Flask
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# 🌐 Endpoint أساسي
@app.route('/')
def home():
    return "Server is running ✅"

# 🔌 أحداث Socket.IO
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

# ✅ تشغيل السيرفر
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True, use_reloader=False)
