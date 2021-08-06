from tkinter import *
from tkinter import ttk 

import mysql.connector

connection =mysql.connector.connect(host="localhost", 
                                user="root", 
                                passwd="", 
                                database="db_lo_de_mary")

cursor = connection.cursor()
cursor.execute("SELECT USUARIO, CONTRASEÑA, DIRECCION, TELEFONO, RTN, CUENTA_BANCARIA FROM TBL_EMPLEADOS")


window = Tk()
window.title('Mostrar Registros')
my_table = ttk.Treeview(window)


registro=0
for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
    usuario = fila[0]  
    contraseña = fila[1]
    direccion = fila[2] 
    telefono= fila[3] 
    rtn = fila[4] 
    cuenta_bancaria = fila[5] 
    my_table.insert(parent="", index="end", uid=registro, text=str(registro),
        values=(usuario, contraseña, direccion, telefono, rtn,cuenta_bancaria))
connection.close() 




# Define Our Columns 
my_table['columns'] = ('USUARIO', 'CONTRASEÑA', 'DIRECCION','TELELFONO','RTN','CUENTA_BANCARIA')

# Formate Our Columns
my_table.column('#0', width=120, minwidth=50)
my_table.column('USUARIO', anchor=W, width=120)
my_table.column('CONTRASEÑA', anchor=W, width=120)
my_table.column('DIRECCION', anchor=W, width=120)
my_table.column('TELEFONO', anchor=W, width=120)
my_table.column('RTN', anchor=W, width=120)
my_table.column('CUENTA_BANCARIA', anchor=W, width=120)

# Create Headings
my_table.heading('#0', text='ID_EMPLEADO', anchor=W)
my_table.heading('USUARIO', text='USUARIO', anchor=W)
my_table.heading('CONTRASEÑA', text='CONTRASEÑA', anchor=W)
my_table.heading('DIRECCION', text='DIRECCION', anchor=W)
my_table.heading('TELEFONO', text='TELEFONO', anchor=W)
my_table.heading('RTN', text='RTN', anchor=W)
my_table.heading('CUENTA_BANCARIA', text='CUENTA_BANCARIA', anchor=W)



# Pack to the screen
my_table.pack(pady=20, padx=20)

window.mainloop()