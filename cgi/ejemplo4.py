#!C:/Python/Python39/python.exe
import mysql.conector
import os
import cgi
import cgitb

print("Content-type: text/html")
print()
#En environ bienen tdas las opciones del servidor
metodo=os.environ["REQUEST_METHOD"]
if metodo == "GET":
    sql="SELECT *FROM usuarios"
    con=mysql.conector.connect(user='',password='',host='',database='')
    cursor=con.cursor()
    st.execute(sql)
    for(user,pass,tipo,nombre) in st:
        print("{},{},{},{}".format(user,pass,tipo,nombre))
        st.close()
        con.close()

elif metodo=="POST":
    print("Metodo agregar")
elif metodo=="PUT":
    print("Metodo actualizar")
elif metodo=="DELETE":
    print("Metodo borrar")
else:
    print("Metodo no aceptado")