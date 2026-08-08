from dataclasses import dataclass


@dataclass
class Componente:
    codigo: str
    nombre: str
    categoria: str
    precio: float
    cantidad: int