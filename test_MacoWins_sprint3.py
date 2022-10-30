
from MacoWins import *

import pytest

una_sucursal_fisica=Sucursalfisica()
una_sucursal_virtual=Sucursalvirtual()
un_producto=Producto("remera","ropa",1,1200)

def reiniciar_productos_y_listas_de_sucursal(sucursal):
    sucursal.productos.clear()
    sucursal.ventas.clear()


def test_de_producto_obtener_precio():

    assert un_producto.retornar_precio()==1200

def test_de_producto_obtener_precio_estado_nueva():

    assert un_producto.precio()==1200

def test_de_producto_obtener_precio_estado_promocion():

    un_producto.cambiar_estado(Promocion(30))
    assert un_producto.precio()==1170

def test_de_producto_obtener_precio_estado_liquidacion():
    
    un_producto.cambiar_estado(Liquidacion())
    assert un_producto.precio()==600

def test_de_producto_retornar_codigo():
    
    assert un_producto.codigo==1

def test_de_producto_calcular_precio_final_con_parametro_True():

    un_producto=Producto("remera","ropa",1,1200)
    
    assert un_producto.calcular_precio_final(True) ==1200

def test_de_producto_calcular_precio_final_con_parametro_False():
    
    un_producto=Producto("remera","ropa",1,1200)
    assert un_producto.calcular_precio_final(False) ==1452

def tes_actualizar_precio_por_porcentaje():
    
    assert un_producto.actualizar_precio_por_porcentaje(50)==1800

def test_consultar_categoria_en_producto():
    
    assert un_producto.consultar_categoria("ropa")==True

def test_agregar_categoria_en_producto():

    un_producto.agregar_categoria("verano")

    assert "verano" in un_producto.categoria 

def test_codigos_de_productos_en_sucursal_fisica():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    otro_producto=Producto("remera x","ropa",3,1200)
    otro_producto_mas=Producto("remera xs","ropa",4,1200)
    una_sucursal_fisica.registrar_producto(un_producto)
    una_sucursal_fisica.registrar_producto(otro_producto)
    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    assert una_sucursal_fisica.codigos_productos()==[1,3,4]

def test_codigos_en_string_de_productos_en_sucursal_fisica():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    un_producto_codigo_string=Producto("remera","ropa","12",1200)

    otro_producto=Producto("remera x","ropa","3",1200)
    otro_producto_mas=Producto("remera xs","ropa","4",1200)
    una_sucursal_fisica.registrar_producto(un_producto_codigo_string)
    una_sucursal_fisica.registrar_producto(otro_producto)
    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    assert una_sucursal_fisica.codigos_productos()==[]

def test_codigos_negativos_en_de_productos_en_sucursal_fisica():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    un_producto_codigo_string=Producto("remera","ropa",-2,1200)

    otro_producto=Producto("remera x","ropa",-3,1200)
    otro_producto_mas=Producto("remera xs","ropa",-4,1200)
    una_sucursal_fisica.registrar_producto(un_producto_codigo_string)
    una_sucursal_fisica.registrar_producto(otro_producto)
    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    assert una_sucursal_fisica.codigos_productos()==[]

def test_codigos_de_productos_en_sucursal_fisica_sin_productos():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    assert una_sucursal_fisica.codigos_productos()==[]

def test_codigos_de_productos__ordenados_de_forma_decreciente_en_sucursal_fisica():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    otro_producto=Producto("remera x","ropa",3,1200)
    otro_producto_mas=Producto("remera xs","ropa",4,1200)
    una_sucursal_fisica.registrar_producto(un_producto)
    una_sucursal_fisica.registrar_producto(otro_producto)
    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    assert una_sucursal_fisica.codigos_ordenados_decreciente_de_productos()==[4,3,1]

def test_codigo_de_producto_solicitado_en_productos_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    assert una_sucursal_fisica.codigo_de_producto_solicitado_en_productos(1)==True

def test_codigo_de_producto_no_existente_solicitado_en_productos_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    assert una_sucursal_fisica.codigo_de_producto_solicitado_en_productos(9)==False

def test_busqueda_de_la_posicion_de_un_codigo_en_la_lista__productos():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    otro_producto=Producto("remera x","ropa",3,1200)
    otro_producto_mas=Producto("remera xs","ropa",4,1200)
    una_sucursal_fisica.registrar_producto(un_producto)
    una_sucursal_fisica.registrar_producto(otro_producto)
    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    assert una_sucursal_fisica.posicion_de_codigo_en_productos(1)==0

def test_busqueda_de_la_posicion_de_un_codigo_no_existente_en_la_lista_en__productos():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    with pytest.raises(ValueError) as exception_info:
        una_sucursal_fisica.posicion_de_codigo_en_productos(20)
    assert str(exception_info.value)=='Lo sentimos el producto consultado, no existe'

def test_agregar_producto_en_sucursal_fisica():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    una_sucursal_fisica.registrar_producto(un_producto)
    return len(una_sucursal_fisica.productos)==1

def test_agregra_dos_productos_con_igual_codigo():
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","ropa",1,200)

    otro_producto=Producto("remera x","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)
    
    with pytest.raises(ValueError) as exception_info:
        
        una_sucursal_fisica.registrar_producto(otro_producto)
    
    assert  str(exception_info.value)=='producto registrado'
    
def test_recargar_stock_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,30)

    assert un_producto.stock==30

def test_recargar_stock_ingresando_string_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    un_producto=Producto("un_producto","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)


    una_sucursal_fisica.recargar_stock(1,"330")

    assert un_producto.stock==330

def test_recargar_stock_ingresando_codigo_inexistente_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    
    una_sucursal_fisica.registrar_producto(un_producto)

    with pytest.raises(ValueError) as exception_info:

        una_sucursal_fisica.recargar_stock(6,"330")

    assert str(exception_info.value)=='No se encuentra el producto'

def test_consultar_stock_de_un_producto_registrado():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("remera","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)

    assert una_sucursal_fisica.hay_stock(1)==False

def test_consultar_stock_de_un_producto_con_stock__registrado():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)
    una_sucursal_fisica.recargar_stock(1,20)

    assert una_sucursal_fisica.hay_stock(1)==True

def test_calcular_precio_final_es_extranjero_True():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("remera","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)

    assert una_sucursal_fisica.calcular_precio_final(1,True)==1200

def test_calcular_precio_final_es_extranjero_False():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("remera","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)

    assert una_sucursal_fisica.calcular_precio_final(1,False)==1452

def test_calcular_precio_final_es_extranjero_False_con_codigo_inexistente():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","remera" ,1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)

    with pytest.raises(ValueError) as exception_info:

        una_sucursal_fisica.calcular_precio_final(5,False)

    assert str(exception_info.value)=="No se encontro el producto"

def test_contar_categorias_de_productos_registrados_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("otro_producto","producto_otro",3,123)

    otro_producto_mas=Producto("otro_producto_mas","producto_otro_mas",2,123)
    
    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    assert una_sucursal_fisica.contar_categorias()==3
    
def test_contar_categorias_de_productos_registrados_con_mas_de_una_categoria_por_producto_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","ropa",1,1200)
    otro_producto=Producto("otro_producto","producto_otro",3,123)

    otro_producto_mas=Producto("otro_producto_mas","producto_otro_mas",2,123)
    
    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.agregar_categoria(3,"otra_categoria_mas")

    assert una_sucursal_fisica.contar_categorias()==4

def test_contar_categorias_de_productos_registrados_con_igual_categoria_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)
    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("otro_producto","ropa",3,123)

    otro_producto_mas=Producto("otro_producto_mas","ropa",2,123)
    
    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.agregar_categoria(3,"ropa")

    assert una_sucursal_fisica.contar_categorias()==1
    
def test_realizar_venta_de_un_producto_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,30)

    una_sucursal_fisica.realizar_venta(un_producto,20,True)
    
    assert len(una_sucursal_fisica.ventas)==1

def test_realizar_venta_de_un_producto_sin_stock_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","ropa",1,1200)

    una_sucursal_fisica.registrar_producto(un_producto)
    
    una_sucursal_fisica.realizar_venta(un_producto,10,True) 

    assert len(una_sucursal_fisica.ventas)==0

def test_realizar_venta_de_un_producto_sin_stock_y_codigo_negativo_en_sucursal_fisica():

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    un_producto=Producto("un_producto","ropa",-112,20)

    una_sucursal_fisica.registrar_producto(un_producto)
    
    una_sucursal_fisica.realizar_venta(un_producto,10,True) 

    assert len(una_sucursal_fisica.ventas)==0

def test_realizar_compra_con_producto_sin_stock():

    un_producto=Producto("un_producto","ropa",1,1200)

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)
    
    with pytest.raises(ValueError) as exception_info:

        una_sucursal_fisica.realizar_compra(1,20,True)

    assert str(exception_info.value)==f'No hay stock Disponible, cantidad dispoble de {un_producto.stock}'

def test_realizar_compra_de_un_producto_con_stock_disponible_sucursal_fisica():

    un_producto=Producto("un_producto","ropa",1,1200)

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,40)

    una_sucursal_fisica.realizar_compra(1,20,True)

    assert len(una_sucursal_fisica.productos)==1

def test_discontinuar_productos_con_stock_en_cero():

    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("un_producto","ropa",2,1200)

    otro_producto_mas=Producto("un_producto","ropa",3,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.discontinuar_productos()

    assert len(una_sucursal_fisica.productos)==0

def test_discontinuar_productos_con_un_producto_con_stock_positivo():

    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("un_producto","ropa",2,1200)

    otro_producto_mas=Producto("un_producto","ropa",3,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.recargar_stock(1,40)

    una_sucursal_fisica.discontinuar_productos()

    assert len(una_sucursal_fisica.productos)==1

def test_valor_de_las_ventas_del_dia():

    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("un_producto","ropa",2,1200)

    otro_producto_mas=Producto("un_producto","ropa",3,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.recargar_stock(1,50)

    una_sucursal_fisica.recargar_stock(2,30)

    una_sucursal_fisica.recargar_stock(3,60)

    una_sucursal_fisica.realizar_compra(1,1,True)

    una_sucursal_fisica.realizar_compra(2,1,True)

    una_sucursal_fisica.realizar_compra(3,1,False)

    assert una_sucursal_fisica.valor_ventas_del_dia()==3852

def test_valor_de_las_ventas_del_dia_sin_ventas():

    un_producto=Producto("un_producto","ropa",1,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,50)

    assert una_sucursal_fisica.valor_ventas_del_dia()==0

def test_valor_de_las_ventas_del_dia_cantidad_solicitada_excedida_del_stock_de_productos_ventas():

    un_producto=Producto("un_producto","ropa",1,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,20)

    with pytest.raises(ValueError) as exception_info:

         una_sucursal_fisica.realizar_compra(1,900,True)
    
    assert str(exception_info.value)==f'No hay stock Disponible, cantidad dispoble de {un_producto.retornar_stock()}'

def test_lista_de_ventas_del_año():

    un_producto=Producto("un_producto","ropa",1,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,20)

    una_sucursal_fisica.realizar_compra(1,10,True)


    assert una_sucursal_fisica.ventas_del_anio()==[una_sucursal_fisica.ventas[0]]

def test_lista_de_ventas_del_año_sin_ventas():

    un_producto=Producto("un_producto","ropa",1,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    assert una_sucursal_fisica.ventas_del_anio()==[]

def test_cantidad_de_codigos_con_las_ventas_realizadas():

    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("un_producto","ropa",2,1200)

    otro_producto_mas=Producto("un_producto","ropa",3,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.recargar_stock(1,50)

    una_sucursal_fisica.recargar_stock(2,30)

    una_sucursal_fisica.recargar_stock(3,60)

    una_sucursal_fisica.realizar_compra(1,12,True)

    una_sucursal_fisica.realizar_compra(2,30,True)

    una_sucursal_fisica.realizar_compra(3,25,False)

    assert una_sucursal_fisica.cantidad_de_codigo_con_ventas([3,2,1])=={3:25,2:30,1:12}

def test_cantidad_de_codigos_con_las_ventas_realizadas():

    un_producto=Producto("un_producto","ropa",1,1200)

    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.recargar_stock(1,50)

    assert una_sucursal_fisica.cantidad_de_codigo_con_ventas([])=={}

def test_codigos_ordenados_de_las_ventas_realizadas():

    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("otro_producto","ropa",2,1200)

    otro_producto_mas=Producto("otro_producto_mas","ropa",3,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.recargar_stock(1,50)

    una_sucursal_fisica.recargar_stock(2,30)

    una_sucursal_fisica.recargar_stock(3,60)

    una_sucursal_fisica.realizar_compra(1,12,True)

    una_sucursal_fisica.realizar_compra(2,30,True)

    una_sucursal_fisica.realizar_compra(3,25,False)

    assert una_sucursal_fisica.codigos_ordenados_de_las_ventas()==[(2,30),(3,25),(1,12)]

def test_productos_mas_vendidos_con_ventas_realizadas():
    
    un_producto=Producto("un_producto","ropa",1,1200)

    otro_producto=Producto("otro_producto","ropa",2,1200)

    otro_producto_mas=Producto("otro_producto_mas","ropa",3,1200)
    
    reiniciar_productos_y_listas_de_sucursal(una_sucursal_fisica)

    una_sucursal_fisica.registrar_producto(un_producto)

    una_sucursal_fisica.registrar_producto(otro_producto)

    una_sucursal_fisica.registrar_producto(otro_producto_mas)

    una_sucursal_fisica.recargar_stock(1,50)

    una_sucursal_fisica.recargar_stock(2,30)

    una_sucursal_fisica.recargar_stock(3,60)

    una_sucursal_fisica.realizar_compra(1,12,True)

    una_sucursal_fisica.realizar_compra(2,30,True)

    una_sucursal_fisica.realizar_compra(3,25,False)

    assert una_sucursal_fisica.productos_mas_vendidos_ordenados(-1)==["otro_producto","otro_producto_mas","un_produucto"]