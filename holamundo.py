from flask import Flask,render_template_string

app=Flask(__name__)

@app.route("/")
def hola_mundo():
    contenido_html="""
      """
    return render_template_string(contenido_html)

if __name__== "__main__":
    app.run(debug=True)