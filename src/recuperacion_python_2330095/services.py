from recuperacion_python_2330095.models import Componente


def validar_componente(componente: Componente) -> bool:
    """Valida que los datos de un componente sean correctos."""
    if not componente.codigo.strip():
        return False

    if not componente.nombre.strip():
        return False

    if not componente.categoria.strip():
        return False

    if componente.precio < 0:
        return False

    return componente.cantidad >= 0


def buscar_componente(inventario: list[Componente], codigo: str):
    """Busca un componente mediante su código."""
    for componente in inventario:
        if componente.codigo == codigo:
            return componente

    return None


def registrar_componente(inventario: list[Componente], componente: Componente) -> bool:
    """Registra un componente si sus datos son válidos y su código no está repetido."""
    if not validar_componente(componente):
        return False

    if buscar_componente(inventario, componente.codigo) is not None:
        return False

    inventario.append(componente)
    return True


def actualizar_componente(
    inventario: list[Componente],
    codigo: str,
    nombre: str,
    categoria: str,
    precio: float,
    cantidad: int,
) -> bool:
    """Actualiza los datos de un componente existente."""
    componente = buscar_componente(inventario, codigo)

    if componente is None:
        return False

    componente_actualizado = Componente(
        codigo=codigo,
        nombre=nombre,
        categoria=categoria,
        precio=precio,
        cantidad=cantidad,
    )

    if not validar_componente(componente_actualizado):
        return False

    componente.nombre = nombre
    componente.categoria = categoria
    componente.precio = precio
    componente.cantidad = cantidad

    return True


def eliminar_componente(inventario: list[Componente], codigo: str) -> bool:
    """Elimina un componente mediante su código."""
    componente = buscar_componente(inventario, codigo)

    if componente is None:
        return False

    inventario.remove(componente)
    return True


def calcular_valor_total(inventario: list[Componente]) -> float:
    """Calcula el valor económico total del inventario."""
    total = 0.0

    for componente in inventario:
        total += componente.precio * componente.cantidad

    return total


def componentes_baja_existencia(
    inventario: list[Componente], limite: int
) -> list[Componente]:
    """Obtiene los componentes cuya cantidad es menor al límite indicado."""
    if limite < 0:
        return []

    componentes = []

    for componente in inventario:
        if componente.cantidad < limite:
            componentes.append(componente)

    return componentes


def componente_mayor_precio(
    inventario: list[Componente],
):
    """Encuentra el componente que tiene el precio más alto."""
    if not inventario:
        return None

    mayor = inventario[0]

    for componente in inventario:
        if componente.precio > mayor.precio:
            mayor = componente

    return mayor
