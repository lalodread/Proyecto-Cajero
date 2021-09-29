# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:49:16 2021
@author: jozic
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

#Clase Cliente
class Cliente: 
    
    #Metodo Init de la clase cliente                
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno,  cuenta):
        self._nombre=nombre
        self._apellidoPaterno=apellidoPaterno
        self._apellidoMaterno=apellidoMaterno
        self._cuenta = cuenta
    
    #Metodo para calcular RFC 
    def calcularRfc(self, nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento):
        self._vocales=[]
        self._fechaNacimiento=list(fechaNacimiento)
        self._listaNombre=list(self._nombre)
        self._listaApellidoPaterno=list(self._apellidoPaterno)
        self._listaApellidoMaterno=list(self._apellidoMaterno)
        for vocal in self._listaApellidoPaterno:
            if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
                self._vocales.append(vocal.upper())
        self._rfcCliente=self._listaApellidoPaterno[0]+self._vocales[0]+self._listaApellidoMaterno[0]+self._listaNombre[0]+self._fechaNacimiento[2]+self._fechaNacimiento[3]+self._fechaNacimiento[5]+self._fechaNacimiento[6]+self._fechaNacimiento[8]+self._fechaNacimiento[9]
        return self._rfcCliente
    
    #Metodo para calcular Edad
    def calcularEdad(self, fechaNacimiento):
        self._fechaNacimiento=datetime.strptime(fechaNacimiento, "%Y/%m/%d")
        self._edad = relativedelta(datetime.now(), self._fechaNacimiento)
        self._edadCliente=self._edad.years
        return self._edadCliente
    
    #Getters para el nombre 
    @property
    def nombre(self):
        return self._nombre
    def apellidoPaterno(self):
        return self._apellidoPaterno  
    def apellidoMaterno(self):
        return self._apellidoMaterno
    def rfc(self):
        return self._listaNombre

    #Getters para la cuenta 
    @property
    def cuenta(self):
        return self._cuenta

    #Setters para el nombre 
    @nombre.setter
    def nombre(self, nombre): 
        self._nombre=nombre

    #Setters para la cuenta
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta=cuenta
    def hacer_deposito(self, cantidad):
        self._cuenta.depositar(cantidad)
    def hacer_retiro(self, cantidad):
        self._cuenta.retirar(cantidad)
   
    #Metodo String 
    def __str__(self):
        return f'Nombre del cliente:{self._nombre} {self._apellidoPaterno} {self._apellidoMaterno}\n{self._cuenta}\nRFC del cliente:{self._rfcCliente}\nEdad de cliente:{self._edadCliente}'

#Clse Cuenta
class Cuenta:
    #Metodo init
    def __init__(self, saldo):
        self._saldo = saldo
    
    #Getters para el saldo 
    @property
    def saldo(self):
        return self._saldo
    
    #Setters para el saldo
    @saldo.setter
    def saldo(self, cantidad):
        self._saldo=cantidad  
    
    #Metodo deposito
    def depositar(self, cantidad):
        self._saldo += cantidad
    
    #Metodo retiro 
    def retirar(self, cantidad):
        if self._saldo > cantidad:
            self._saldo -= cantidad
        else:
            print(f"Saldo insuficiente\nEl saldo actual es: {self.saldo:0.2f}")
    
    #Metodo String
    def __str__(self):
        return f'Saldo en cuenta: {self._saldo:0.2f}'

        
    

    