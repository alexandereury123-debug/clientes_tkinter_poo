"""Esta clase modela los datos de un cliente."""

from dataclasses import dataclass

# Decorador que permite crear automáticamente el constructor
@dataclass
class Client:
    id: int
    name: str
    phone: str