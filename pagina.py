from tkinter import *
from tkinter import ttk
import proyect_database

root=Tk()

root.resizable(False, False)
root.geometry("390x480")
root.config(background="#FF4500")
root.title("INGRESO DE EMPLEADOS")


usuario=StringVar()
contraseña=StringVar()
direccion=StringVar()
telefono=StringVar()
rtn=StringVar()
cuenta_bancaria=StringVar()

def registrar():
    # Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    direccion = entry_direccion.get()
    telefono= entry_telefono.get()
    rtn = entry_rtn.get()
    cuenta_bancaria = entry_cuenta.get()
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    proyect_db = proyect_database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    proyect_db.insert_db(usuario, contraseña,direccion, telefono, rtn, cuenta_bancaria)

    
    



label_empleados1=Label(root, text="Registro de Empleados", font=("Calibri","18", "bold"),bg="#FF4500", fg="white", justify=CENTER)
label_empleados1.pack()



label_usuario=Label(root,text="USUARIO: ", font=("Calibri", "14"), bg="#FF4500")
label_usuario.place(x=5,y=50)
entry_usuario=Entry(root, font=("Calibri","14"))
entry_usuario.place(x=90, y=50)


label_contraseña=Label(root,text="CONTRASEÑA: ", font=("Calibri", "14"), bg="#FF4500")
label_contraseña.place(x=5,y=90)
entry_contraseña=Entry(root, font=("Calibri","14"))
entry_contraseña.place(x=120, y=90)

label_direccion=Label(root,text="DIRECCIÓN: ", font=("Calibri", "14"), bg="#FF4500")
label_direccion.place(x=5,y=130)
entry_direccion=Entry(root, font=("Calibri","14"))
entry_direccion.place(x=110, y=130)

label_telefono=Label(root,text="TELEFONO: ", font=("Calibri", "14"), bg="#FF4500")
label_telefono.place(x=5,y=170)
entry_telefono=Entry(root, font=("Calibri","14"))
entry_telefono.place(x=100, y=170)

label_rtn=Label(root, text="RTN: ", bg="#FF4500", font=("Calibri", "14"))
label_rtn.place(x=5, y=210)
entry_rtn=Entry(root, font=("Calibri", "14"))
entry_rtn.place(x=50, y=210)


label_cuenta=Label(root, text="CUENTA: ", bg="#FF4500", font=("Calibri", "14"))
label_cuenta.place(x=5, y=250)
entry_cuenta=Entry(root, font=("Calibri", "14"))
entry_cuenta.place(x=85, y=250)



boton_agregar_info=Button(root,text="REGISTRAR EMPLEADO", font=("Calibri", "14"), bg="SandyBrown", background="#FE9520",command=registrar)
boton_agregar_info.place(x=100,y=320)



root.mainloop()
