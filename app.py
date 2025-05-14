import request
import configparser


from flask import Flask, render_template, request

app = flask(_name_)

if _name_ == "__main__":
    app.run(debug=True)


@app.route('/')
def weather_dashboard():
    return render_template ('homme.html')


@app.route('/results')
def render_resultados
    cityname = request.form['cityname']

    api=