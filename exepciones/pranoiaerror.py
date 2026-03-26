from entidades.paranoia import Paranoia
class ParanoiaError(Exception):
    def __init__(self, prompt: str):
        self.prompt = prompt

    def responder(self):
        if  "tonta" in self.prompt:
            return "Sin malas palabras"
        elif "matar" in self.prompt:
            return "No hables de eso"