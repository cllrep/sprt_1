class Inventario:
    '''
        Clase para representar un inventario para almacenar un conjunto de objetos de clase producto
    '''

    def __init__(self):
        '''
          Inicializa el objeto inventario vacio
        '''
        self.productos = {}

    def agregar_producto(self, producto):
        '''
          Agrega un objeto producto al inventario, si ya existe la id arroja error     
          vars: 
            producto (obj): objeto de la clase Producto
        '''
        if producto.id_producto not in self.productos:
            self.productos[producto.id_producto] = producto
            print("\nProducto agregado al inventario.")
        else:
            print("Error: El producto ya existe en el inventario.")

    def eliminar_producto(self, id_producto):
        '''
          Elimina un objeto producto del inventario según id_producto
          vars: 
            id_producto (int): id única del producto a eliminar
        
        '''
        try:
            del self.productos[id_producto]
            print("\nProducto eliminado del inventario.")
        except KeyError:
            raise KeyError("Error: Producto no encontrado en el inventario.")

    def actualizar_producto(self, id_producto, nombre=None, descripcion=None, cantidad=None, precio=None):
        '''
          Actualiza los datos de un objeto producto, llamando funcion modificar_info de clase Producto
          vars: 
            id_producto (int): id única del producto a actualizar
            nombre, descripcion, cantidad, precio (opcionales): conjunto de datos de producto que pueden ser modificados
        '''
        try:
            producto = self.productos[id_producto]
            producto.modificar_info(nombre, descripcion, cantidad, precio)

        except KeyError:
            raise KeyError("Error: Producto no encontrado en el inventario.")

    def buscar_producto(self, id_producto):
        '''
            Busca y entrega los datos de un objeto producto según Id y llama a funcion obtener_info() de Producto
            vars: 
                id_producto (int): id del producto buscado
        '''
        try: 
            producto_buscado = self.productos[id_producto]
            print(producto_buscado.obtener_info())
            return self.productos[id_producto]

        except KeyError: 
            raise KeyError("Error: Producto no encontrado en el inventario.")
            

    def mostrar_inventario(self):
        '''
           Muestra listado de productos en el inventario, incluido la cantidad y valor total de las existencias

        '''
        if self.productos:
            print("Listado de Inventario:\n")
            total_productos = 0
            total_valor = 0
            for id_producto, producto in self.productos.items():
                print(producto.obtener_info())
                total_productos += producto.cantidad
                total_valor += producto.cantidad * producto.precio

            print(f'\nTotal de productos : {total_productos} \nValorización total inventario: $ {total_valor}')
        else:
            print("El inventario está vacío.")