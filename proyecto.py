
import os
programa = True


while programa:
    os.system('cls')
    print("Bienvenido al programa de gestión de proyectos.")
    print("1. Ver tema")
    print("2. Ver problema")
    print("3. Ver solución")
    print("4. Ver descripción de base de datos")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    os.system('cls')

    if opcion == '1':
        print("Mercado IBM/Guayerd GRP3: Una tienda minorista de abarrotes y productos de limpieza en Córdoba, Argentina. " \
        "Ofrece tanto productos de consumo diario (bebidas, alimentos, productos de limpieza) como " \
        "opciones gourmet locales. Vende en mostrador y también con reparto a domicilio en ciudades cercanas como " \
        "Villa María y Alta Gracia")
        input("\nPresione Enter para continuar...")
    elif opcion == '2':
        print("La tienda carece de información analítica estructurada para responder preguntas comerciales básicas: ¿qué productos generan mayor " \
            "volumen de ventas?, ¿quiénes son los clientes que compran con más frecuencia o gastan más? Sin estas respuestas, las decisiones sobre " \
            "promociones, compras y gestión de stock son reactivas y poco focalizadas, lo que provoca oportunidades perdidas de aumentar la recompra, " \
            "optimizar inventario y mejorar la rentabilidad.")
        
        print("\nAdemás, la información disponible está distribuida en varias tablas (clientes, ventas, detalle_ventas, productos) " \
            "y no está integrada ni resumida de forma que permita identificar fácilmente top productos o top clientes. El objetivo es resolver " \
            "esta falta de visibilidad mediante un análisis reproducible que identifique los productos más vendidos y los clientes con mayor " \
            "contribución, para soportar estrategias de promoción y fidelización..")
        input("\nPresione Enter para continuar...")
    elif opcion == '3':
        print("La tienda quiere identificar qué productos son los más vendidos y quiénes son los clientes que más compran, " \
            "para diseñar promociones y descuentos que aumenten la recompra y la fidelización.")
        print("\nPropondremos un script en Python que siga estos pasos de manera sencilla: ")
        print("\n")
        print("1. Leer bases de datos: (Clienets, ventas, productos, detalles_ventas)")
        print("2. Unir la información para relacionar clientes con sus compras y los productos adquiridos.")
        print("3. Contar cuántas veces se vendió cada producto y calcular el total de ingresos de cada cliente.")
        print("4. Generar dos listas: Top productos más vendidos y Top clientes más compradores.")
        print("5. Presentar los resultados en un formato fácil de usar para tomar decisiones comerciales.")
        input("\nPresione Enter para continuar...")
    elif opcion == '4':
        bd_boleano = True
        print("En este apartado puedes seleccionar la base de datos que queires ver su información: ")

        while bd_boleano:
            try:
                opcion_bd = int(input(
                "Seleccione la tabla para mostrar su estructura de columnas:\n"
                "1. clientes.xlsx\n"
                "2. ventas.xlsx\n"
                "3. productos.xlsx\n"
                "4. detalle_ventas.xlsx\n"
                "5. Volver al menú principal\n"
                "Ingrese el número de opción: "
                ))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            os.system('cls')

            if opcion_bd == 1:
                print("Estructura de columnas de clientes.xlsx\n")
                print("{:<15} {:<15} {:<20} {}".format("Columna", "Tipo de dato", "Escala", "Ejemplos"))
                print("-" * 70)
                print("{:<15} {:<15} {:<20} {}".format("id_cliente", "int", "nominal", "1, 2, 3, 4, 5"))
                print("{:<15} {:<15} {:<20} {}".format("nombre_cliente", "str", "nominal", "Mariana Lopez, Nicolas Rojas, Hernan Martinez, Uma Martinez, Agustina Flores"))
                print("{:<15} {:<15} {:<20} {}".format("email", "str", "nominal", "mariana.lopez@mail.com, nicolas.rojas@mail.com, hernan.martinez@mail.com, uma.martinez@mail.com, agustina.flores@mail.com"))
                print("{:<15} {:<15} {:<20} {}".format("ciudad", "str", "nominal", "Carlos Paz, Rio Cuarto, Cordoba, Villa Maria, Alta Gracia"))
                print("{:<15} {:<15} {:<20} {}".format("fecha_alta", "datetime", "razón (temporal)", "2023-01-01T00:00:00.000000000, 2023-01-02T00:00:00.000000000, 2023-01-03T00:00:00.000000000, 2023-01-04T00:00:00.000000000, 2023-01-05T00:00:00.000000000"))
                input("\nPresione Enter para continuar...")
            elif opcion_bd == 2:
                print("Estructura de columnas de ventas.xlsx\n")
                print("{:<15} {:<15} {:<20} {}".format("Columna", "Tipo de dato", "Escala", "Ejemplos"))
                print("-" * 70)
                print("{:<15} {:<15} {:<20} {}".format("id_venta", "int", "nominal", "1, 2, 3, 4, 5"))
                print("{:<15} {:<15} {:<20} {}".format("fecha", "datetime", "razón (temporal)", "2024-06-19T00:00:00.000000000, 2024-03-17T00:00:00.000000000, 2024-01-13T00:00:00.000000000, 2024-02-27T00:00:00.000000000, 2024-06-11T00:00:00.000000000"))
                print("{:<15} {:<15} {:<20} {}".format("id_cliente", "int", "nominal", "62, 49, 20, 36, 56"))
                print("{:<15} {:<15} {:<20} {}".format("nombre_cliente", "str", "nominal", "Guadalupe Romero, Olivia Gomez, Tomas Acosta, Martina Molina, Bruno Diaz"))
                print("{:<15} {:<15} {:<20} {}".format("email", "str", "nominal", "guadalupe.romero@mail.com, olivia.gomez@mail.com, tomas.acosta@mail.com, martina.molina@mail.com, bruno.diaz@mail.com"))
                print("{:<15} {:<15} {:<20} {}".format("medio_pago", "str", "nominal", "tarjeta, qr, transferencia, efectivo"))
                input("\nPresione Enter para continuar...")
            elif opcion_bd == 3:
                print("Estructura de columnas de productos.xlsx\n")
                print("{:<15} {:<15} {:<20} {}".format("Columna", "Tipo de dato", "Escala", "Ejemplos"))
                print("-" * 70)
                print("{:<15} {:<15} {:<20} {}".format("id_producto", "int", "nominal", "1, 2, 3, 4, 5"))
                print("{:<15} {:<15} {:<20} {}".format("nombre_producto", "str", "nominal", "Coca Cola 1.5L, Pepsi 1.5L, Sprite 1.5L, Fanta Naranja 1.5L, Agua Mineral 500ml"))
                print("{:<15} {:<15} {:<20} {}".format("categoria", "str", "nominal", "Alimentos, Limpieza"))
                print("{:<15} {:<15} {:<20} {}".format("precio_unitario", "int", "razón", "2347, 4973, 4964, 2033, 4777"))
                input("\nPresione Enter para continuar...")
            elif opcion_bd == 4:
                print("Estructura de columnas de detalle_ventas.xlsx\n")
                print("{:<15} {:<15} {:<20} {}".format("Columna", "Tipo de dato", "Escala", "Ejemplos"))
                print("-" * 70)
                print("{:<15} {:<15} {:<20} {}".format("id_venta", "int", "nominal", "1, 2, 3, 4, 5"))
                print("{:<15} {:<15} {:<20} {}".format("id_producto", "int", "nominal", "90, 82, 39, 70, 22"))
                print("{:<15} {:<15} {:<20} {}".format("nombre_producto", "str", "nominal", "Toallas Húmedas x50, Aceitunas Negras 200g, Helado Vainilla 1L, Fernet 750ml, Medialunas de Manteca"))
                print("{:<15} {:<15} {:<20} {}".format("cantidad", "int", "razón", "1, 5, 2, 4, 3"))
                print("{:<15} {:<15} {:<20} {}".format("precio_unitario", "int", "razón", "2902, 2394, 469, 4061, 2069"))
                print("{:<15} {:<15} {:<20} {}".format("importe", "int", "razón", "2902, 11970, 2345, 8122, 2069"))
                input("\nPresione Enter para continuar...")
            elif opcion_bd == 5:
                bd_boleano = False
            else:
                print("Opción no válida.")
                input("\nPresione Enter para continuar...")

            os.system('cls')

    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        programa = False
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.\n")
        input("Presione Enter para continuar...")