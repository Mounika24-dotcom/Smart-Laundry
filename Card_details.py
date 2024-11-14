import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Credit Card Information")

# Define Labels
tk.Label(root, text="Card Holder Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Card Number").grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="CVV").grid(row=2, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text="Expiry Date").grid(row=3, column=0, padx=10, pady=5, sticky='w')

# Define Entry fields for each label
tk.Entry(root).grid(row=0, column=1, padx=10, pady=5)
tk.Entry(root).grid(row=1, column=1, padx=10, pady=5)
tk.Entry(root).grid(row=2, column=1, padx=10, pady=5)
tk.Entry(root).grid(row=3, column=1, padx=10, pady=5)

# Define the Submit Button
tk.Button(root, text="Submit").grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
