from flask import Flask, request, render_template


app = Flask(__name__)




#index.html--------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


#ejercicio1.html----------------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = None
    total_sin_descuento = 0
    descuento = 0
    total_pagar = 0


    if request.method == 'POST':

        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        descuento1 = 15  # Porcentaje
        descuento2 = 25  # Porcentaje
        valorTarro = 9000

        print(f"Nombre: {nombre}, Edad: {edad}, Cantidad: {cantidad}")

        match edad:
            case _ if edad < 0:
                print("Error de datos")
            case _ if edad < 18:
                print("Este usuario no tiene descuento")
                descuento = 0
                total_sin_descuento = cantidad * valorTarro
                total_pagar = cantidad * valorTarro

            case _ if 18 <= edad <= 30:
                descuento = (cantidad * valorTarro ) * descuento1 / 100
                total_sin_descuento = cantidad * valorTarro
                total_pagar = (valorTarro * cantidad) - descuento
                print(f"Descuento de {descuento1}%, Total: {total_pagar}")

            case _:
                descuento = (cantidad * valorTarro) * descuento2 / 100
                total_sin_descuento = cantidad * valorTarro
                total_pagar = (valorTarro * cantidad) - descuento
                print(f"Descuento de {descuento2}%, Total: {total_pagar}")

    return render_template('ejercicio1.html',
                           nombre=nombre,
                           total_sin_descuento=total_sin_descuento,
                           descuento=int(descuento),
                           total_pagar=int(total_pagar)


#ejercicio2.html----------------------------------



@app.route('/ejercicio2')
def ejercicio2():




    return render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run()


