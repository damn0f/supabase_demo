import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContacto(id_contacto)
        return render.actualizar_contacto(contacto)

    def POST(self, id_contacto):
        formulario = web.input()
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']

        model_contactos = ModelContactos()
        datos = model_contactos.actualizarContacto(id_contacto, nombre, email, telefono)
        print(datos)  # depuración

        if datos:
            mensaje = "Contacto actualizado correctamente"
        else:
            mensaje = "No se pudo actualizar el contacto"

        web.header('Content-Type', 'text/html')
        return f"""
        <h1>{mensaje}</h1>
        <input type="button" onclick="location.href='/contactos';" value="Regresar">
        """