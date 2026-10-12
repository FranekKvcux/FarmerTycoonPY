import tkinter as tk

root = tk.Tk()

root.title("FarmerTycoon")
root.geometry("400x600")

class Plot:
	def __init__(self, id, owned, type, state):
		self.id     = id
		self.owned  = owned
		self.type   = type
		self.state  = state
		self.growth = 0
		self.crop   = None
		self.icon   = "\U0001f4e6" if type == "granary" else "\U0001f33e" if type == "field" else "\U0001f6d2" if type == "shop" else "\U0001f512"

p0 = Plot(0, True, "field", "cultivated")
print(p0.icon)

plots = []

root.mainloop()
