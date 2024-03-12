from Producto import Producto
from Inventario import Inventario

# Funcion generadora de menu
def menu():
    print('\nSISTEMA DE INVENTARIO')
    print('')
    print('****** Menú Principal ******')
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Mostrar inventario")
    print("6. Salir")

if __name__ == "__main__":
    inventario = Inventario() # Crear instancia de obj inventario

    #Poblar inventario con 3 productos
    producto1 = Producto('1', 'Notebook', 'Modelo XYZ', 100, 500000)
    producto2 = Producto('2', 'Notebook', 'Modelo ZZZ', 50, 600000)
    producto3 = Producto('3', 'Notebook', 'Modelo VVV', 30, 550000)

    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar nuevo producto
            try: 
                id_producto = input("Ingrese el ID del producto1: ")
                nombre = input("Ingrese el nombre del producto: ")
                descripcion = input("Ingrese la descripción del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = int(input("Ingrese el precio del producto: "))
                producto = Producto(id_producto, nombre, descripcion, cantidad, precio)
            except KeyError as e:
                print('Dato ingresado erroneamente, respete formatos')
                print(e)

            try:
                inventario.agregar_producto(producto)
                input("\nPulse para volver al menu... ")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            # Buscar producto en inventario
            id_producto = input("Ingrese el ID del producto a buscar: ")
            try:
                print("Información del producto encontrado:")
                inventario.buscar_producto(id_producto)

                input("\nPulse para volver al menu... ")
            except KeyError as e:
                print(e)
        elif opcion == "3":
            # Modificar producto en inventario
            id_producto = input("Ingrese el ID del producto a modificar: ")
            try:
                nombre = input("Ingrese el nuevo nombre del producto (deje en blanco para no modificar): ")
                descripcion = input("Ingrese la nueva descripción del producto (deje en blanco para no modificar): ")
                cantidad = input("Ingrese la nueva cantidad del producto (deje en blanco para no modificar): ")
                precio = input("Ingrese el nuevo precio del producto (deje en blanco para no modificar): ")
                
                inventario.actualizar_producto(id_producto, nombre, descripcion, cantidad, precio)
                input("\nPulse para volver al menu... ")
            except KeyError as e:
                print(e)
        elif opcion == "4":
            # Eliminar producto en inventario
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            try:
                inventario.eliminar_producto(id_producto)
                input("\nPulse para volver al menu... ")
            except KeyError as e:
                print(e)

        elif opcion == "5":
            # Mostrar listado de inventario
            inventario.mostrar_inventario()
            input("\nPulse para volver al menu... ")

        elif opcion == "6":

            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")