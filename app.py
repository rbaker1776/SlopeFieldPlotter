import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("500x350")

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text="Slope Field Plotter")
label.pack(pady=12, padx=10)

entry1 = tk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = tk.CTkEntry(master=frame, placeholder_text="Password", show='*')
entry2.pack(pady=12, padx=10)

root.mainloop()
