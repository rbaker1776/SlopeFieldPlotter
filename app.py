import customtkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plotSlopeField(event, bounds=((-3, 3), (-3, 3)), n=60):
	equation = equation_field.get()
	x_coords = np.linspace(bounds[0][0], bounds[0][1], n)
	y_coords = np.linspace(bounds[1][0], bounds[1][1], n)

	ax.clear()
	L = 2.0 / n
	for x in x_coords:
		for y in y_coords:
			m = eval(equation, {'x': x, 'y': y})
			theta = np.arctan(x)
			x0, x1, y0, y1 = x-L*np.cos(theta), x+L*np.cos(theta), y-L*np.sin(theta), y+L*np.sin(theta)
			ax.plot([x0, x1], [y0, y1], color="black", marker='', linewidth=0.5)
	
	canvas.draw()

if __name__ == "__main__":
	tk.set_appearance_mode("dark")
	tk.set_default_color_theme("dark-blue")

	root = tk.CTk()
	root.geometry("600x450")
	root.title("Slope Field Plotter")

	plot_frame = tk.CTkFrame(master=root)
	plot_frame.pack(pady=10, padx=20, fill="both", expand=True)

	fig = Figure(figsize=(5, 3.5), dpi=100)
	ax = fig.add_subplot(111)

	x = np.linspace(0, 10, 100)
	y = np.sin(x)
	ax.plot(x, y)

	canvas = FigureCanvasTkAgg(fig, master=plot_frame)
	canvas.draw()
	canvas.get_tk_widget().pack(fill="both", expand=True)

	input_frame = tk.CTkFrame(master=root)
	input_frame.pack(pady=10, padx=20, fill='x')

	equation_field = tk.CTkEntry(master=input_frame, placeholder_text="dy/dx = ")
	equation_field.pack(pady=12, padx=10, fill='x')
	equation_field.bind("<Return>", plotSlopeField)

	root.mainloop()
