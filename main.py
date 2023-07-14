from flask import Flask, request, jsonify, abort
from datetime import datetime

app = Flask(__name__)

class Operacion:
  def __init__(self, numero_destino ,  Valor):
    self.numero_destino = numero_destino
    self.fecha = datetime.now().strftime('%d/%m/%Y')
    self.valor = Valor


class Cuenta:
  def __init__(self, numero, nombre, saldo, contacts):
      self.numero = numero
      self.saldo = saldo
      self.nombre = nombre
      self.contacts = list(contacts)
      self.historial = []
  

  def newOperation(self, valor : Operacion):
    new_Operation = "Realizado en  " + str(valor.fecha)  
    self.historial.append(new_Operation)


BD = [
    Cuenta("21345", "Arnaldo", 200, ["123", "456"]),
    Cuenta("123", "Luisa", 400, ["456"]),
    Cuenta("456", "Andrea", 300, ["21345"])
]


def get_cuenta(numero_cuenta):
    for n in BD:
        if n.numero == numero_cuenta:
            return n
    return None

def get_contacts(cuenta):
    contactos = {}
    for contacto in cuenta.contacts:
        contactos[contacto] = get_cuenta(contacto).nombre
    return contactos


@app.route("/billetera/contactos", methods=["GET"])
def billetera_contactos():
    numero_cuenta = request.args.get("minumero")    
    if numero_cuenta is None:
        return jsonify({
            "success" : "true",
            "status": 404,
            "body": "Not Found"
        })
    
    cuenta = get_cuenta(numero_cuenta)
    if cuenta is None:
        return jsonify({
            "success" : "true",
            "status": 404,
            "body": "Not Found"
        })

    contactos = get_contacts(cuenta)
    
    return jsonify(
        {
          "status": 200,
          "contactos" : contactos
        }
    )


@app.route("/billetera/pagar", methods=["GET"])
def billetera_pagar():
    enviante = request.args.get("minumero")
    destino = request.args.get("numerodestino")
    valor_dinero = request.args.get("valor")
    
    usuario1 = get_cuenta(enviante)
    usuario2 = get_cuenta(destino)
    
    if usuario1 is None or usuario2 is None:
        return jsonify(
            {
              "status": 404,
              "body": "User Not Found"
            }
        )
    if destino not in usuario1.contacts:
        return jsonify(
            {
              "status": 400,
              "body": "Not Contact"
            }
        )

    trans = Operacion(destino, valor_dinero)
    usuario2.newOperation( trans)

    return jsonify({
        "status": 200,
        "body": "Realizado en " + str(trans.fecha )
    })



@app.route("/billetera/historial", methods=["GET"])
def billetera_historial():
    nombre = request.args.get("minumero")
    usuario = get_cuenta(nombre)
    if usuario is None:
        return jsonify(
            {
            "status": 404,
            "body": "Usuario Not Found"
            }
        )
    
    historial = usuario.historial
    
    return jsonify({
        "status": 200,
        "historial" : historial
        })



if __name__ == "__main__":
    app.run()

