# Importar o app, builder (GUI)
# Criar nosso aplicativo
# Criar a função build

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    