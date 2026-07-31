from services.client_service import ClientService
import tkinter as tk
from tkinter import ttk, messagebox


class AppWindow(tk.Tk):

    def __init__(self, service: ClientService) -> None:
        super().__init__()

        self.service = service

        self.title("Sistema de Gestión de Clientes")
        self.geometry("650x500")

        self.create_widget()

    def create_widget(self):
        """Inicializa todos los widgets"""

        titulo = tk.Label(
            self,
            text="Sistema de Gestión de Clientes",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        self.render_entries()

        self.button = tk.Button(
            self,
            text="Agregar Cliente",
            command=self.create_new_client
        )
        self.button.pack(pady=10)

        self.create_data_table()
        self.render_data_table()

    def render_entries(self):

        label_id = tk.Label(self, text="Ingresa el ID")
        label_id.pack(pady=(5, 0))

        self.entry_id = tk.Entry(self)
        self.entry_id.pack(pady=(0, 8))

        label_name = tk.Label(self, text="Ingresa el nombre")
        label_name.pack(pady=(5, 0))

        self.entry_name = tk.Entry(self)
        self.entry_name.pack(pady=(0, 8))

        label_phone = tk.Label(self, text="Ingresa el teléfono")
        label_phone.pack(pady=(5, 0))

        self.entry_phone = tk.Entry(self)
        self.entry_phone.pack(pady=(0, 8))

    def clear_entries(self):

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

        self.entry_id.focus()

    def create_new_client(self):

        id_text = self.entry_id.get()
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()

        if not id_text or not name or not phone:

            messagebox.showwarning(
                "Campos vacíos",
                "Debe completar todos los campos."
            )
            return

        try:
            id = int(id_text)

        except ValueError:

            messagebox.showerror(
                "Error",
                "El ID debe ser un número."
            )
            return

        self.service.create_one(id, name, phone)

        self.render_data_table()

        self.clear_entries()

        messagebox.showinfo(
            "Éxito",
            "Cliente registrado correctamente."
        )

    def create_data_table(self):

        self.tree = ttk.Treeview(
            self,
            columns=("id", "name", "phone"),
            show="headings"
        )

        self.tree.column("id", anchor="center", width=70)
        self.tree.column("name", anchor="center", width=250)
        self.tree.column("phone", anchor="center", width=180)

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Nombre")
        self.tree.heading("phone", text="Teléfono")

        self.tree.pack(pady=20)

    def render_data_table(self):

        clients = self.service.find_all()

        for item in self.tree.get_children():
            self.tree.delete(item)

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