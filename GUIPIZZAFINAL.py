# final project -> GUI APP to pizza ordering
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class PizzaApp:
    def __init__(self, root):
        # Initialize the PizzaApp class
        self.root = root
        self.root.title("Pizza")
        # Create a label widget to display a welcome message
        self.label = Label(root, text="Welcome to Pizza!", font=("Arial", 16))
        self.label.pack(pady=20)
        # Load and resize an image to be displayed
        self.image = Image.open("pic1.png")
        self.image = self.image.resize((200, 150))
        self.photo = ImageTk.PhotoImage(self.image)
        # Create an image label widget to display the image
        self.image_label = Label(root, image=self.photo)
        self.image_label.pack(pady=20)
        # Create a button widget to open the order window
        self.button = Button(root, text="Order Now", command=self.open_order_window)
        self.button.pack(pady=20)
        # Create an exit button widget to close the application
        self.exit_button = Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=20)  

    def open_order_window(self):
        # Hide the root window and open a new order window
        self.root.withdraw()
        self.order_window = Toplevel()
        self.order_window.title("Pizza Order")
        # Create a label widget to prompt the user to enter the pizza type
        self.label = Label(self.order_window, text="Enter your pizza type you want:", font=("Arial", 14))
        self.label.pack(pady=20)
        # Create a label widget to display the "Pizza:" text
        self.pizza_label = Label(self.order_window, text="Pizza:", font=("Arial", 12))
        self.pizza_label.pack()
        # Load and resize an image to be displayed in the order window
        self.image = Image.open("pic3.png")
        self.image = self.image.resize((200, 150))
        self.photo = ImageTk.PhotoImage(self.image)
        # Create an image label widget to display the image in the order window
        self.image_label = Label(self.order_window, image=self.photo)
        self.image_label.pack(pady=20)
        # Create an entry widget for the user to enter the pizza type
        self.pizza_entry = Entry(self.order_window)
        self.pizza_entry.pack(pady=20)

        # Create a label widget to prompt the user to enter the card number
        self.payment_label = Label(self.order_window, text="Enter your card number", font=("Arial", 12))
        self.payment_label.pack()
        # Create an entry widget for the user to enter the card number
        self.payment_entry = Entry(self.order_window)
        self.payment_entry.pack(pady=20)
        
        # Create a button widget to place the order
        self.order_button = Button(self.order_window, text="Ordering", command=self.place_order)
        self.order_button.pack(pady=20)
        
        # Create a button widget to cancel the order
        self.cancel_button = Button(self.order_window, text="Cancel", command=self.cancel_order)
        self.cancel_button.pack(pady=20)

    def place_order(self):
        # Get the pizza type and payment method entered by the user
        pizza = self.pizza_entry.get()
        payment = self.payment_entry.get()
        
        if pizza and payment:
            # Display a payment confirmation messagebox
            confirmation = f"You have successfully paid {payment} for your {pizza} pizza!"
            messagebox.showinfo("Payment Confirmation", confirmation)
            
            # Display an order confirmation messagebox
            order_confirmation = f"You have ordered a {pizza} pizza."
            messagebox.showinfo("Order Confirmation", order_confirmation)
            
            # Destroy the order window and show the root window
            self.order_window.destroy()
            self.root.deiconify()
        else:
            # Display a warning messagebox for invalid input
            messagebox.showwarning("Invalid Input", "Please enter a pizza type and payment method.")
    
    def cancel_order(self):
        # Destroy the order window and show the root window
        self.order_window.destroy()
        self.root.deiconify()

root = Tk()
app = PizzaApp(root)
root.mainloop()