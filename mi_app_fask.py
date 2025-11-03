from flask import Flask, render_template_string, request
import paho.mqtt.client as mqtt

# Broker público
BROKER = "broker.hivemq.com"
TOPIC = "juanled/test"

# Configurar cliente MQTT
client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

# Flask app
app = Flask(__name__)

estado = "OFF"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Control IoT</title>
    <style>
        body { font-family: Arial; background: #111; color: white; text-align: center; padding-top: 100px; }
        button { padding: 15px 30px; margin: 10px; font-size: 20px; border: none; border-radius: 10px; cursor: pointer; }
        .on { background-color: #28a745; }
        .off { background-color: #dc3545; }
    </style>
</head>
<body>
    <h1>💡 Estado del LED: {{ estado }}</h1>
    <form method="post">
        <button name="accion" value="ON" class="on">Encender</button>
        <button name="accion" value="OFF" class="off">Apagar</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    global estado
    if request.method == 'POST':
        estado = request.form['accion']
        client.publish(TOPIC, estado)
        print(f"📤 Mensaje enviado: {estado}")
    return render_template_string(HTML, estado=estado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)