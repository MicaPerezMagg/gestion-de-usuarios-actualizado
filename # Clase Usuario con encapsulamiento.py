# Clase Usuario con encapsulamiento
class Usuario:
    def __init__(self, email, nombre, password, rol):
        self.email = email
        self.nombre = nombre
        self.__password = password  # atributo privado
        self.rol = rol

    def verificar_password(self, ingreso):
        return ingreso == self.__password

    def cambiar_password(self, nueva):
        self.__password = nueva

    def obtener_info(self):
        return f"Email: {self.email}, Nombre: {self.nombre}, Rol: {self.rol}"

# Lista simulando base de datos
usuarios = [
    Usuario("admin@correo.com", "Administrador", "Admin123", "admin"),
    Usuario("usuario@correo.com", "Usuario Normal", "Usuario123", "usuario")
]

def validar_contraseña(contraseña):
    tiene_numero = any(c.isdigit() for c in contraseña)
    return len(contraseña) >= 6 and tiene_numero

def registrar_usuario():
    email = input("Email: ")
    nombre = input("Nombre: ")

    while True:
        password = input("Contraseña (mínimo 6 caracteres y al menos un número): ")
        if validar_contraseña(password):
            break
        else:
            print("Contraseña inválida.")

    while True:
        rol = input("Rol (admin / usuario): ").lower()
        if rol in ["admin", "usuario"]:
            break
        else:
            print("Rol inválido.")

    nuevo = Usuario(email, nombre, password, rol)
    usuarios.append(nuevo)
    print("Usuario registrado.")

def iniciar_sesion():
    email = input("Email: ")
    password = input("Contraseña: ")
    for u in usuarios:
        if u.email == email and u.verificar_password(password):
            print(f"Bienvenido, {u.nombre}.")
            return u
    print("Credenciales incorrectas.")
    return None

def menu_admin(usuario_actual):
    while True:
        print("\nMenú Administrador")
        print("1. Ver todos los usuarios")
        print("2. Cambiar rol de un usuario")
        print("3. Eliminar un usuario")
        print("4. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            for u in usuarios:
                print(u.obtener_info())

        elif opcion == "2":
            email = input("Email del usuario: ")
            for u in usuarios:
                if u.email == email:
                    nuevo_rol = input("Nuevo rol (admin/usuario): ").lower()
                    if nuevo_rol in ["admin", "usuario"]:
                        u.rol = nuevo_rol
                        print("Rol actualizado.")
                    else:
                        print("Rol inválido.")
                    break
            else:
                print("Usuario no encontrado.")

        elif opcion == "3":
            email = input("Email del usuario a eliminar: ")
            for u in usuarios:
                if u.email == email and u != usuario_actual:
                    usuarios.remove(u)
                    print("Usuario eliminado.")
                    break
            else:
                print("No se puede eliminar ese usuario.")

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def menu_usuario(usuario_actual):
    while True:
        print("\nMenú Usuario")
        print("1. Ver mi información")
        print("2. Cambiar mi contraseña")
        print("3. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            print(usuario_actual.obtener_info())

        elif opcion == "2":
            nueva = input("Nueva contraseña: ")
            if validar_contraseña(nueva):
                usuario_actual.cambiar_password(nueva)
                print("Contraseña actualizada.")
            else:
                print("Contraseña inválida.")

        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

def menu_principal():
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuario.rol == "admin":
                    menu_admin(usuario)
                else:
                    menu_usuario(usuario)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

menu_principal()
