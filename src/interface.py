import customtkinter as ctk

from src.clicker import AutoClicker


class App:

    def __init__(self):

        self.clicker = AutoClicker()

        self.window = ctk.CTk()
        self.window.title("AutoClicker")
        self.window.geometry("300x200")


        self.title = ctk.CTkLabel(
            self.window,
            text="Auto Clicker"
        )

        self.title.pack(pady=20)


        self.start_button = ctk.CTkButton(
            self.window,
            text="Démarrer",
            command=self.clicker.start
        )

        self.start_button.pack(pady=10)


        self.stop_button = ctk.CTkButton(
            self.window,
            text="Arrêter",
            command=self.clicker.stop
        )

        self.stop_button.pack(pady=10)


    def run(self):
        self.window.mainloop()
