#Programa principal

#Importação de classes
from view import View
from control import Control
from model import Model
#Instanciar a View
m =Model()
v =View()
#Instanciar a Control
c =Control (v,m)

v.set_control(c)
#Exibir o menu
c.exibir_menu()