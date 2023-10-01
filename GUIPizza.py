from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza")

        ## Create the main window elements
        self.label = Label(root, text="Welcome to Pizza!", font=("Arial", 16))
        self.label.pack(pady=20)
        self.image = Image.open("p2.png")
        self.image = self.image.resize((300, 300)) 
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(root, image=self.photo)
        self.image_label.pack(pady=20)
        self.button = Button(root, text="Order Now", command=self.open_order_window)
        self.button.pack(pady=20)
        self.exit_button = Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=20)


    def open_order_window(self):
        self.root.withdraw()

        self.order_window =Toplevel()
        self.order_window.title("Pizza Order")
        
        self.label =Label(self.order_window, text="Select your pizza:", font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.pizza_label = Label(self.order_window, text="Pizza:", font=("Arial", 12))
        self.pizza_label.pack()
        
        self.pizza_entry = Entry(self.order_window)
        self.pizza_entry.pack(pady=20)
        
        self.order_button = Button(self.order_window, text="Place Order", command=self.place_order)
        self.order_button.pack(pady=20)
        
        self.cancel_button = Button(self.order_window, text="Cancel", command=self.cancel_order)
        self.cancel_button.pack(pady=20)

    def place_order(self):
        pizza = self.pizza_entry.get()
        
        if pizza:
            messagebox.showinfo("Order Confirmation", f"You have ordered a {pizza} pizza!")
            self.order_window.destroy()
            self.root.deiconify()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a pizza type.")
    
    def cancel_order(self):
        self.order_window.destroy()
        self.root.deiconify()

root = Tk()

app = PizzaApp(root)

root.mainloop()