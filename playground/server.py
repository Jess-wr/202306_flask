from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/play')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def playground1():
    return render_template("index.html")

@app.route('/play/<int:num>')
def playground2(num):
    return render_template("hello.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def playground3(num, color):
    return render_template("hello.html", num=num, color=color)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

