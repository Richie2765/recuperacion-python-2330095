# Inventario de Componentes Electrónicos

## Datos del estudiante

- Nombre completo: Ricardo Aparicio Tovar
- Matrícula: 2330095
- Grupo: IM 8-1
- Número de variante: 01

## Nombre del proyecto

Inventario de Componentes Electrónicos

## Descripción

Este proyecto consiste en un sistema de inventario desarrollado en Python para administrar componentes electrónicos.

El programa permite registrar componentes, consultarlos, actualizarlos y eliminarlos. También realiza cálculos relacionados con el valor del inventario, detecta componentes con baja existencia y encuentra el componente con mayor precio.

La información se mantiene durante la ejecución del programa mediante estructuras de datos de Python.

## Funcionalidades

El sistema permite:

- Registrar componentes electrónicos.
- Mostrar todos los componentes registrados.
- Buscar un componente mediante su código.
- Actualizar la información de un componente.
- Eliminar un componente.
- Evitar códigos duplicados.
- Validar códigos, nombres, categorías, precios y cantidades.
- Calcular el valor total del inventario.
- Mostrar componentes con existencia menor a un límite.
- Encontrar el componente de mayor precio.
- Mostrar un resumen general del inventario.
- Manejar búsquedas sin resultados.
- Manejar entradas incorrectas de precio y cantidad.

## Datos de cada componente

Cada componente contiene los siguientes datos:

- Código.
- Nombre.
- Categoría.
- Precio.
- Cantidad.

## Estructura del proyecto

```text
recuperacion-python-2330095/
│
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
│
├── src/
│   └── recuperacion_python_2330095/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── services.py
│
└── tests/
    ├── __init__.py
    └── test_services.py
```

### Archivos principales

- `main.py`: contiene el menú principal y la interacción con el usuario.
- `models.py`: contiene la clase `Componente`.
- `services.py`: contiene las funciones de registro, búsqueda, actualización, eliminación, validaciones y cálculos.
- `test_services.py`: contiene las pruebas automatizadas realizadas con pytest.

## Requisitos

Para ejecutar el proyecto se necesita:

- Python.
- Git.
- uv.

Las dependencias de desarrollo utilizadas son:

- pytest.
- Ruff.

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd recuperacion-python-2330095
```

## Sincronización

Para crear el ambiente virtual e instalar las dependencias:

```bash
uv sync
```

## Ejecución

Para iniciar el programa:

```bash
uv run python -m recuperacion_python_2330095.main
```

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
uv run pytest
```

## Ruff

Para revisar el código:

```bash
uv run ruff check .
```

Para comprobar el formato:

```bash
uv run ruff format --check .
```

En caso de necesitar aplicar formato automáticamente:

```bash
uv run ruff format .
```

## Pruebas implementadas

Se implementaron 12 pruebas automatizadas con pytest.

Las pruebas verifican:

- Registro correcto de componentes.
- Búsqueda de componentes existentes.
- Cálculo del valor total del inventario.
- Cálculo del valor de un inventario vacío.
- Comportamiento al buscar el componente de mayor precio en un inventario vacío.
- Rechazo de componentes con precio negativo.
- Rechazo de códigos duplicados.
- Búsqueda de un componente inexistente.
- Actualización de componentes.
- Eliminación de componentes.
- Filtrado de componentes con baja existencia.
- Obtención del componente con mayor precio.

## Decisiones de diseño

El proyecto fue dividido en diferentes archivos para separar responsabilidades.

La clase `Componente` se encuentra en `models.py` y representa los datos de cada elemento del inventario.

Las funciones relacionadas con la lógica del sistema se encuentran en `services.py`. Esto permite separar las operaciones del inventario de la interacción con el usuario.

El archivo `main.py` contiene el menú y se encarga de solicitar información al usuario y llamar a las funciones correspondientes.

La información se almacena en una lista de objetos `Componente` durante la ejecución del programa.

## Problemas encontrados

Durante el desarrollo se detectó que Ruff indicaba que el archivo de pruebas no tenía el formato esperado.

El problema se solucionó ejecutando:

```bash
uv run ruff format .
```

Posteriormente se verificó nuevamente el proyecto mediante:

```bash
uv run ruff check .
```

y:

```bash
uv run ruff format --check .
```

Después de aplicar el formato, las pruebas se ejecutaron nuevamente con pytest para comprobar que los cambios de formato no afectaran el funcionamiento del programa.