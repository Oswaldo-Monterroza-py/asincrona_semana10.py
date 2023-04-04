print(' -----------------------------------------------------------------------------------')
print(' |                       Bienvenido a nuestro programa                             |')
print(' -----------------------------------------------------------------------------------')

# Se solicita crear un programa que permita al usuario procesar los montos de las compras de un cliente (Se desconoce la cantidad de compras que realizará), se contará el ingreso de datos de las compras.
# Si se ingresa un monto negativo, no se debe procesar la operación, si el monto supera los $500, se debe aplicar un 5% de descuento, pero si supera los $1000 se debe aplicar un 10% de descuento.

# Inicializacion de variables
total_compra = 0
x = 1

# Se solicita la cantidad de compras realizadas por el cliente
cantidad= int(input('\nIngrese la cantidad de compras realizadas por el cliente: '))

# En base a la cantidad de compras ingresadas, se ingresaran los montos hasta que se cumpla la condición
while x <= cantidad:
    monto = float(input("\nIngrese el monto de la compra: "))
    
    # Si el monto ingresado es negativo, la transacción no se podrá procesar
    if monto < 0:
        print('\nLa operación no se puede procesar ya que se han ingresado valores negativos')
        break
    
    # Los montos se van sumando en la variable total_compra
    x = x + 1
    total_compra = total_compra + monto
    
    # El total de la compra se muestra en la pantalla
    if total_compra <= 500:
        print(f"\nEl total de compras del cliente es de ${total_compra:.2f}")
    
    # Si el total cumple con algunas de las condiciones establecidas, se le aplica el descuento correspondiente
    elif total_compra > 500 and total_compra <= 1000:
        
        total_descuento = total_compra - (total_compra * 0.05)
        print(f"\nEl total de compras del cliente es de ${total_compra:.2f}")
        print(f"\nSe aplicó un descuento del 5%. El monto con descuento es de ${total_descuento:.2f}")
        
    elif total_compra > 1000:
        
        total_descuento = total_compra - (total_compra * 0.10)
        print(f"\nEl total de compras del cliente es de ${total_compra:.2f}")
        print(f"\nSe aplicó un descuento del 10%. El monto con descuento es de ${total_descuento:.2f}")
        
    else:
        
        print('\nHubo un error')
        
print('\nGracias por su compra')
print('Fin del programa')
