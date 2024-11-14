import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Smart Laundry System - Reservation Slot Page")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="Reservation Slot Page", font=("Arial", 16))
title_label.pack(pady=(10, 5))

# Time label
time_label = tk.Label(root, text="Time:")
time_label.pack()

# Start and Stop buttons
def start_machine():
    messagebox.showinfo("Start Machine", "The machine has started.")

def stop_machine():
    messagebox.showinfo("Stop Machine", "The machine has stopped.")

start_button = tk.Button(root, text="Start Machine", command=start_machine)
start_button.pack(pady=(5, 5), side="left", padx=20)

stop_button = tk.Button(root, text="Stop Machine", command=stop_machine)
stop_button.pack(pady=(5, 5), side="right", padx=20)

# Separator
separator_label = tk.Label(root, text="Reservation:")
separator_label.pack(pady=(20, 5))

# Time slot buttons
def reserve_slot(time_slot):
    messagebox.showinfo("Reservation", f"Slot reserved for {time_slot}")

slot1_button = tk.Button(root, text="3:30 - 4:30", command=lambda: reserve_slot("3:30 - 4:30"))
slot1_button.pack(pady=(5, 5), padx=10)

slot2_button = tk.Button(root, text="4:30 - 5:30", command=lambda: reserve_slot("4:30 - 5:30"))
slot2_button.pack(pady=(5, 5), padx=10)

slot3_button = tk.Button(root, text="5:30 - 6:30", command=lambda: reserve_slot("5:30 - 6:30"))
slot3_button.pack(pady=(5, 5), padx=10)

# Run the main loop
root.mainloop()