from fastapi import FastAPI, HTTPException
import mysql.connector
from core.connection import connection
from models.user import Usuario
from models.producto import Producto

app = FastAPI()

# obtener usuarios
@app.get("/usuarios")
async def get_usuarios():
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM usuarios"

    try:
        cursor.execute(query)
        usuarios = cursor.fetchall()
        return usuarios
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al obtener los usuarios")
    finally:
        cursor.close()

# obtener usuario por id
@app.get("/usuarios/{id}")
async def get_usuario(id: int):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM usuarios WHERE id = %s"

    try:
        cursor.execute(query, (id,))
        usuario = cursor.fetchone()
        return usuario
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al obtener el usuario")
    finally:
        cursor.close()

# crear usuario
@app.post("/usuarios")
async def create_usuario(usuario: Usuario):
    cursor = connection.cursor(dictionary=True)

    query = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"

    try:
        cursor.execute(query, (usuario.nombre, usuario.correo, usuario.contrasena))
        connection.commit()
        return {"message": "usuario creado correctamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al crear el usuario")
    finally:
        cursor.close()

# actualizar usuario
@app.put("/usuarios/{id}")
async def update_usuario(id: int, usuario: Usuario):
    cursor = connection.cursor(dictionary=True)

    query = "UPDATE usuarios SET nombre = %s, correo = %s, contrasena = %s WHERE id = %s"

    try:
        cursor.execute(query, (usuario.nombre, usuario.correo, usuario.contrasena, id))
        connection.commit()
        return {"message": "usuario actualizado correctamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al actualizar el usuario")
    finally:
        cursor.close()

# eliminar usuario
@app.delete("/usuarios/{id}")
async def delete_usuario(id: int):
    cursor = connection.cursor(dictionary=True)

    query = "DELETE FROM usuarios WHERE id = %s"

    try:
        cursor.execute(query, (id,))
        connection.commit()
        return {"message": "usuario eliminado correctamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al eliminar el usuario")
    finally:
        cursor.close()

# obtener productos
@app.get("/productos")
async def get_productos():
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM productos"

    try:
        cursor.execute(query)
        productos = cursor.fetchall()
        return productos
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al obtener los productos")
    finally:
        cursor.close()

# obtener producto por id
@app.get("/productos/{id}")
async def get_producto(id: int):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM productos WHERE id = %s"

    try:
        cursor.execute(query, (id,))
        producto = cursor.fetchone()
        return producto
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al obtener el producto")
    finally:
        cursor.close()

# crear producto
@app.post("/productos")
async def create_producto(producto: Producto):
    cursor = connection.cursor(dictionary=True)

    query = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"

    try:
        cursor.execute(query, (producto.nombre, producto.descripcion, producto.precio, producto.stock))
        connection.commit()
        return {"message": "producto creado correctamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al crear el producto")
    finally:
        cursor.close()

# actualizar producto
@app.put("/productos/{id}")
async def update_producto(id: int, producto: Producto):
    cursor = connection.cursor(dictionary=True)

    query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s WHERE id = %s"

    try:
        cursor.execute(query, (producto.nombre, producto.descripcion, producto.precio, producto.stock, id))
        connection.commit()
        return {"message": "producto actualizado correctamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al actualizar el producto")
    finally:
        cursor.close()

# eliminar producto
@app.delete("/productos/{id}")
async def delete_producto(id: int):
    cursor = connection.cursor(dictionary=True)

    query = "DELETE FROM productos WHERE id = %s"

    try:
        cursor.execute(query, (id,))
        connection.commit()
        return {"message": "producto eliminado correctamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="error al eliminar el producto")
    finally:
        cursor.close()

