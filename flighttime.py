import tkinter as tk
from tkinter import ttk

def calculate_flight_time():
    try:
        battery_capacity_ah = float(entry_battery_capacity.get())
        motors_number = int(entry_motors_number.get())
        motor_current = float(entry_motor_current.get())
        
        # Flight time calculation formula
        flight_time = (battery_capacity_ah / (motors_number * motor_current)) * 60 * 0.8
        result.set(f"Flight Time: {flight_time:.2f} mins")
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Drone Flight Time Calculator")
root.geometry("400x300")

# Create input fields
label_battery_capacity = tk.Label(root, text="Battery Capacity (AH):")
label_battery_capacity.grid(row=0, column=0, padx=10, pady=10)
entry_battery_capacity = tk.Entry(root)
entry_battery_capacity.grid(row=0, column=1, padx=10, pady=10)

label_motors_number = tk.Label(root, text="Number of Motors:")
label_motors_number.grid(row=1, column=0, padx=10, pady=10)
entry_motors_number = tk.Entry(root)
entry_motors_number.grid(row=1, column=1, padx=10, pady=10)

label_motor_current = tk.Label(root, text="Motor Current (A):")
label_motor_current.grid(row=2, column=0, padx=10, pady=10)
entry_motor_current = tk.Entry(root)
entry_motor_current.grid(row=2, column=1, padx=10, pady=10)

# Create a button to calculate flight time
button_calculate = tk.Button(root, text="Calculate Flight Time", command=calculate_flight_time)
button_calculate.grid(row=3, columnspan=2, pady=10)

# Create a label to display the result
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result)
label_result.grid(row=4, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
