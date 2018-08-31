# metodo de la secante
# busca de raices de un polinomio

import numpy as np
import matplotlib.pyplot as plt


funcionx=lambda x:x**3+4*x**2-10
x=np.linspace(0,9,100)
plt.plot(x,x**3+4*x**2-10)       # graficamos la funcion ha resolver 
    

def secante_tabla(funcionx,xa,tolera):
    dx=4*tolera              #delta de x 
    xb=xa+dx                 #un paso mas que xa
    tramo=dx
    tabla=[]
    while (tramo>=tolera):
        fa=funcionx(xa)
        fb=funcionx(xb)
        xc=xa-fa*(xb-xa)/(fb-fa)
        tramo=abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb=xa
        xa=xc
    tabla=np.array(tabla)
    return(tabla)
	
	#ingresamos datos
a=1
b=2
xa=1.5
tolera=0.001
tramos=100

tabla=secante_tabla(funcionx,xa,tolera)
n=len(tabla)
raiz=tabla[n-1,2]

np.set_printoptions(precision=4)
print('[xa,\t xb,\t xc,\t tramo]')
for i in range(0,n,1):
    print(tabla[i])
print('raiz en: ',raiz)


# añadiendo la grafica
xi=np.linspace(a,b,tramos+1)
fi=funcionx(xi)
dx=(b-xa)/2
m=(funcionx(xa+dx)-funcionx(xa))/(xa+dx-xa)        #pendiente
b0=funcionx(xa)-m*xa
tangentei=m*xi+b0
fxa=funcionx(xa)
xb=xa+dx
fxb=funcionx(xb)

plt.plot(xi,fi,label='f(x)')
plt.plot(xi,tangentei,label='secante')
plt.plot(xa,funcionx(xa),'go',label='xa')
plt.plot(xa+dx,funcionx(xa+dx),'ro',label='xb')
plt.plot((-b0/m),0,'yo',label='xc')
plt.plot([xa,xa],[0,fxa],'pendiente')
plt.plot([xb,xb],[0,fxb],'pendiente')
plt.axhline(0,color='k')
plt.title('Metodo de la secante')
plt.show()