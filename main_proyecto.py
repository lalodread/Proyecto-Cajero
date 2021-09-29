# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:57:12 2021

@author: jozic
"""
from Clases_proyecto import Cliente, Cuenta
from datetime import datetime

cuentas = {'12345': ['1234','Sandra','Sanchez', 'Solis', 3000.00, '1965/03/27'], '98765': ['1234','Fernando','Espinoza', 'Palacios', 10000.00, '1950/04/26'] }



def tipoUsuarios():
    tipo=0
    while tipo == 0:
        usuarioTipo=int(input("Que tipo de usuario es:\n1.-Gerente\n2.-Cliente\nOpcion: "))
        if usuarioTipo == 1:
            passwordGerente = 0 
            while passwordGerente==0:
                passwdGerente=str(input("Ingrese password: "))
                if passwdGerente == "root":
                    gerente()                    
                    break
                else:
                    print("Pasword incorrecto, intente nuevamente")
        elif usuarioTipo == 2:
            datosCliente()
            break
        else:
            print("Opcion incorrecta, ingrese una opcion valida")

def gerente():
    opcionTipo = 0 
    while opcionTipo == 0:
        opcionGerente=int(input("Selecciona una operacion:\n1.-Agregar cuenta\n2.-Eliminar cuenta\n3.-Salir\nOpcion: "))
        if opcionGerente == 1:
            cuentaUsuario=str(input("Ingrese numero de cuenta a agregar: "))
            if cuentaUsuario in cuentas.keys():
                print("Numero de cuenta ya asignado")
            else:
                passUsuario=str(input("Defina un password numerico para el cliente: "))
                nombreUsuario=str(input("Ingrese nombre de cliente: "))
                apPaternoUsuario=str(input("Ingrese apellido paterno de cliente: "))
                apMaternoUsuario=str(input("Ingrese apellido materno de cliente: "))
                saldoUsuario=float(input("Ingrese saldo inicial en cuenta en formato 00.00: "))
                fechaUsuario=str(input("Ingrese fecha de nacimiento en formato YYYY/MM/DD: "))
                cuentas[cuentaUsuario]=[passUsuario,nombreUsuario, apPaternoUsuario, apMaternoUsuario, saldoUsuario, fechaUsuario]
        elif opcionGerente == 2:
            cuentaUsuario=str(input("Ingrese numero de cuenta a eliminar: "))
            try:
                del cuentas[cuentaUsuario]
            except:
                print("La cuenta no existe")
        elif opcionGerente == 3:
            opcionTipo = 1 
        else:
            print("La opcion es incorrecta, por favor ingrese otra")

def datosCliente ():    
    cajeroEncendido = 0
    while cajeroEncendido == 0:
        global numeroCuenta
        numeroCuenta=str(input("Ingrese numero de cuenta: "))
        if numeroCuenta in cuentas.keys():
            nombreCliente=cuentas.get(numeroCuenta, [])[1]
            apellidoPaternoCliete=cuentas.get(numeroCuenta, [])[2]
            apellidoMaternoCliente=cuentas.get(numeroCuenta, [])[3]
            fechaNacimientoCliente=cuentas.get(numeroCuenta, [])[5]
            passwordCliente=cuentas.get(numeroCuenta, [])[0]
            cuentaCliente=cuentas.get(numeroCuenta, [])[4]
            correctPass=0
            while correctPass==0:
                password=str(input("Ingrese password: "))
                if password == passwordCliente:
                    ejecutarClases(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente)
                    break
                else:
                    print("Pasword incorrecto, intente nuevamente")
        else:
            print("El numero de cuenta no existe, ingrese otro")

def menuCuenta(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente):
    opcionSeguir = 0
    while opcionSeguir == 0:
        otra=int(input("Desea hacer otra operacion:\n1.-Si\n2.-No\nOpcion:"))
        if otra == 1:
           ejecutarClases(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente)
        elif otra == 2:
            tipoUsuarios()
            opcionSeguir = 1
        else:
            print("Opcion no valida")

def generarReporte(operacionReporte, cantidad, cuentaCliente, numeroCuenta):
    fechaActual = datetime.now()
    archivo=open(f'movimientos_{numeroCuenta}.txt', mode='a')
    archivo.write(f'Fecha:{fechaActual}\nOperacion:{operacionReporte}\nMonto:{cantidad}\nBalance:{cuentaCliente}\n\n')
    archivo.close()    

def leerReporte(numeroCuenta):
    with open(f'movimientos_{numeroCuenta}.txt', mode='r') as archivo:
        for registro in archivo:
            print(f'{registro}')

def ejecutarClases(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente):
    flag=0
    while flag == 0:
        operacion=int(input("Ingrese operacion a realizar:\n1.-Consultar datos\n2.-Depositar\n3.-Retirar\n4.-Generar reporte\n5.-Salir\nOpcion:"))
        if operacion == 1 :
            cuenta = Cuenta(cuentaCliente)
            fecha=fechaNacimientoCliente
            cliente=Cliente(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente,cuenta)
            cliente.calcularRfc(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fecha)
            cliente.calcularEdad(fecha)
            print(cliente)
            menuCuenta(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente)
        elif operacion == 2:
            cuenta = Cuenta(cuentaCliente)
            fecha=fechaNacimientoCliente
            cliente=Cliente(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente,cuenta)
            cliente.calcularRfc(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fecha)
            cliente.calcularEdad(fecha)
            cantidadDeposito=int(input("Ingrese monto a depositar: "))
            cliente.hacer_deposito(cantidadDeposito)
            print(cliente)
            cuentas.get(numeroCuenta, [])[4]=cliente.cuenta.saldo
            cuentaCliente = cliente.cuenta.saldo
            operacionReporte = "Deposito"
            generarReporte(operacionReporte, cantidadDeposito, cuentaCliente, numeroCuenta)
            menuCuenta(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente)
        elif operacion == 3:
            cuenta = Cuenta(cuentaCliente)
            fecha=fechaNacimientoCliente
            cliente=Cliente(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente,cuenta)
            cliente.calcularRfc(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fecha)
            cliente.calcularEdad(fecha)
            cantidadRetiro=int(input("Ingrese monto a retirar: "))
            cliente.hacer_retiro(cantidadRetiro)
            print(cliente)
            cuentas.get(numeroCuenta, [])[4]=cliente.cuenta.saldo
            cuentaCliente = cliente.cuenta.saldo
            operacionReporte = "Retiro"
            generarReporte(operacionReporte, cantidadRetiro,cuentaCliente, numeroCuenta)
            menuCuenta(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente)
        elif operacion == 4:
            leerReporte(numeroCuenta)
            menuCuenta(nombreCliente, apellidoPaternoCliete, apellidoMaternoCliente, fechaNacimientoCliente, cuentaCliente)
        elif operacion==5:
            flag=1
            tipoUsuarios()
        else:
            print("Opcion no valida, ingrese otra")

if __name__ == '__main__':
    tipoUsuarios()

                