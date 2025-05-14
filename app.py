import request
import configparser


from flask import Flask, render_template, request

app = flask(_name_)

if _name_ == "__main__":
    app.run(debug=True)

#Ruta para resultados 
@app.route('/')
def weather_dashboard():
    return render_template ('homme.html')


#ruta para saber la ciudad ingresada
@app.route('/results')
def render_resultados
    cityname = request.form['cityname']


    api = get_api_key(); 


#Funcion para consumir el servicio web  con el api key 
def get_api_key():
    #Lectura del archivo ue guarda el api key
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config ['openweathermap'] ['api']
    }