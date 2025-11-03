from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt


app = Flask(__name__)

lamp_state = {"status": "OFF"}

# Crear cliente MQTT
mqtt_client = mqtt.Client()

# Conectar al broker público de prueba
mqtt_client.connect("test.mosquitto.org", 1883, 60)

@app.route("/", methods=["GET"])
def index():
    return f"""
    <html>
    <body>
        <h1>💡 Estado: {lamp_state['status']}</h1>
        <form action="/toggle" method="post">
            <button name="status" value="ON">Encender</button>
            <button name="status" value="OFF">Apagar</button>
        </form>
    </body>
    </html>
    """

@app.route("/toggle", methods=["POST"])
def toggle():
    status = request.form.get("status")
    if status:
        lamp_state["status"] = status
        mqtt_client.publish("home/lamp", lamp_state["status"])
    return f"""
    <html>
    <body>
        <h1>💡 Estado: {lamp_state['status']}</h1>
        <form action="/toggle" method="post">
            <button name="status" value="ON">Encender</button>
            <button name="status" value="OFF">Apagar</button>
        </form>
    </body>
    </html>
    """

@app.route("/state", methods=["GET"])
def state():
    return jsonify(lamp_state)

if __name__ == "__main__":
    print("Python está ejecutando miAppFlaskPY.py")
    app.run(host="0.0.0.0", port=5000)