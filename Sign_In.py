import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Sign In Page")
root.geometry("300x350")

# Labels and Entries dictionary to store references
labels = [
    "First Name",
    "Last Name",
    "Phone Number",
    "Email Id",
    "User Id",
    "Password",
    "Confirm Password"
]

# Store entry widgets in a dictionary
entries = {}

# Create labels on the left and entry fields on the right
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text, font=("Arial", 10))
    label.grid(row=i, column=0, sticky="e", padx=10, pady=5)  # Align labels to the right

    entry = tk.Entry(root, show="*" if "Password" in label_text else "")
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="we")  # Align entries to the left

    entries[label_text] = entry

# Create_Account button
def Create_Account():
    # Print or process entries here
    for field, entry in entries.items():
        print(f"{field}: {entry.get()}")

Create_Account_button = tk.Button(root, text="Create Account", command=Create_Account)
Create_Account_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Make columns responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# Run the Tkinter event loop
root.mainloop()
