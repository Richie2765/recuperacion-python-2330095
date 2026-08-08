from recuperacion_python_2330095.models import Componente
from recuperacion_python_2330095.services import (
    actualizar_componente,
    buscar_componente,
    calcular_valor_total,
    componente_mayor_precio,
    componentes_baja_existencia,
    eliminar_componente,
    registrar_componente,
)


def mostrar_menu():
    print("\n=== INVENTARIO DE COMPONENTES ELECTRÓNICOS ===")
    print("1. Registrar componente")
    print("2. Mostrar todos los componentes")
    print("3. Buscar componente")
    print("4. Actualizar componente")
    print("5. Eliminar componente")
    print("6. Mostrar valor total del inventario")
    print("7. Mostrar componentes con baja existencia")
    print("8. Mostrar componente de mayor precio")
    print("9. Mostrar resumen general")
    print("0. Salir")


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: $"))

            if precio < 0:
                print("El precio no puede ser negativo.")
                continue

            return precio

        except ValueError:
            print("Ingresa un precio válido.")


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))

            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            return cantidad

        except ValueError:
            print("Ingresa una cantidad válida.")


def registrar(inventario):
    print("\n--- Registrar componente ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()

    componente = Componente(
        codigo=codigo,
        nombre=nombre,
        categoria=categoria,
        precio=precio,
        cantidad=cantidad,
    )

    if registrar_componente(inventario, componente):
        print("Componente registrado correctamente.")
    else:
        print("No se pudo registrar. Verifica los datos o el código duplicado.")


def mostrar_todos(inventario):
    print("\n--- Componentes registrados ---")

    if not inventario:
        print("No hay componentes registrados.")
        return

    for componente in inventario:
        print(
            f"Código: {componente.codigo} | "
            f"Nombre: {componente.nombre} | "
            f"Categoría: {componente.categoria} | "
            f"Precio: ${componente.precio:.2f} | "
            f"Cantidad: {componente.cantidad}"
        )


def buscar(inventario):
    print("\n--- Buscar componente ---")

    codigo = input("Código a buscar: ").strip()
    componente = buscar_componente(inventario, codigo)

    if componente is None:
        print("No se encontró ningún componente con ese código.")
        return

    print(f"Nombre: {componente.nombre}")
    print(f"Categoría: {componente.categoria}")
    print(f"Precio: ${componente.precio:.2f}")
    print(f"Cantidad: {componente.cantidad}")


def actualizar(inventario):
    print("\n--- Actualizar componente ---")

    codigo = input("Código del componente: ").strip()

    if buscar_componente(inventario, codigo) is None:
        print("No se encontró el componente.")
        return

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()

    if actualizar_componente(
        inventario,
        codigo,
        nombre,
        categoria,
        precio,
        cantidad,
    ):
        print("Componente actualizado correctamente.")
    else:
        print("No se pudo actualizar el componente.")


def eliminar(inventario):
    print("\n--- Eliminar componente ---")

    codigo = input("Código del componente: ").strip()

    if eliminar_componente(inventario, codigo):
        print("Componente eliminado correctamente.")
    else:
        print("No se encontró el componente.")


def mostrar_valor_total(inventario):
    total = calcular_valor_total(inventario)
    print(f"\nValor total del inventario: ${total:.2f}")


def mostrar_baja_existencia(inventario):
    print("\n--- Componentes con baja existencia ---")

    limite = leer_cantidad()
    componentes = componentes_baja_existencia(inventario, limite)

    if not componentes:
        print("No hay componentes por debajo de ese límite.")
        return

    for componente in componentes:
        print(
            f"{componente.codigo} - {componente.nombre} "
            f"- Cantidad: {componente.cantidad}"
        )


def mostrar_mayor_precio(inventario):
    componente = componente_mayor_precio(inventario)

    if componente is None:
        print("\nNo hay componentes registrados.")
        return

    print("\n--- Componente de mayor precio ---")
    print(f"Código: {componente.codigo}")
    print(f"Nombre: {componente.nombre}")
    print(f"Precio: ${componente.precio:.2f}")


def mostrar_resumen(inventario):
    print("\n--- Resumen general ---")
    print(f"Total de componentes diferentes: {len(inventario)}")

    total_unidades = sum(componente.cantidad for componente in inventario)
    print(f"Total de unidades almacenadas: {total_unidades}")

    valor_total = calcular_valor_total(inventario)
    print(f"Valor total del inventario: ${valor_total:.2f}")

    componente = componente_mayor_precio(inventario)

    if componente is not None:
        print(f"Componente más caro: {componente.nombre} (${componente.precio:.2f})")
    else:
        print("Componente más caro: No disponible")


def main():
    inventario = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar(inventario)

        elif opcion == "2":
            mostrar_todos(inventario)

        elif opcion == "3":
            buscar(inventario)

        elif opcion == "4":
            actualizar(inventario)

        elif opcion == "5":
            eliminar(inventario)

        elif opcion == "6":
            mostrar_valor_total(inventario)

        elif opcion == "7":
            mostrar_baja_existencia(inventario)

        elif opcion == "8":
            mostrar_mayor_precio(inventario)

        elif opcion == "9":
            mostrar_resumen(inventario)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
