from flask import Flask , render_template 
from flask_socketio import SocketIO


#TODO Crear la aplicacion Flask
app=Flask(__name__)

#TODO CONFIGURACION DE LA CLAVE SECRETA PARA CONFIGURACIONES 
app.config["SECRET_KEY"]="qwerty1232"

#TODO Incializar SocketIO con la aplicaionde FLASK 
socketio=SocketIO(app)


@app.route("/")
def index():
    return render_template("realtime.html")

@socketio.on("mensaje")
def manejar_mensaje(data):
    #TODO obterner el nombre y el nuevo mensaje del diccionario "data"
    nombre=data["nombre"]
    nuevo_mensaje=data["mensaje"]

#Emitir un evento actualizar_mensaje a odos los clientes conectados
    socketio.emit("actualizar_mensajes",{"nombre":nombre,"mensaje":nuevo_mensaje})


if __name__=="__main__":
    socketio.run(app,debug=True)