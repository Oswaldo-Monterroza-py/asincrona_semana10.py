total_compras = 0

while True:
    monto = float(input("Ingrese el monto de la compra (ingrese un número negativo para finalizar): "))
    
    if monto < 0:
        break
    
    if monto > 500 and monto <= 1000:
        monto_descuento = monto * 0.95
        print(f"Se aplicó un descuento del 5%. El monto con descuento es de ${monto_descuento:.2f}")
    elif monto > 1000:
        monto_descuento = monto * 0.90
        print(f"Se aplicó un descuento del 10%. El monto con descuento es de ${monto_descuento:.2f}")
    else:
        monto_descuento = monto
        
    total_compras += monto_descuento
    
print(f"El total de compras del cliente es de ${total_compras:.2f}")











