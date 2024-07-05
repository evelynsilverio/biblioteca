import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libros')
def libros():
    #Conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a",
        user="postgres",
        password="chikis03",
        host="localhost",
        port="5432"
    )

    #Crear un cursor(objeto para recorrer las tablas)
    cursor = conexion.cursor()
    #Ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libro''')
    #Recuperar la información
    datos = cursor.fetchall()
    #Cerrar cursos y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)


