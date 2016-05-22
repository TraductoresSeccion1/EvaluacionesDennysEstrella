#Desarrolle un programa que permita 
#1. Definir una lista de articulos con su precio
#2. Que un usuario pueda comprar dichos articulos 
#3. Imprimir la factura con el calculo del IVA

# - * - coding: UTF-8 - * -
print("Precios sin IVA: Camisa:100Bs ------ Pantalon: 120Bs ------ Falda 100Bs")
print("Elija el producto deseado: ")
print("Producto\t\t\tCodigo")
print("Camisa\t\t\t\t  1")
print("Pantalon\t\t\t  2")
print("Falda\t\t\t\t  3")



cuenta = []
precios = [100, 120, 100]

comprando = 0
while comprando == 0:

	codigo = input("Introduzca el codigo del articulo: ")
	cantidad = input("Introduzca la cantidad de articulos: ")
	cuenta.append((precios[codigo-1])* cantidad)
	comprando = input("Para agregar otro articulo 0 para salir 1: ")

print("<------------------FACTURA CON IVA----------------------->")
sub_total = 0

for precios in cuenta:
	sub_total = sub_total + precios

print("El sub_total a pagar es de Bs: " + str(sub_total))
iva = sub_total * 12/100
print("El IVA a pagar es de Bs: " + str(iva))
precio_neto = sub_total + iva
print("El precio total a pagar es de Bs: " + str(precio_neto))

