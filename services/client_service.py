"""Contiene la lógica de negocio de mi aplicación."""

from models.client import Client
from repositories.client_repository import ClientRepository


class ClientService:
    def __init__(self, repository: ClientRepository) -> None:
        self.repository = repository

    def find_all(self):
        return self.repository.find_all()

    def create_one(self, id: int, name: str, phone: str):
        client = Client(id, name, phone)
        self.repository.create_one(client)