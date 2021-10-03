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
    
    
    class fecha():


    # init method or constructor
    def __init__(self, year ,month ,day ):
        self.dia = day
        self.mes = month
        self.año = year


    def validar(self):
        mes = int(self.mes)
        año = int(self.año)
        dia = int(self.dia)

        if (año < 1900 or año > 2021 ):
            print("año invalido")
            exit()
        else:
            print("año valido")

        if (mes < 1 or mes > 12):
            print("mes invalido")
            exit()
        else:
            print("mes valido")

        bisiesto = False
        if año % 4 != 0:  # no divisible entre 4
            bisiesto = False
        elif año % 4 == 0 and año % 100 != 0:  # divisible entre 4 y no entre 100 o 400
            bisiesto = True
        elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:  # divisible entre 4 y 10 y no entre 400
            bisiesto = False
        elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:  # divisible entre 4, 100 y 400
            bisiesto = True

        print(bisiesto)
        diasmes = 0
        if mes in [4, 6, 9, 11]:
            diasmes = 30
            # Febrero depende de si es o no bisiesto
        if mes == 2:
            if bisiesto == True:
                diasmes = 29
            else:
                diasmes = 28
        else:
            # En caso contrario, tiene 31 días
            diasmes = 31
        print(diasmes)

        if (dia < 1 or dia > diasmes):
            print("día invalido")
            exit()
        else:
            print("dia valido")
    def generar_fecha_letra(self):
        mes = int(self.mes)
        año = int(self.año)
        dia = int(self.dia)
        d1 = datetime(año, mes, dia)

        def current_date_format(d1):
            months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                      "Noviembre", "Diciembre")
            day = d1.day
            month = months[d1.month - 1]
            year = d1.year
            messsage = "{} de {} del {}".format(day, month, year)
            return messsage
        print (current_date_format(d1))
    def _str_(self):
        mes = int(self.mes)
        año = int(self.año)
        dia = int(self.dia)
        d1 = datetime(año, mes, dia)


        print (d1.strftime("%d/%m/%Y "))





validarf = fecha("2021","2", "16")


validarf.validar()
validarf.generar_fecha_letra()
validarf._str_()
