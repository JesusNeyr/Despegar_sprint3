from ast import Num, Str
from datetime import date
from math import prod

from operator import itemgetter
from tokenize import Number



fecha_anio_actual=date.strftime(date.today(), "%Y")
dia =date.strftime(date.today(), "%Y-%m-%d")

productos = [

]

ventas = []

class Sucursal:
    def __init__(self) :
        self.productos = []
        self.ventas = []


    def registrar_producto(self,producto_nuevo):
 
        if "codigo" not in producto_nuevo and "stock" in producto_nuevo:
            raise ValueError("no se encotro codigo, no incializar stock ")       
        if len(productos)==0:
            producto_nuevo["stock"]=0
            productos.append(producto_nuevo)
        else:
            for producto in productos:
                    
                if producto_nuevo["codigo"]==producto["codigo"]:
                    raise ValueError("producto registrado")
            producto_nuevo["stock"]=0
            productos.append(producto_nuevo)
            


class Producto(Sucursal):
    def __init__(self, nombre, categoria, codigo, precio_base):
        self.nombre = nombre
        self.categoria = categoria
        self.codigo = codigo
        self.precio_base = precio_base
        self.estado = Nueva()

    def precio(self):
        return self.estado.precio(self.precio_base)

#Liquidacion().precio(5000)

    def cambiar_estado(self, estado):
        self.estado = estado

    def consultar_categoria(self,consultar_categoria):
        return consultar_categoria in self.categoria

    def agregar_categoria(self,nueva_categoria):
        self.categoria.append(nueva_categoria) 



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








        









# def lista_de_codigos_productos():
#     codigos=[]
#     if len(productos)==0:       
#         codigos=[]
#     else:
#         [codigos.append(producto["codigo"]) for producto in productos if  "codigo" in producto]
            
        
#     return sorted(codigos,reverse=True)

# def lista_de_codigos_ventas():   
#     codigos=[]
#     if len(ventas)>0:
        
#         [codigos.append(venta["codigo_producto"]) for venta in ventas]
#     else:
#         codigos=[]
#     return codigos

# def codigo_de_producto_solicitado_en_productos(codigo):
 
    
#     return codigo in lista_de_codigos_productos()

    
# def posicion_de_codigo_ordenado_decre_de_productos(codigo_de_producto):   
#     return lista_de_codigos_productos().index(codigo_de_producto)
    
# def registrar_producto(producto_nuevo):
#     global productos

#     if "codigo" not in producto_nuevo and "stock" in producto_nuevo:
#         raise ValueError("no se encotro codigo, no incializar stock ")       
#     if len(productos)==0:
#         producto_nuevo["stock"]=0
#         productos.append(producto_nuevo)
#     else:
#         for producto in productos:
                
#              if producto_nuevo["codigo"]==producto["codigo"]:
#                  raise ValueError("producto registrado")
#         producto_nuevo["stock"]=0
#         productos.append(producto_nuevo)

# def recargar_stock(codigo_producto, cantidad):
    

#     for producto in productos:
        
#         if codigo_de_producto_solicitado_en_productos(codigo_producto):
            
#             if producto["codigo"] == codigo_producto:
                
#                 producto["stock"] += cantidad
                
#         else:
            
#             raise ValueError("No se encuentra el producto")

# def hay_stock(codigo_producto):
    
    
#     lista_de_codigos=lista_de_codigos_productos()
    
#     posicion=posicion_de_codigo_ordenado_decre_de_productos(codigo_producto)
    

#     if codigo_producto in lista_de_codigos:

#         return productos[posicion]["codigo"]== codigo_producto and productos[posicion]["stock"] > 0

# def calcular_precio_final(un_producto, es_extranjero):
    
#     if un_producto["precio"] > 70 and es_extranjero:
        
#         return un_producto["precio"]
    
#     else:
        
#         return un_producto["precio"] + un_producto["precio"] * 0.21

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

