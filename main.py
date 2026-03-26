from entidades.paranoia import Paranoia
from exepciones.pranoiaerror import ParanoiaError

try:
    print("Puedes hacer una pregunta a Paranoia")
    pregunta = input()

    respuesta = Paranoia(pregunta).responder()
    print(respuesta)
    
except ParanoiaError as e:
    print(e.responder())