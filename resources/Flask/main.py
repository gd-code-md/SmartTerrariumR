try:
    import time
    import json
    import threading
    from ArduinoConnection import ArduinoConnection
    from flask import Flask, request, render_template, redirect, url_for
    from datetime import datetime
except Exception as eImp:
    print(f"Ocurrió el error de importación: {eImp}")

# Inicia coneccion con arduino
conn = ArduinoConnection()
sem = threading.Semaphore()
modo = ""

# Se crea la app, se instancia el framework para poder usarse.
app = Flask(__name__)
app.secret_key = "clave_secreta_flask"


@app.context_processor  # Context processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

#---------------------------------Endpoints------------------------------------#


@app.route('/', methods=["POST", "GET"])  # Ruta inicial del proyecto
def index():
    temp1 = 5.0
    temp2 = 44
    hum1 = 30
    global modo
    sem.acquire()
    if request.method == "POST":
        modo = request.form.get("modoOperacion")
    sem.release()

    if modo == 'true':
        return render_template('automatico.html', temp1=temp1, temp2=temp2, hum1=hum1)
    if modo == 'false':
        return render_template('manual.html', temp1=temp1, temp2=temp2, hum1=hum1)

    return render_template('bienvenida.html', dato1=modo)


# Agregar el contenido correspondiente a los html´s de automatico y manual.


@app.route('/automatico', methods=["POST", "GET"])
def automatico():
    temp1 = 5.0
    temp2 = 44
    hum1 = 30
    return render_template('automatico.html', temp1=temp1, temp2=temp2, hum1=hum1)


@app.route('/manual', methods=["POST", "GET"])
def manual():
    temp1 = 5.0
    temp2 = 44
    hum1 = 30
    return render_template('manual.html', temp1=temp1, temp2=temp2, hum1=hum1)


@app.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/raspberry')
def raspberry():
    Nombre = "GDCode"
    data = {
        "user": {
            "name": "satyam kumar",
        }
    }
    text = json.dumps(data)
    return render_template('rasp.html', Nom=Nombre, JsonString=text)


@app.route('/raspberry', methods=['POST'])
def my_form_post():
    Nombre = "GDCode"
    data = {
        "user": {
            "name": "satyam kumar",
        }
    }
    text = json.dumps(data)
    conn.initConnection()
    conn.recieving = True
    while conn.recieving is True:
        conn.writeArduino(text)
        time.sleep(.5)
        conn.readArduino()
    conn.closeConnection()
    return render_template('rasp.html', JsonString=text, send_data=conn.sendData,
                           received_data=conn.receivedData, Nom=Nombre)


#----------------------------Error Handlers------------------------------------#


@app.errorhandler(500)
def not_found(e):
    return render_template('errorHandlers/error500.html'), 500


#-------------------------------Execute----------------------------------------#

if __name__ == "__main__":
    # Con esto hacemos que el servidor de flasjk al arrancar y haya cambios en el código se registren los cambios, algo como django.
    app.run(host="127.0.0.1", port=5000, debug=False)
