import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:

    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContacto(id_contacto)
        return render.borrar_contacto(contacto)

    def POST(self, id_contacto):
        model_contactos = ModelContactos()
        datos = model_contactos.borrarContacto(id_contacto)
        print(datos)

        if datos:
            mensaje = "Contacto borrado correctamente"
        else:
            mensaje = "No se pudo borrar el contacto"

        web.header('Content-Type', 'text/html')
        return f"""
        <h1>{mensaje}</h1>
        <input type="button" onclick="location.href='/contactos';" value="Regresar">
        """