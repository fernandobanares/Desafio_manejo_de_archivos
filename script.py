
from usuario import Usuario
import json
instancias = []

with open("error.log", "a+") as error_log:
    with open("usuarios.txt") as usuarios:
        linea = usuarios.readline()
        while linea:
            try:
                usuario = json.loads(linea)
                instancias.append(
                    Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
            except json.JSONDecodeError as e:
                error_log.write(f"Error de decodificación JSON: {e}\n")
            except Exception as e:
                error_log.write(f"Error inesperado: {e}\n")
            linea = usuarios.readline()

print(f"Cantidad de usuarios: {len(instancias)} : {instancias}")

    