from services.client_service import ClientService
import tkinter as tk
from tkinter import ttk, messagebox


class AppWindow(tk.Tk):

    def __init__(self, service: ClientService) -> None:
        super().__init__()

        # Inyección del servicio
        self.service = service

        # Configuración de la ventana
        self.title("Sistema de Gestión de Clientes")
        self.geometry("700x550")
        self.resizable(False, False)

        # Crear interfaz
        self.create_widget()

    def create_widget(self):
        """Inicializa todos los widgets de la aplicación."""

        # =========================================================
        # TÍTULO
        # =========================================================

        titulo = tk.Label(
            self,
            text="Sistema de Gestión de Clientes",
            font=("Arial", 16, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            pady=(20, 15)
        )

        # =========================================================
        # FORMULARIO
        # =========================================================

        formulario = tk.LabelFrame(
            self,
            text="Registro de Cliente",
            padx=10,
            pady=10
        )

        formulario.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=30,
            pady=5,
            sticky="ew"
        )

        # ID
        label_id = tk.Label(
            formulario,
            text="ID:"
        )

        label_id.grid(
            row=0,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.entry_id = tk.Entry(
            formulario,
            width=30
        )

        self.entry_id.grid(
            row=0,
            column=1,
            padx=10,
            pady=8,
            sticky="w"
        )

        # Nombre
        label_name = tk.Label(
            formulario,
            text="Nombre:"
        )

        label_name.grid(
            row=1,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.entry_name = tk.Entry(
            formulario,
            width=30
        )

        self.entry_name.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="w"
        )

        # Teléfono
        label_phone = tk.Label(
            formulario,
            text="Teléfono:"
        )

        label_phone.grid(
            row=2,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.entry_phone = tk.Entry(
            formulario,
            width=30
        )

        self.entry_phone.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="w"
        )

        # Botón
        self.button = tk.Button(
            formulario,
            text="Agregar Cliente",
            command=self.create_new_client,
            width=20
        )

        self.button.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=(10, 5)
        )

        # =========================================================
        # TABLA
        # =========================================================

        tabla_frame = tk.LabelFrame(
            self,
            text="Clientes Registrados",
            padx=10,
            pady=10
        )

        tabla_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=30,
            pady=15,
            sticky="nsew"
        )

        self.tree = ttk.Treeview(
            tabla_frame,
            columns=("id", "name", "phone"),
            show="headings",
            height=10
        )

        # Configuración de columnas
        self.tree.column(
            "id",
            anchor="center",
            width=70
        )

        self.tree.column(
            "name",
            anchor="center",
            width=250
        )

        self.tree.column(
            "phone",
            anchor="center",
            width=180
        )

        # Encabezados
        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "name",
            text="Nombre"
        )

        self.tree.heading(
            "phone",
            text="Teléfono"
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        # Configurar expansión del frame de tabla
        tabla_frame.grid_rowconfigure(
            0,
            weight=1
        )

        tabla_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # Cargar datos
        self.render_data_table()

    def clear_entries(self):
        """Limpia todos los campos del formulario."""

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

        self.entry_id.focus()

    def create_new_client(self):
        """Crea un nuevo cliente utilizando el servicio."""

        id_text = self.entry_id.get()
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()

        # Validar campos vacíos
        if not id_text or not name or not phone:

            messagebox.showwarning(
                "Campos vacíos",
                "Debe completar todos los campos."
            )

            return

        # Validar ID
        try:

            id = int(id_text)

        except ValueError:

            messagebox.showerror(
                "Error",
                "El ID debe ser un número."
            )

            return

        # Crear cliente mediante el servicio
        self.service.create_one(
            id,
            name,
            phone
        )

        # Actualizar tabla
        self.render_data_table()

        # Limpiar formulario
        self.clear_entries()

        messagebox.showinfo(
            "Éxito",
            "Cliente registrado correctamente."
        )

    def render_data_table(self):
        """Carga los clientes en el Treeview."""

        clients = self.service.find_all()

        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar clientes
        for client in clients:

            self.tree.insert(
                "",
                "end",
                values=(
                    client.id,
                    client.name,
                    client.phone
                )
            )