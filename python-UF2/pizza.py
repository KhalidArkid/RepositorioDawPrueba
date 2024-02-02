'''
Imagineu-vos que heu estat contractats per dissenyar el sistema de gestió d'una pizzeria. 
L'objectiu és desenvolupar un conjunt de funcions que permetin gestionar diferents tasques relacionades amb el funcionament de la pizzeria. Això inclou la presa de comandes, la preparació de pizzes, la gestió de l'estoc d'ingredients i el processament dels pagaments.
Recordeu fer servir disseny top down, i mantenir un baix acoblament i una alta cohesió.
'''

'''
1.1 Gestión de Pizzeria
1.2 Recibir pedido
1.3 Preparación Pizza 
1.4 Gestión de stock
1.5 Pagos 
'''

'''
1.1.1 (Recibir que quiere el cliente)
1.1.2 Verificación de stock
1.2.1 Cocina
1.2.2 Verificar calidad
1.3.1 Actualizar stock
1.3.2 Abastecer
1.4.1 Costes
1.4.2 Imprimir factura
'''

def usuario():
    print("Bienvenido a Pizzeria Kaldi")
    pizza = input(("Introduce el nombre de tu pizza: "))
    ingredientes = input("Introduce los ingredientes que quieres (separados por comas): ").split(",")
    return {"pizza": pizza, "ingredientes": ingredientes}

def verificar_stock():
    ...

def cocina():
    ...

def control_calidad():
    ...

def atualizar_stock():
    ...

def abastecer():
    ...

def calculo_costes():
    ...

def imprimir_factura():
    ...

pedido_actual = usuario()
