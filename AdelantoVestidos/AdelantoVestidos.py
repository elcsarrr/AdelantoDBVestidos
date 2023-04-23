import mysql.connector
from tkinter import *

# Crear una conexion a la base de datos
conexion = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    database='vestis'
)
# Funcion para agregar un cliente a la base de datos
def agregar_cliente():
    nombre = nombre_entry.get()
    documento = documento_entry.get()
    direccion = direccion_entry.get()
    telefono = telefono_entry.get()

    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO clientes (nombre, documento, direccion, telefono)
        VALUES (%s, %s, %s, %s)
    """, (nombre, documento, direccion, telefono))
    conexion.commit()

    nombre_entry.delete(0, END)
    documento_entry.delete(0, END)
    direccion_entry.delete(0, END)
    telefono_entry.delete(0, END)

# Funcion para agregar un vestido a la base de datos
def agregar_vestido():
    codigo = codigo_entry.get()
    color = color_entry.get()
    tamano = tamano_entry.get()
    precio = precio_entry.get()

    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO vestidos (codigo, color, tamano, precio)
    VALUES (%s, %s, %s, %s)
""", (codigo, color, tamano, precio))
    conexion.commit()

    codigo_entry.delete(0, END)
    color_entry.delete(0, END)
    tamano_entry.delete(0, END)
    precio_entry.delete(0, END)

# Funcion para alquilar un vestido
def alquilar_vestido():
    cliente_id = cliente_id_entry.get()
    vestido_id = vestido_id_entry.get()
    fecha_alquiler = fecha_alquiler_entry.get()
    fecha_devolucion = fecha_devolucion_entry.get()

    cursor = conexion.cursor()
    cursor.execute("SELECT precio FROM vestidos WHERE id = %s", (vestido_id,))
    precio_vestido = cursor.fetchone()[0]

    monto = precio_vestido * 2 # Se cobra el doble del precio del vestido

    cursor.execute("""
        INSERT INTO alquileres (cliente_id, vestido_id, fecha_alquiler, fecha_devolucion, monto)
        VALUES (%s, %s, %s, %s, %s)
    """, (cliente_id, vestido_id, fecha_alquiler, fecha_devolucion, monto))
    conexion.commit()

    cliente_id_entry.delete(0, END)
    vestido_id_entry.delete(0, END)
    fecha_alquiler_entry.delete(0, END)
    fecha_devolucion_entry.delete(0, END)

# Crear la interfaz grafica
root = Tk()


# Crear los campos de entrada de datos para clientes
Label(root, text="Nombre").grid(row=0, column=0)
Label(root, text="Documento").grid(row=1, column=0)
Label(root, text="Direccion").grid(row=2, column=0)
Label(root, text="Telefono").grid(row=3, column=0)

nombre_entry = Entry(root)
documento_entry = Entry(root)
direccion_entry = Entry(root)
telefono_entry = Entry(root)

nombre_entry.grid(row=0, column=1)
documento_entry.grid(row=1, column=1)
direccion_entry.grid(row=2, column=1)
telefono_entry.grid(row=3, column=1)
# Crear el boton para agregar un cliente
Button(root, text="Agregar cliente", command=agregar_cliente).grid(row=4, column=0, columnspan=2)

# Crear los campos de entrada de datos para vestidos
Label(root, text="Codigo").grid(row=5, column=0)
Label(root, text="Color").grid(row=6, column=0)
Label(root, text="Tamanio").grid(row=7, column=0)
Label(root, text="Precio").grid(row=8, column=0)

codigo_entry = Entry(root)
color_entry = Entry(root)
tamano_entry = Entry(root)
precio_entry = Entry(root)

codigo_entry.grid(row=5, column=1)
color_entry.grid(row=6, column=1)
tamano_entry.grid(row=7, column=1)
precio_entry.grid(row=8, column=1)

# Crear el boton para agregar un vestido
Button(root, text="Agregar vestido", command=agregar_vestido).grid(row=9, column=0, columnspan=2)

# Crear los campos de entrada de datos para alquilar un vestido
Label(root, text="ID del cliente").grid(row=10, column=0)
Label(root, text="ID del vestido").grid(row=11, column=0)
Label(root, text="Fecha de alquiler").grid(row=12, column=0)
Label(root, text="Fecha de devolucion").grid(row=13, column=0)

cliente_id_entry = Entry(root)
vestido_id_entry = Entry(root)
# Crear los campos de entrada de datos para alquilar un vestido (continuacion)
fecha_alquiler_entry = Entry(root)
fecha_devolucion_entry = Entry(root)

cliente_id_entry.grid(row=10, column=1)
vestido_id_entry.grid(row=11, column=1)
fecha_alquiler_entry.grid(row=12, column=1)
fecha_devolucion_entry.grid(row=13, column=1)

# Crear el boton para alquilar un vestido
Button(root, text="Alquilar vestido", command=alquilar_vestido).grid(row=14, column=0, columnspan=2)

# Ejecutar la interfaz grafica
root.mainloop()