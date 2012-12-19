#!/usr/bin/python
# encoding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.integrate

"""Übung 09 Integrieren mit numpy"""
#Markus Klemm WS12/13 Phy-BA

funktion = lambda x: (np.exp(x/10)*np.sin(x) + x) / (np.log(x**2 + 10))
ugrenze = 0
ogrenze = 10

#1.
def Mittelpunktregel(func,a,b,n=1000):
    """Gibt das numerische Integral der übergebenen Funktion von den Integrationsgrenzen a bis b zurück. 
    Die Stützstellenzahl n kann optinal angegeben werden, standardmäßig verwendet wird 1000"""
    
    x = np.linspace(a,b,n+1)
    
    mk_as = x[:-1]
    mk_bs = x[1:]
    
    #func(((a + b) / 2)) * (b-a)
    
    return np.sum(func(((mk_as + mk_bs) / 2)) * (mk_bs - mk_as))
    
    

#2.
for x in [10,100,1000]:
    print "Integrale mit " + str(x) + " Stützstellen:"
    print "Mithilfe der Mittelpunktregel: " + str(Mittelpunktregel(funktion,ugrenze,ogrenze,x))


#3.
y1000 = np.array(funktion(np.linspace(ugrenze,ogrenze,1000)))

print "Scipy Resultate:"
print "Scipy.Integrate.Quad: " + str(scipy.integrate.quad(funktion,ugrenze,ogrenze))
print "Scipy.Integrate.Trapz: " + str(scipy.integrate.trapz(y1000,dx=0.01))
print "Scipy.Integrate.Simps: " + str(scipy.integrate.simps(y1000,dx=0.01))

#4.
plt.title("$f_{(x)}$")
plt.plot(y1000,label="$f_{(x)}$")
plt.show()