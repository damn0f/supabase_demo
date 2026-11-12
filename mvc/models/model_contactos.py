import os
from supabase import create_client, Client
from dotenv import load_dotenv

import logging


load_dotenv()

logger = logging.getLogger(__name__)

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )         
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        # SELECT * FROM contactos;
        try: 
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 101: {str(error)}")
            print(f"ERROR 101: {error.args[0]}")

    def buscarContacto(self, id_contacto:int):

        try: 
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 102: {str(error)}")
            print(f"ERROR 102: {error.args[0]}")


    def insertarContacto(self, nombre:str, email:str, telefono:str):
        try:
            data = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            response = self.supabase.table("contactos").insert(data).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 103: {str(error)}")
            print(f"ERROR 103: {error.args[0]}")

    def borrarContacto(self, id_contacto:int):
        try:
            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 104: {str(error)}")
            print(f"ERROR 104: {error.args[0]}")

    def actualizarContacto(self, id_contacto:int, nombre, email, telefono):
        try:

            valores_nuevos = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            response = self.supabase.table("contactos").update(valores_nuevos).eq("id_contacto", id_contacto).execute()
            return response.data

        except Exception as error:
            logger.error(f"ERROR 105: {str(error)}")
            print(f"ERROR 105: {error.args[0]}")

if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(30))
    # print(model_contactos.insertarContacto("hola", "hola@gmail.com", "2222"))
    # print(model_contactos.borrarContacto(8))
    # print(model_contactos.actualizarContacto(1, "Dejah modificada", "dejah11@gmail.com", "444444"))