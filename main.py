from entidades.paranoia import Paranoia
from exepciones.pranoiaerror import ParanoiaError
try:
    print("Puedes hacerle una pregunta a Paranoia.")
    prompt = input()
    paranoia = Paranoia(prompt)

    respuesta = paranoia.responder()
    print(respuesta)

except ParanoiaError as e:
    print(e.mensaje)
