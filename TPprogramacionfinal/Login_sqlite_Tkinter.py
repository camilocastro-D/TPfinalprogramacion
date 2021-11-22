'''
	
	
'''

from tkinter import *						
import tkinter as tk	

from tkinter import messagebox as mb	#Nos permite abrir ventanas de mensajes
import sqlite3							#Nos permite conectarnos a una base de datos 

ventana=tk.Tk()
ventana.title("FARMACIA")	#Titulo de la ventana principal
ventana.geometry("280x450+300+250")	#Tamaño de nuestra ventana Principal
	
color='#c5e2f6'			#color de fondo usado
ventana['bg']=color		#Definimos nuestra ventana 'bg' con el valor 'color'
Label(ventana,bg=color,text="FARMACIA",font=("Arial Black",16)).pack()	#Mostramos texto 'FARMACIA'


#Cajas de nuestra ventana Principal
Label(ventana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Usuario:'
caja1=Entry(ventana,font=("Arial",10))										#Creamos una caja de texto 'caja1'
caja1.pack()																#Posicion de la 'caja1'
Label(ventana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña:'
caja2=Entry(ventana,show="*")												#Creamos la 'caja2' (contraseña)
caja2.pack()																#Posicion de 'caja2'

db=sqlite3.connect('login.db')		#Nos conectamos a nuestra base de datos 'login.db'
c=db.cursor()						#creamos un cursor

def login():				#Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
	usuario=caja1.get()		#Obtenemos el valor de la 'caja1' (usuario)
	contr=caja2.get()		#Obtenemos el valor de la 'caja2' (contraseña)
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))	#Seleccionamos datos '(usuario,contr)'
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		#Mostramos 'Login Correcto'
		if cargar_productos():
			Button(ventana,text="Cargar",bg='#a6d4f2',command=cargar_productos,font=("Arial Rounded MT Bold",10)).pack()

		else:
			print("sssssssssssssss")

	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	#Mostramos 'Login incorrecto'
	



def cargar_productos():													#Funcion cargar_productos ... nos permote cargar los registros
	newVentana =tk.Toplevel(ventana)
	newVentana.title("carga de productos")
	newVentana.geometry("300x290+800+250")
	newVentana['bg']=color
	labelExample=tk.Label(newVentana,text="ENTRAR : ",bg=color,font=("Arial Black",12)).pack(side="top")
	Label(newVentana,text="Producto : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Producto:'
	caja8=Entry(newVentana)															#Creamos 'caja8' (Producto)
	caja8.pack()
	Label(newVentana,text="Precio : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'precio'
	caja9=Entry(newVentana)															#Creamos 'caja9' (Precio)
	caja9.pack()
	Label(newVentana,text="Metodo de pago : ",bg=color,font=("Arial Black",10)).pack()	#Texto ',etododepao'
	caja10=Entry(newVentana)															#Creamos 'caja10' (Metododepago)
	caja10.pack()
	buttons=tk.Button(newVentana,text="Cargar !",command=cargar_productos,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	def subir_productos():
		Producto=caja8.get()
		Precio=caja9.get()
		Metodo=caja10.get()
		buttons=tk.Button(newVentana,text="Cargar !",command=subir_productos,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")

	

def nuevaVentana():							#Funcion nuevaVentana ... Nos permitira el registro de nuevos usuarios
	newVentana=tk.Toplevel(ventana)			#Definimos 'newVentana'
	newVentana.title("Registro de Usuario")	#Le damos el titulo 'Registro de Usuario'
	newVentana.geometry("300x290+800+250")	#Tamaño de la ventana
	newVentana['bg']=color					#Definimos newVentana 'bg' con el valor de 'color'
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	#Texto 'Registro'
	#panel_reg=tk.Label(newVentana,image=photo_reg).pack(side="left")	#Mostramos la imagen en la posicion 'left' (Izquierda)

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Nombre:'
	caja3=Entry(newVentana)															#Creamos 'caja3' (Nombre)
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Apellidos'
	caja4=Entry(newVentana)															#Creamos 'caja4' (Apellidos)
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Usuario'
	caja5=Entry(newVentana)															#Creamos 'caja5' (Usuario)
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña'
	caja6=Entry(newVentana,show="*")												#Creamos 'caja6' (Contraseña)
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Repita la Contraseña'
	caja7=Entry(newVentana,show="*")															#Creamos 'caja7' 
	caja7.pack()
	def registro():				#Funcion registro ... Nos permitira escribir los datos a nuestra base de datos
		Nombre=caja3.get()		#Obtenemos el valor de 'caja3'
		Apellido=caja4.get()	#Obtenemos el valor de 'caja4'
		Usr_reg=caja5.get()		#Obtenemos el valor de 'caja5'
		Contra_reg=caja6.get()	#Obtenemos el valor de 'caja6'
		Contra_reg_2=caja7.get() #Obtenemos el valor de 'caja7'
		if(Contra_reg==Contra_reg_2):		#Esta condicion nos permite saber si las contraseñas coinciden
			#El siguiente comando es el encargado de insertar los datos obtenidos en el registro
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			#Confirmamos los datos
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		#Cerramos la ventana de registro
		else:	#Se ejecutara si las contraseñas no coinciden
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje
		#c.close()		#Nos permite cerrar el cursor ...
		#db.close()
	#El siguiente comando (boton) nos permite llamar ala funcion registro
	buttons=tk.Button(newVentana,text="Registrar ¡",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana,text=" ",bg=color,font=("Arial",10)).pack()		#Solo es una linea vacia ... (lo use para separar el boton) 
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		#Boton ==> funcion 'login'
Label(ventana,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana,text="No tienes una cuenta ? : ",bg=color,font=("Arial Black",10)).pack()		#Simple texto
#La siguiente linea (boton) nos llama ala funcion 'nuevaVentana' ==> ( ventana de registro)
boton1=Button(ventana,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventana.mainloop()