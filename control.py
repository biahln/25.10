#Classe de controle
class Control:
    #Método construtor:
    def __init__(self,view,model):
        #Atributos
        self.view=view
        self.model=model

    #Método para exibir menu
    def exibir_menu(self):
        # Acionar o método da classe View
        self.view.exibir_menu()
    def get_lista_compras(self):
        return self.model.get_lista_compras()
