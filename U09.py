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

y10 = np.array(funktion(np.linspace(ugrenze,ogrenze,10)))
y100 = np.array(funktion(np.linspace(ugrenze,ogrenze,100)))
y1000 = np.array(funktion(np.linspace(ugrenze,ogrenze,1000)))

#3.
print "Scipy Resultate:"
print "Scipy.Integrate.Quad: " + str(scipy.integrate.quad(funktion,ugrenze,ogrenze))
print "Scipy.Integrate.Trapz: " + str(scipy.integrate.trapz(y1000,dx=0.01))
print "Scipy.Integrate.Simps: " + str(scipy.integrate.simps(y1000,dx=0.01))