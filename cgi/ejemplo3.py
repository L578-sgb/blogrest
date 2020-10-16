#!C:/Python/Python39/python.exe
import os
import cgi

print("Content-type: text/html")
print()
#valorGet es un arreglo que guarda todo lo que le mandan en el formulario
valoresGet = cgi.FieldStorage()
nA=valoresGet["numeroA"].value
nB=valoresGet["numeroB"].value

r=int(nA)+int(nB)
#En %s va imprimir lo que tenga r
#print("La suma es %s" % r)
#Otra forma de hacerlo con el format
print("La suma {} mas {} es: {}".format(nA,nB,r))