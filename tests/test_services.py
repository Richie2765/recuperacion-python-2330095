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


def test_registrar_componente():
    inventario = []
    componente = Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5)

    resultado = registrar_componente(inventario, componente)

    assert resultado is True
    assert len(inventario) == 1


def test_buscar_componente_existente():
    componente = Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5)
    inventario = [componente]

    resultado = buscar_componente(inventario, "C001")

    assert resultado is not None
    assert resultado.nombre == "Arduino Uno"


def test_calcular_valor_total():
    inventario = [
        Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5),
        Componente("C002", "ESP32", "Microcontrolador", 180.0, 10),
    ]

    resultado = calcular_valor_total(inventario)

    assert resultado == 3550.0


def test_valor_total_inventario_vacio():
    inventario = []

    resultado = calcular_valor_total(inventario)

    assert resultado == 0.0


def test_componente_mayor_precio_inventario_vacio():
    inventario = []

    resultado = componente_mayor_precio(inventario)

    assert resultado is None


def test_rechazar_precio_negativo():
    inventario = []
    componente = Componente("C001", "Arduino Uno", "Microcontrolador", -350.0, 5)

    resultado = registrar_componente(inventario, componente)

    assert resultado is False
    assert len(inventario) == 0


def test_rechazar_codigo_duplicado():
    inventario = []
    componente1 = Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5)
    componente2 = Componente("C001", "ESP32", "Microcontrolador", 180.0, 10)

    registrar_componente(inventario, componente1)
    resultado = registrar_componente(inventario, componente2)

    assert resultado is False
    assert len(inventario) == 1


def test_buscar_componente_inexistente():
    inventario = [
        Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5)
    ]

    resultado = buscar_componente(inventario, "C999")

    assert resultado is None


def test_actualizar_componente():
    inventario = [
        Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5)
    ]

    resultado = actualizar_componente(
        inventario,
        "C001",
        "Arduino Uno R3",
        "Microcontrolador",
        400.0,
        8,
    )

    assert resultado is True
    assert inventario[0].nombre == "Arduino Uno R3"
    assert inventario[0].precio == 400.0
    assert inventario[0].cantidad == 8


def test_eliminar_componente():
    inventario = [
        Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5)
    ]

    resultado = eliminar_componente(inventario, "C001")

    assert resultado is True
    assert len(inventario) == 0


def test_componentes_baja_existencia():
    inventario = [
        Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 2),
        Componente("C002", "ESP32", "Microcontrolador", 180.0, 10),
    ]

    resultado = componentes_baja_existencia(inventario, 5)

    assert len(resultado) == 1
    assert resultado[0].codigo == "C001"


def test_componente_mayor_precio():
    inventario = [
        Componente("C001", "Arduino Uno", "Microcontrolador", 350.0, 5),
        Componente("C002", "ESP32", "Microcontrolador", 180.0, 10),
    ]

    resultado = componente_mayor_precio(inventario)

    assert resultado is not None
    assert resultado.codigo == "C001"