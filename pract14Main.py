'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 14: Manejo De Archivos
Archivo Main
Fecha: 24 De Noviembre De 2022
'''

import pract14Func as pf
opc=1
while opc==1:
    try:
        pf.main()
        opc=int(input("Continuar? (0/1): "))
        while opc<0 or opc>1:
            opc=int(input("Continuar? (0/1): "))
    except:
        print("Parametros No Válidos")