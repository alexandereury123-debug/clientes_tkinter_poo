"""Se encarga de gestionar el almacenamiento de los datos en memoria."""

from models.client import Client


class ClientRepository:
    # Simula mi base de datos
    _clients: list[Client] = [
        Client(1, "Juan Pérez", "809-555-1234"),
        Client(2, "María Rodríguez", "829-555-5678"),
        Client(3, "Carlos Gómez", "849-555-9012"),
    ]

    def __init__(self) -> None:
        pass

    def find_all(self) -> list[Client]:
        """Retorna todos los clientes registrados."""
        return self._clients

    def create_one(self, client: Client):
        """Agrega un nuevo cliente."""
        self._clients.append(client)