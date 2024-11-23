from flask import Flask, render_template


app = Flask(__name__)



#index.html--------------------------------------
@app.route('/')
def home():
    return render_template('index.html')



#ejercicio1.html----------------------------------
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


if __name__ == '__main__':
    app.run()


