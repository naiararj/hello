from flask import Flask

app = Flask(__name__)

@app.route("/medianotas/<x>/<y>/<z>")
def medianotas(x,y,z):
    soma=float(x)+float(y)+float(z)
    mediaformatada=soma/3 
    if(mediaformatada>=60):
        return "Você foi aprovado"
    elif(mediaformatada<60):
        return "Você foi reprovado"

