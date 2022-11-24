'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 14: Manejo De Archivos
Archivo De Funciones
Fecha: 24 De Noviembre De 2022
'''

import random
def guardar():
    try:
        archivo=open("SaveData.txt",'r')
        info=archivo.read()
        archivo=open("SaveData.txt",'a')
        archivo.write('El Archivo Existe')
        print(info)
        archivo.close()
    except Exception:
        print("El archivo no existe")

def listaNumeros():
    lista=[]
    f=open("listaNum.txt",'w')
    for x in range(10):
        num=random.randint(0,9)
        f.write(str(num)+' ')
        lista.append(num)
    f.write('\n')
    suma=sum(lista)
    mayor=max(lista)
    menor=min(lista)
    promedio=sum(lista)/len(lista)
    f.write("Número Mayor: "+str(mayor)+"\n")
    f.write("Número Menor: "+str(menor)+"\n")
    f.write("Suma De Elementos: "+str(suma)+"\n")
    f.write("Promedio: "+str(promedio)+"\n")
    f=open("listaNum.txt",'r')
    info=f.read()
    print(info)
    f.close()

def main():
    print("1) Guardar Texto En Archivo")
    print("2) Lista De Números Aleatorios")
    opc=int(input("Selecciona Una Opción: "))
    while opc<1 or opc>2:
        opc=str(input("Selecciona Una Opción: "))
    if opc==1:
        guardar()
    else:
        listaNumeros()