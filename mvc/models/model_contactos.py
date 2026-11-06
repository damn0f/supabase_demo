import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )         
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        # SELECT * FROM contactos;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto:int):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
        return response.data

    def insertarContacto(self, nombre:str, email:str, telefono:str):
        data = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").insert(data).execute()
        return response.data

    def borrarContacto(self, id_contacto:int):
        response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
        return response.data

    def actualizarContacto(self, id_contacto:int, nombre, email, telefono):
        valores_nuevos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").update(valores_nuevos).eq("id_contacto", id_contacto).execute()
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(30))
    # print(model_contactos.insertarContacto("hola", "hola@gmail.com", "2222"))
    # print(model_contactos.borrarContacto(8))
    # print(model_contactos.actualizarContacto(1, "Dejah modificada", "dejah11@gmail.com", "444444"))