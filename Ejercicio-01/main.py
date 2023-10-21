from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = {
    0: {"id": 0, "name":"John","email": "email", "age": 20},
    1: {"id": 1 , "name":"great","email": "email", "age": 20},
    
}


class User(BaseModel):
  id: int
  name: str
  email: str
  age: int

@app.get("/")
def home():
    return{"message": "Hello World"}

@app.post("/users")
def create_user(user: User):
    database[user.id] = user
    return {"message": "Usuario creado correctamente"}

@app.get("/users")
def get_all_users():
  # Devolvemos la lista de todos los usuarios en la db fake de memoria
    return list(database.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = database.get(user_id)
    if user:
        return user
    return {"error": "Usuario no encontrado"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in database:
        database[user_id] = user
        return {"message": "Usuario actualizado correctamente"}
    return {"error": "Usuario no encontrado"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in database:
        del database[user_id]
        return {"message": "Usuario borrado correctamente"}
    return {"error": "Usuario no encontrado"}
    