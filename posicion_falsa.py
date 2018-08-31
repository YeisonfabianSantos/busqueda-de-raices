# Posicion falsa 

import numpy as np 

funcionx=lambda x:x**3+4*x**2-10         #declaramos la funcion 

#ingresamos datos
a=1
b=2
tolera=0.001

#busqueda de raices
tabla=[]
fa=funcionx(a)
fb=funcionx(b)
c=b-fb*(a-b)/(fa-fb)
fc=funcionx(c)
tramo=abs(c-a)
tabla=[[a,b,c,fa,fb,fc,tramo]]

while(tramo>tolera):
    cambia=np.sign(fa)*np.sign(fc)
    if(cambia>0):
        a=c
    else:
        b=c
    fa=funcionx(a)
    fb=funcionx(b)
    c=b-fb*(a-b)/(fa-fb)
    fc=funcionx(c)
    tramo=abs(c-a)
    tabla.append([a,c,b,fa,fb,fc,tramo])

tabla=np.array(tabla)
resultado=c

#buscando la respuesta
fa=funcionx(a)
fb=funcionx(b)
cambia=np.sign(fa)*np.sign(fb)
if(cambia>0):
    resultado=np.nan

#imprimimos
print('[a,\t b, \t c, \t f(a), \t f(b), \t f(c),tramo]')
n=len(tabla)
np.set_printoptions(precision=4)
for i in range(0,n,1):
    print(tabla[i])
print('la raiz es:', resultado)
