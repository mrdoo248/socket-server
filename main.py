from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
# ⚡️ لا تحدد async_mode، Replit سيختار الأنسب تلقائيًا
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print("✅ Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("❌ Client disconnected")

@socketio.on('cmd')
def handle_cmd(data):
    print("📥 CMD received:", data)
    socketio.emit('cmd', data)

if __name__ == '__main__':
    # use_reloader=False مهم على Replit
    socketio.run(app, host='0.0.0.0', port=3000, debug=True, use_reloader=False)
