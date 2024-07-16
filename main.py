import psycopg2
from flask import Flask, request,redirect, render_template, url_for
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
    cursor.execute('''SELECT * FROM libros_view''')
    #Recuperar la información
    datos = cursor.fetchall()
    #Cerrar cursos y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():

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
    cursor.execute('''SELECT * FROM autores_view''')
    #Recuperar la información
    datos = cursor.fetchall()
    #Cerrar cursos y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
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
    cursor.execute('''SELECT * FROM pais''')
    #Recuperar la información
    datos = cursor.fetchall()
    #Cerrar cursos y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
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
    # Borrar el registro con el id_pais selecccionado
    cursor.execute('''DELETE FROM pais WHERE id_pais=%s''', (id_pais,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/update1_pais/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
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
    # recuperar el registro del id_pais seleccionado
    cursor.execute('''SELECT * FROM pais WHERE id_pais=%s''', (id_pais,))
    datos = cursor.fetchall()
    # id_pais = request.form['id_pais']
    # nombre = request.form['nombre']
    # datos = {
    #     'id_pais':id_pais,
    #     'nombre':nombre
    # }
    cursor.close()
    conexion.close()
    return render_template('editar_pais.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)


