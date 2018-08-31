#Punto fijo

import numpy as np
import matplotlib.pyplot as plt

funcionx=lambda x:np.exp(-x)-x
funciongx=lambda x:np.exp(-x)

#ingresamos datos
a=0
b=1
tolera=0.001
tramos=101

def puntofijo(gx,a,tolera,n=15):
    i=1
    b=gx(a)
    tramo=abs(b-a)
    while(tramo>=tolera and i<=n):
        a=b
        b=gx(a)
        tramo=abs(b-a)
        i=i+1
    respuesta=b

#buscando la respuesta

    if(i>=n):
        respuesta=np.nan
    return(respuesta)

respuesta=puntofijo(funciongx,a,tolera)       #procedimiento


#buscando la respuesta

print('la raiz es:',respuesta)

#graficamos

xi=np.linspace(a,b,tramos)
fi=funcionx(xi)
gi=funciongx(xi)
yi=xi
plt.plot(xi,fi,label='f(x)',color='r')
plt.plot(xi,gi,label='g(x)',color='b')
plt.plot(xi,yi,label='y=x',color='y')
plt.axvline(respuesta)
plt.title('Punto Fijo')
plt.show()
