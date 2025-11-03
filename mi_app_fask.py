from flask import Flask, request, render_template_string, jsonify

app = Flask(_name_)

lamp_state = {"status": "OFF"}

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Control de Lámpara</title>
  <style>
    body { font-family: Arial; text-align: center; margin-top: 80px; }
    h1 { font-size: 2em; }
    button { font-size: 1.2em; margin: 10px; padding: 10px 20px; border-radius: 8px; }
    .on { background-color: #4CAF50; color: white; }
    .off { background-color: #f44336; color: white; }
  </style>
</head>
<body>
  <h1>💡 Estado: {{ state }}</h1>
  <form action="/toggle" method="post">
    <button class="on" name="status" value="ON">Encender</button>
    <button class="off" name="status" value="OFF">Apagar</button>
  </form>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_PAGE, state=lamp_state["status"])

@app.route('/toggle', methods=['POST'])
def toggle():
    global lamp_state
    status = request.form.get("status")
    if status:
        lamp_state["status"] = status
    return render_template_string(HTML_PAGE, state=lamp_state["status"])

@app.route('/state', methods=['GET'])
def state():
    return jsonify(lamp_state)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)