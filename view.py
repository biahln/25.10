#Classe de visualização
class View:
    def __init__(self):
        self.control=None
    #Guarda control associada
    def set_control(self,control):
        self.control=control
    #Método de exibição do menu
    def exibir_menu(self):
        resposta = True

        while resposta:
            print('''
            1.Exibir lista
            2.Incluir item
            3.Excluir item
            4.Sair 
            ''')

            #Solicitar opção
            resposta=input('Digite um número: ')

            #Verifica a resposta
            if resposta=='1':
                print('\n Lista de itens')
            elif resposta=='2':
                print('\n Item concluído')
            elif resposta=='3':
                print('\n Item excluído')
            elif resposta=='4':
                print('\n Tchau, i have to go now')
                resposta=False
            else:
                print('\n Valor incorreto')
    #Exibir lista de compras
    def exibir_lista_compras(self,lista_compras):
        for chave,valor in lista_compras.items:
            print()


