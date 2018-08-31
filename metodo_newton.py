#metodo de newton-raphson

import numpy as np
import matplotlib as plt

funcionx=lambda x:x**3+4*x**2-10
fxderiva=lambda x:3*(x**2)+8*x

#ingresamos datos
xi=2
tolera=0.001

#busqueda de raices
tabla=[]
tramo=abs(2*tolera)
while(tramo>=tolera):
    xnuevo=xi-funcionx(xi)/fxderiva(xi)
    tramo=abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi=xnuevo
    
tabla=np.array(tabla)
n=len(tabla)

#imprimimos
print(['xi','xnuevo','tramo'])
np.set_printoptions(precision=4)
for i in range(0,n,1):
    print(tabla[i])
print('raiz en: ',xi)