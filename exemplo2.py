from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial


class Tela(BoxLayout):
    orientation = 'vertical'
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        self.textosTela1 = ["1","2","3"]
        self.textosTela2 = [["dale1","dale1","dale1"],["dale2","dale2","dale2"],["dale3","dale3","dale3"]]
        self.tela = 0
        self.resposta = []

        self.montaTela()

    def montaTela(self):
        self.clear_widgets()
        aux = 0
        t = Button(text="valida")
        t.bind(on_press=partial(self.valida,teste=2))
        self.add_widget(t)
        for i in self.textosTela2[self.tela]:
            b = Button(text=i)
            b.bind(on_press = partial(self.buttonAction,indice=aux))
            self.add_widget(b)
            aux+=1


    
    def buttonAction(self,instance, **kargs):
        self.resposta.append(kargs["indice"])
        self.tela+=1
        self.montaTela()

    def valida(self, instance, **kargs):
        print(self.resposta)

class MainApp(App):
    def build(self):
        return Tela()


MainApp().run()