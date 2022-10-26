from ast import Num, Str
from calendar import c
from datetime import date
from math import prod
from multiprocessing.dummy import Value

from operator import itemgetter
from tokenize import Number



fecha_anio_actual=date.strftime(date.today(), "%Y")
dia =date.strftime(date.today(), "%Y-%m-%d")



class Producto:
    def __init__(self, nombre, categoria, codigo, precio_base):
        self.nombre = nombre
        self.categoria = categoria
        self.codigo = codigo
        self.precio_base = precio_base
        self.estado = Nueva()

    def precio(self):
        return self.estado.precio(self.precio_base)

    def cambiar_estado(self, estado):
        self.estado = estado

    def retornar_codigo(self):

        return self.codigo

    def consultar_categoria(self,consultar_categoria):
        return consultar_categoria in self.categoria

    def agregar_categoria(self,nueva_categoria):
        self.categoria.append(nueva_categoria)
    
    def agregar_stock(self):
        Producto.stock=0

    def calcular_precio_final(self,es_extranjero):
        if Producto.precio(self) > 70 and es_extranjero:
            
            return Producto.precio(self)
        
        else:
            
            return Producto.precio(self) + Producto.precio(self) * 0.21
        # esta bien aca deberia de calcular
        # en la sucursal deberia pedir el codigo


    #aca van los metodos 
    # y en cada clase de sucursal va a ir su constructor
class Sucursal:
    
        # self.producto=Producto()
    
    def codigos_productos(self):
        codigos=[]
        if len(self.productos)==0:       
            codigos=[]
        else:
            [codigos.append(producto.codigo) for producto in self.productos if  producto.codigo]
        return codigos
    
    def codigos_ordenados_decreciente_de_productos(self):
        return sorted(Sucursal.codigos_productos(self),reverse=True)
    
    def lista_de_codigos_ventas(self):   
        codigos=[]
        if len(self.ventas)>0:
        
            [codigos.append(venta.codigo_producto) for venta in self.ventas]
            
        else:
            
            codigos=[]
        
        return codigos

    def codigo_de_producto_solicitado_en_productos(self,codigo):
        
        return codigo in Sucursal.codigos_productos(self)
    def posicion_de_codigo_ordenado_decre_de_productos(self,codigo_de_producto):

        if Sucursal.codigo_de_producto_solicitado_en_productos(self,codigo_de_producto):
                    return Sucursal.codigos_productos(self).index(codigo_de_producto)
        else:
            raise ValueError("Lo sentimos el producto que desea no se encuetra")

    def buscar_producto(self,codigo_de_producto):
        if Sucursal.codigo_de_producto_solicitado_en_productos(self,codigo_de_producto):
            for producto in self.productos:
                if codigo_de_producto ==producto.codigo:
                            return producto
        else:
            raise ValueError("No se encontro el producto")
    def registrar_producto(self,producto_nuevo):
     
        if len(self.productos)==0:
            producto_nuevo.agregar_stock()
            self.productos.append(producto_nuevo)
        else:
       
            if producto_nuevo.retornar_codigo() in Sucursal.codigos_productos(self):
                raise ValueError("producto registrado")
            else:
                producto_nuevo.agregar_stock()
                self.productos.append(producto_nuevo)
            
    def recargar_stock(self,codigo_de_producto, cantidad):
    
        for producto in self.productos:
        
            if Sucursal.codigo_de_producto_solicitado_en_productos(self,codigo_de_producto):
            
                if producto.codigo == codigo_de_producto:
                
                    producto.stock += cantidad
                
            else:
            
                raise ValueError("No se encuentra el producto")

    def hay_stock(self,codigo_producto):
    
    
        lista_de_codigos=Sucursal.codigos_productos(self)
    
        posicion=Sucursal.posicion_de_codigo_ordenado_decre_de_productos(self,codigo_producto)
    

        if codigo_producto in lista_de_codigos:

            return self.productos[posicion].codigo == codigo_producto and self.productos[posicion].stock > 0
    def mostrar(self):
        for i in self.productos:
            print(f'nombre del producto {i.nombre}, stock = {i.stock},codigo = {i.codigo}')
    
    def calcular_precio_final(self,codigo,es_extranjero):
        producto_encontrado=Sucursal.buscar_producto(self,codigo)
        return producto_encontrado.calcular_precio_final(es_extranjero)

    def contar_categorias(self):
        
        categorias_unicas=[]
        for producto in self.productos:
            [categorias_unicas.append(producto.categoria) for producto in self.productos if producto.categoria not in categorias_unicas]       
        return len(categorias_unicas)

    def realizar_venta(self,producto_vendido,cantidad):
        
        if producto_vendido.codigo>0:
            self.ventas.append( {
                
                        "codigo_producto": producto_vendido.codigo,
                        "cantidad": cantidad,       
                        "fecha": date.strftime(date.today(), "%Y-%m-%d"),
                        "precio": Sucursal.calcular_precio_final(self,producto_vendido.codigo,True) * cantidad
                        
                        })
        
    def realizar_compra(self,codigo_de_producto, cantidad):
        
        # lista_de_codigos = lista_de_codigos_productos()
        
        posicion=Sucursal.posicion_de_codigo_ordenado_decre_de_productos(self,codigo_de_producto)
        
        if self.hay_stock(codigo_de_producto) and cantidad <= self.productos[posicion].stock:
            
                self.productos[posicion].stock-= cantidad
                
                Sucursal.realizar_venta(self,self.productos[posicion],cantidad)
                
        else:
                raise ValueError("No hay stock Disponible, cantidad dispoble de " + str(self.productos[posicion].stock))
        
    def discontinuar_productos(self):
   
        for producto in self.productos :
            
            if  producto.stock == 0:
                
                del self.productos[self.productos.index(producto)]

    def valor_ventas_del_dia(self):
    
        suma_ventas = 0
        
        for venta in self.ventas:
            
            if venta["fecha"]== dia:
                
                suma_ventas += venta["precio"]
                
        return suma_ventas
    def ventas_del_anio(self):
        lista_de_ventas_del_anio = []
        for venta in self.ventas:
            
            if venta.fecha[0:4] == fecha_anio_actual:
                
                lista_de_ventas_del_anio.append(venta)
                
        return lista_de_ventas_del_anio

    def cantidad_de_codigo_con_ventas(self,codigos_ordenados_de_productos_decre):
        
        cantidad_repetida_de_codigo_vendidos={}
        
        for codigo in codigos_ordenados_de_productos_decre:
            
            for venta in self.ventas:
                
                if codigo == venta["codigo_producto"]:
                    
                    if codigo in cantidad_repetida_de_codigo_vendidos:
                        
                        cantidad_repetida_de_codigo_vendidos[codigo] += venta["cantidad"]
                        
                    else:
                        
                        cantidad_repetida_de_codigo_vendidos[codigo] = venta["cantidad"]
                        
        return cantidad_repetida_de_codigo_vendidos

    def productos_mas_vendidos_ordenados(self,codigos_ordenados_por_ventas):
        
        
        nombre_productos = []
        
        for codigo in codigos_ordenados_por_ventas:
            
            for producto in self.productos:
                
                if codigo[0] == producto.codigo:
                    
                    nombre_productos.append(producto.nombre)
                    
        return nombre_productos

    def productos_mas_vendidos(self,hasta=-1):
               
        if len(self.ventas) <= hasta:
            
            raise ValueError("cantidad solicitada excedida")
        
        codigos_ordenados_de_productos_decre=Sucursal.codigos_ordenados_decreciente_de_productos(self)
        
        cantidad_repetida_de_codigo_vendidos= Sucursal.cantidad_de_codigo_con_ventas(self,codigos_ordenados_de_productos_decre)
        
        codigos_ordenados_por_ventas=sorted(cantidad_repetida_de_codigo_vendidos.items(), key=itemgetter(1),reverse=True)
        
        nombre_productos=Sucursal.productos_mas_vendidos_ordenados(self,codigos_ordenados_por_ventas)
        
        if hasta!=-1:
            return nombre_productos[:hasta]
        else:
            return nombre_productos
    def actualizar_precios_por_categoria(self,categoria, porcentaje):
        
    
        if type(porcentaje)==int:
        
            for producto in self.productos:

                precio_de_producto=producto.precio

                if producto.categoria== categoria.lower():
                    
                    producto.precio = 230
                    #precio_de_producto + precio_de_producto * porcentaje/100
        else:

            raise ValueError("Porcentaje no recibe cadena de texto, solo numeros")



class Sucursalvirtual(Sucursal):
    def __init__(self) :
        self.productos = []
        self.ventas = []
        # self.gastos_de_dia 

    def cantidad_de_ventas_del_dia(self):
        self.ventas
        ventas_por_dia= [venta for venta in self.ventas if dia in venta["fecha"]]
        return len(ventas_por_dia)

    def gastos_por_dia(self,gasto_variable):
        if Sucursalvirtual.cantidad_de_ventas_del_dia(self) > 2:
            return Sucursalvirtual.cantidad_de_ventas_del_dia(self) * gasto_variable
        else:
            return gasto_variable

    def ganancias_total_por_dia(self):
        return Sucursalvirtual.valor_ventas_del_dia(self) - Sucursalvirtual.gastos_por_dia(self,500)
    
   

        
    

class Nueva:
    def precio(self, precio_base):
        return precio_base

class Liquidacion:
    def precio(self, precio_base):
        return precio_base / 2

class Promocion:
    def __init__(self, valor_fijo):
        self.valor_fijo = valor_fijo

    def precio(self, precio_base):
        return precio_base - self.valor_fijo

macowin = Sucursalvirtual()
pantalon= Producto("pantalon","ropa",100,5000)
remera = Producto("remera", "ropa", 101, 2000)
short = Producto("short","ropa",102,1000)
macowin.registrar_producto(pantalon)
macowin.registrar_producto(remera)
macowin.registrar_producto(short)
macowin.recargar_stock(100,20)
macowin.recargar_stock(101,20)
macowin.recargar_stock(102,20)
macowin.realizar_compra(100,1)
macowin.realizar_compra(101,1)
macowin.realizar_compra(102,1)
print(macowin.gastos_por_dia(500))    
print(macowin.ganancias_total_por_dia())

# collar=Producto("collar","accesorio",123,1234)
# p=Sucursal()
# p.registrar_producto(collar)
# p.mostrar()
# print("-----------------")
# pantalon=Producto("pantalon","ropa",324,87687)
# p.registrar_producto(pantalon)
# p.mostrar()
# p.productos

# p.hay_stock(324)





        











# def contar_categorias(productos):
    
#     categorias_unicas=[]
#     for producto in productos:
#         if "categoria" not in producto:
#             return 0

#     [categorias_unicas.append(producto["categoria"]) for producto in productos if producto["categoria"] not in categorias_unicas]
    
#     return len(categorias_unicas)

# def realizar_venta(producto_vendido,cantidad):
#     if "codigo"  in producto_vendido and producto_vendido["codigo"]>0:
#         ventas.append( {
            
#                     "codigo_producto": producto_vendido["codigo"],
#                     "cantidad": cantidad,       
#                     "fecha": date.strftime(date.today(), "%Y-%m-%d"),
#                     "precio": producto_vendido["precio"]
                    
#                     })
#     else:
#         raise ValueError("Codigo no encontrado")
    
# def realizar_compra(codigo_producto, cantidad):
    
    
#     global ventas
    
#     lista_de_codigos = lista_de_codigos_productos()
    
#     posicion=posicion_de_codigo_ordenado_decre_de_productos(codigo_producto)
    
#     if hay_stock(codigo_producto) and cantidad <= productos[posicion]["stock"]:
        
#             productos[posicion]["stock"]-= cantidad
            
#             realizar_venta(productos[posicion],cantidad)
            
#     else:
#             raise ValueError("No hay stock Disponible, cantidad dispoble de " + str(productos[posicion]["stock"]) )
        
# def discontinuar_productos():
    
    
#     for producto in productos :
        
#         if  producto["stock"] == 0:
            
#             del productos[productos.index(producto)]

# def valor_ventas_del_dia():
    
#     global ventas 
#     global dia 

#     suma_ventas = 0
    
#     for venta in ventas:
        
#         if venta["fecha"] == dia:
            
#             suma_ventas += venta["precio"]
            
#     return suma_ventas

# def ventas_del_anio():
#     global ventas
#     lista_de_ventas_del_anio = []
    
#     for venta in ventas:
        
#         if venta["fecha"][0:4] == fecha_anio_actual:
            
#             lista_de_ventas_del_anio.append(venta)
            
#     return lista_de_ventas_del_anio

# def cantidad_de_codigo_con_ventas(codigos_ordenados_de_productos_decre):
    
#     cantidad_repetida_de_codigo_vendidos={}
    
#     for codigo in codigos_ordenados_de_productos_decre:
        
#         for venta in ventas:
            
#             if codigo == venta["codigo_producto"]:
                
#                 if codigo in cantidad_repetida_de_codigo_vendidos:
                    
#                      cantidad_repetida_de_codigo_vendidos[codigo] += venta["cantidad"]
                     
#                 else:
                    
#                     cantidad_repetida_de_codigo_vendidos[codigo] = venta["cantidad"]
                    
#     return cantidad_repetida_de_codigo_vendidos

# def productos_mas_vendidos_ordenados(codigos_ordenados_por_ventas):
    
    
#     nombre_productos = []
    
#     for codigo in codigos_ordenados_por_ventas:
        
#         for producto in productos:
            
#             if codigo[0] == producto["codigo"]:
                
#                 nombre_productos.append(producto["nombre"])
                
#     return nombre_productos

# def productos_mas_vendidos(hasta=-1):
    
    
#     global ventas
    
#     if len(ventas) <= hasta:
        
#         raise ValueError("cantidad solicitada excedida")
    
#     codigos_ordenados_de_productos_decre=lista_de_codigos_productos()
    
#     cantidad_repetida_de_codigo_vendidos= cantidad_de_codigo_con_ventas(codigos_ordenados_de_productos_decre)
    
#     codigos_ordenados_por_ventas=sorted(cantidad_repetida_de_codigo_vendidos.items(), key=itemgetter(1),reverse=True)
    
#     nombre_productos=productos_mas_vendidos_ordenados(codigos_ordenados_por_ventas)
    
#     if hasta!=-1:
#         return nombre_productos[:hasta]
#     else:
#         return nombre_productos
    
# def actualizar_precios_por_categoria(categoria, porcentaje):

    
#     if type(porcentaje)==int:
#         for producto in productos:
            
#             if producto["categoria"] == categoria.lower():
                
#                 producto["precio"] += producto["precio"]* porcentaje/100
#     else:

#         raise ValueError("Porcentaje no recibe cadena de texto, solo numeros")

