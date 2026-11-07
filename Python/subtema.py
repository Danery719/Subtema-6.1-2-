import modulo_ventas

def main():
    opcion = 0

    while opcion != 6:
        print("\n=== MINIMARKET - INVENTARIO CON PIPE ===")
        print("1. Registrar producto")
        print("2. Buscar por codigo")
        print("3. Listar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Salir")
        opcion = int(input("Opcion: ").strip())

        if opcion == 1:
            modulo_ventas.registrar_producto()
        elif opcion == 2:
            modulo_ventas.buscar_por_codigo()
        elif opcion == 3:
            modulo_ventas.listar()
        elif opcion == 4:
            modulo_ventas.modificar_producto()
        elif opcion == 5:
            modulo_ventas.eliminar_producto()
        elif opcion == 6:
            print("Saliendo del inventario...")
        else:
            print("Opcion no valida.")


main()