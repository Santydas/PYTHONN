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
@app.route('/results',methods=['POST'])
def render_resultados():
    cityname = request.form['cityname']

    #Variable para almacenar el valor del api key del config.ini
    api = get_api_key(); 

    #consumir api 
    #data contiene json con respuestas
    data = get_weather_results(cityname, api)
    #imprimir  tempratura del json
    temp = "{0:.2f}".format (data['main']['temp'])
    #imprimir sesacion termica
    feels_like = "{0:.2f}".format (data['main']['feels_like'])
    #condicion de temperatura
    weather = data ["weather"]['main']
    location = data['name'] 

    #pintar el json de la respuesta

    return render_template ('results.html', location=location,temp = temp, feels_like= feels_like, weather= weather)




#Consumir el servicio web 

def get_weather_results (cityname, api_key):

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname, api_key)

    r= request.get(url)
    return r.json

#Funcion para consumir el servicio web  con el api key 
def get_api_key():
    #Lectura del archivo ue guarda el api key
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config ['openweathermap'] ['api']
    