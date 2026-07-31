from repositories.client_repository import ClientRepository
from services.client_service import ClientService
from ui.app_window import AppWindow


def main():
    # Crear el repositorio
    repository = ClientRepository()

    # Inyectar el repositorio al servicio
    service = ClientService(repository)

    # Inyectar el servicio a la interfaz gráfica
    app_window = AppWindow(service)

    # Iniciar la aplicación
    app_window.mainloop()


if __name__ == "__main__":
    main()