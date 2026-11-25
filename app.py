from flask import Flask, render_template, request

app = Flask(__name__)

VALOR_TARRO = 9000

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = int(request.form.get("edad", "0"))
        cantidad = int(request.form.get("cantidad", "0"))

        total = cantidad * VALOR_TARRO

        if 18 <= edad <= 30:
            porcentaje_descuento = 15
        elif edad > 30:
            porcentaje_descuento = 25
        else:
            porcentaje_descuento = 0

        descuento = total * porcentaje_descuento / 100
        total_pagar = total - descuento

        return render_template(
            "resultado1.html",
            nombre=nombre,
            edad=edad,
            cantidad=cantidad,
            total=total,
            porcentaje_descuento=porcentaje_descuento,
            descuento=descuento,
            total_pagar=total_pagar
        )

    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    tipo_mensaje = ""

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip().lower()
        contrasena = request.form.get("contrasena", "")

        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"
            tipo_mensaje = "exito"
        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"
            tipo_mensaje = "exito"
        else:
            mensaje = "Usuario o contraseña incorrectos"
            tipo_mensaje = "error"

    return render_template("ejercicio2.html", mensaje=mensaje, tipo_mensaje=tipo_mensaje)

if __name__ == "__main__":
    app.run(debug=True)
