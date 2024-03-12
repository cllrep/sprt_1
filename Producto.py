class Producto:
    '''
        Clase para representar un producto en el inventario.
    '''
    def __init__(self, id_producto, nombre, descripcion, cantidad, precio):
        '''
            Inicializa el objeto producto
            vars:
                id_producto (str): El id único del producto
                nombre (str): El nombre del producto.
                descripcion (str): La descripción del producto.
                cantidad (int): La cantidad del producto.
                precio (int): El precio del producto.
        '''
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtener_info(self):
        ''' 
            Retorna la información de todos los atributos del producto en formato string.
        '''
        return f"Id: {self.id_producto:<3}| Nombre: {self.nombre:<12}| Descripción: {self.descripcion:<15}| Cantidad: {self.cantidad:<5}| Precio: $ {self.precio:<10}"

    def modificar_info(self, nombre=None, descripcion=None, cantidad=None, precio=None):
        '''
            Modifica la información del producto según los atributos ingresados a la función.
            vars:
                nombre (str, opcional): El nuevo nombre del producto.
                descripcion (str, opcional): La nueva descripción del producto.
                cantidad (int, opcional): La nueva cantidad del producto.
                precio (int, opcional): El nuevo precio del producto.
        '''
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if cantidad:
            self.cantidad = cantidad
        if precio:
            self.precio = precio
        print(f'El producto con id {self.id_producto} ha sido modificado exitosamente...\n')
        return self