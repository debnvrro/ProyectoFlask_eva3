from flask import Flask, render_template, request

# Inicialización de la aplicación Flask
app = Flask(__name__)


# Ruta principal: Menú inicial con dos botones
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para el Ejercicio 1: Cálculo de promedio de notas y asistencia
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        # Recepción de datos desde el formulario HTML
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Cálculo del promedio de las 3 notas
        promedio = round((nota1 + nota2 + nota3) / 3, 1)

        # Evaluación de condiciones de aprobación (Promedio >= 40 y Asistencia >= 75%)
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


# Ruta para el Ejercicio 2: Determinar el nombre con mayor cantidad de caracteres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    cantidad_caracteres = None

    if request.method == 'POST':
        # Recepción de los 3 nombres desde el formulario HTML
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Almacenamiento en lista y búsqueda del nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad_caracteres=cantidad_caracteres)


if __name__ == '__main__':
    # Ejecución de la aplicación en modo depuración
    app.run(debug=True)