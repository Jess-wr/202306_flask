from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def tablero_grande():
    return render_template("index.html") 

@app.route('/<int:num>')
def tablero_2(num=4):
    return render_template("board.html", num=num)

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html", banana=banana, num=num)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

"""
@app.route('/play')
def level_one():
    return render_template("index.html",num=3,color="blue")

@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", num=num, color=color)
    """