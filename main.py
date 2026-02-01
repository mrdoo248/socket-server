from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "SERVER OK"   # ← هذا يمنع 404

@socketio.on("connect")
def connect():
    print("✅ CLIENT CONNECTED")

@socketio.on("cmd")
def cmd(data):
    print("📥 CMD:", data)
    socketio.emit("cmd", data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=3000, allow_unsafe_werkzeug=True)
