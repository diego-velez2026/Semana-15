# Programa para registrar y consultar contactos

# Diccionario para almacenar los contactos
contactos = {}

while True:
    print("\n--- REGISTRO DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar un contacto
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número telefónico: ")

        contactos[nombre] = telefono
        print("Contacto agregado correctamente.")

    # Mostrar los contactos
    elif opcion == "2":
        if len(contactos) == 0:
            print("No hay contactos registrados.")
        else:
            print("\nContactos registrados:")
            for nombre, telefono in contactos.items():
                print("Nombre:", nombre, "- Teléfono:", telefono)

    # Buscar un contacto
    elif opcion == "3":
        nombre = input("Ingrese el nombre que desea buscar: ")

        if nombre in contactos:
            print("Contacto encontrado.")
            print("Nombre:", nombre)
            print("Teléfono:", contactos[nombre])
        else:
            print("El contacto no existe.")

    # Salir del programa
    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")