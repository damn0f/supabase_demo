import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class InsertarContacto:

    # Renderiza el arhivo insertar_contacto.html
    def GET(self):
        return render.insertar_contacto()
    
    # Recibe los input del formulario y accede a cada uno
    # utilizando el atributo 'name'
    def POST(self):
        # Accede a los datos del formulario 'contactos'
        formulario = web.input()
        # Obtiene el valor del input del nombre
        nombre = formulario['nombre']
        # Obtiene el valor del input del email
        email = formulario['email']
        # Obtiene el valor del input del telefono
        telefono = formulario['telefono']

        # Imprime los datos para verificar que se obtienen los valores de forma correcta.
        # print(f"Nombre: {nombre}")
        # print(f"Email: {email}")
        # print(f"Teléfono: {telefono}")

        model_contactos = ModelContactos()
        datos = model_contactos.insertarContacto(nombre, email, telefono)

        #print (datos)

        web.header('Content-Type', 'text/html')
        html = "<h1>Contacto almacenado correctamente</h1> <a href='/contactos'>Regresar</a>"

        return html