import random
from exepciones.pranoiaerror import ParanoiaError
from colorama import Fore
class Paranoia:
    def __init__(self, prompt: str):
        self.prompt = prompt

    def responder(self):
        respuesta = [ 
            "jaja ¿para qué quieres saber eso? saludos", 
            "ni tú sabes eso y me estás preguntando a mí", 
            "yo solo sé que no sé nada", 
            "puede que sí, puede que no, pero lo más seguro es que quién sabe xD",
            "simón, al rato..."
        ]
        
        if self.prompt == "tonta":
            raise ParanoiaError(f"{Fore.RED}No hables de eso")

        elif self.prompt == "matar":
            raise ParanoiaError(f"{Fore.RED}Sin matar a nadie")

        return f"{Fore.GREEN}{random.choice(respuesta)}"