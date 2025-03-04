# Importar o app, builder (GUI)
# Criar nosso aplicativo
# Criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text = 'Dolar R${:.2f}'.format(self.pegar_cotacao('USD'))
        self.root.ids["moeda2"].text = 'Euro R${:.2f}'.format(self.pegar_cotacao('EUR'))
        self.root.ids["moeda3"].text = 'Peso Mexicano R${:.2f}'.format(self.pegar_cotacao('MXN'))
        self.root.ids["moeda4"].text = 'Bitcoin R${:.2f}'.format(self.pegar_cotacao('BTC'))     

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        valor = float(dic_requisicao[f'{moeda}BRL']['bid'])
        return valor

MeuAplicativo().run()