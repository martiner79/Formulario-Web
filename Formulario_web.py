
from flask import Flask,request


formulario_html =  """

<!DOCTYPE html>
<html>
    <head><meta charset="utf-8"></head>
    <h2>
        <title>Formulario web</title>
    </h2>
    <body>
        <form method="POST"> 
            <p>Selecione un numero (Opcional): </p>
                <input type="radio" name="elección"/>1
                <input type="radio" name="elección"/>2
                <input type="radio" name="elección">3
                <br>
            <p>Los siguientes campos son obligatorios:</p>
            Nombre:<br>
            <input type="text" name="name">
                <br><br>
                Email:<br>
                <input type="text" name="email">
                <br><br>
                Descripción:<br>
                <textarea name="message"></textarea>
                <br><br>
                <input type="submit" value="Enviar datos">
        </form>
    </body>
</html>
"""

enviado_html = """
<!Doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Enviado</title>
        <meta http-equiv="refresh" content="3";URL="http://localhost:5000/form">
    </head>
    <body>
        ¡Los datos se han enviado correctamente!
    </body>
</html>
"""

campos_vacios_error_html = """
<!Doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Vacios</title>
        <meta http-equiv="refresh" content="3";URL="http://localhost:5000/form">
    </head>
    <body>
        Error: Compruebe que los campos no estén vacíos.
    </body>
</html>
"""



app = Flask(__name__)

@app.route("/")
def home():
    return '<h2>Bienvenido/a</h2>Puede visualizar el Formulario en <a href="http://localhost:5000/form">localhost:5000/form</a>'

@app.route("/form",  methods=["GET"])
def tomar_formulario():
    if request.method == "GET":
        return formulario_html.encode("utf-8")


@app.route("/form", methods = ["POST"])
def enviar_datos():
    if request.method == "POST":
        try:
            #Con esta función juntamos el contenido enviado en un diccionario.
            carga = dict(request.form)
            if carga["name"] and carga["email"] and carga["message"]:
                print(f"""
                *----------------------------°
                Nombre: {carga["name"]}
                Email: {carga["email"]}
                Descripción: {carga["message"]}
                °----------------------------*
                """)
                return enviado_html.encode("utf-8")
            else:
                return campos_vacios_error_html.encode("utf-8")
        except Exception:
            return campos_vacios_error_html.encode("utf-8")
    else:
        return campos_vacios_error_html.encode("utf-8")




if __name__ == "__main__":
    app.run("localhost",port=5000, debug=True)
