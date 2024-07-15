import tkinter as tk
from tkinter import ttk

def calculate_thrust_and_current():
    try:
        # Get input values
        prop_size = prop_entry.get()
        battery_cells = int(battery_slider.get())
        kv_rating = float(kv_entry.get())

        # Validate propeller size format
        if 'x' not in prop_size:
            result_label.config(text="Please enter propeller size in format DxP (e.g., 5045).")
            return

        diameter_str, pitch_str = prop_size.split('x')

        # Ensure diameter and pitch are valid numbers
        if not (diameter_str.isdigit() and pitch_str.isdigit()):
            result_label.config(text="Please enter valid numeric values for propeller size.")
            return

        diameter, pitch = float(diameter_str), float(pitch_str)

        # Calculate battery voltage
        voltage = battery_cells * 4.1  # Assuming 4.1V per LiPo cell

        # Calculate RPM
        rpm = kv_rating * voltage

        # Estimate thrust in grams (g)
        thrust = (diameter**4 * pitch) / 1000000 * rpm**2 * 0.000000011 * 1000

        # Estimate current draw in amps (A)
        current_draw = (thrust / 1000) * (kv_rating / 1000) * battery_cells * 10

        # Calculate recommended ESC rating (30% above current draw)
        esc_rating = current_draw * 1.3

        # Explanation of calculations
        explanation = (f"Calculations:\n"
                       f"1. Battery Voltage = Battery Cells * 4.1V\n"
                       f"2. RPM = KV Rating * Voltage\n"
                       f"3. Thrust (g) = (Diameter^4 * Pitch) / 1000000 * RPM^2 * 0.000000011 * 1000\n"
                       f"4. Current Draw (A) = (Thrust / 1000) * (KV Rating / 1000) * Battery Cells * 10\n"
                       f"5. Recommended ESC Rating (A) = Current Draw * 1.3")

        # Update result label
        result_label.config(text=f"Estimated Thrust: {thrust:.2f} g\n"
                                 f"Estimated Current Draw: {current_draw:.2f} A\n"
                                 f"Recommended ESC Rating: {esc_rating:.2f} A\n\n"
                                 f"{explanation}")
    except ValueError:
        result_label.config(text="Please enter valid values.")

def update_slider_label(val):
    slider_label.config(text=f"Battery Cells: {int(float(val))}")

# Create main window
root = tk.Tk()
root.title("Drone Thrust and Current Calculator")
root.geometry("800x600")
root.configure(bg="#333333")  # Dark theme

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#333333")  # Dark theme
style.configure("TLabel", background="#333333", foreground="#ffffff", font=("Helvetica", 12))  # White text
style.configure("TButton", background="#3498db", foreground="#ffffff", font=("Helvetica", 12))  # Blue buttons
style.configure("TEntry", fieldbackground="#555555", foreground="#ffffff", font=("Helvetica", 12))  # Dark entry fields
style.configure("TScale", background="#333333", troughcolor="#555555", sliderlength=20)  # Dark slider
style.configure("TScrollbar", background="#555555")  # Dark scrollbar
style.configure("TCombobox", background="#555555", fieldbackground="#555555", font=("Helvetica", 12))  # Dark combobox

# Create and place widgets
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Header section
header_frame = ttk.Frame(frame, padding="10")
header_frame.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(header_frame, text="Box 24 - Detail Line Information", font=("Helvetica", 16, "bold")).grid(row=0, column=0, sticky="w", pady=5)

# Input section
input_frame = ttk.Frame(frame, padding="10")
input_frame.grid(row=1, column=0, columnspan=2, pady=10)

ttk.Label(input_frame, text="Propeller (DxP, e.g., 5045):").grid(row=0, column=0, sticky="w", pady=5)
prop_entry = ttk.Entry(input_frame)
prop_entry.grid(row=0, column=1, pady=5, padx=10)

ttk.Label(input_frame, text="Motor KV:").grid(row=1, column=0, sticky="w", pady=5)
kv_entry = ttk.Entry(input_frame)
kv_entry.grid(row=1, column=1, pady=5, padx=10)

slider_label = ttk.Label(input_frame, text=f"Battery Cells: 3", font=("Helvetica", 12))
slider_label.grid(row=2, column=1, pady=5, padx=10)

ttk.Label(input_frame, text="Battery (S rating):").grid(row=3, column=0, sticky="w", pady=5)
battery_slider = ttk.Scale(input_frame, from_=1, to=6, orient=tk.HORIZONTAL, command=update_slider_label)
battery_slider.set(3)
battery_slider.grid(row=3, column=1, pady=5, padx=10)

calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate_thrust_and_current)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

# Result section
result_frame = ttk.Frame(frame, padding="10")
result_frame.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(result_frame, text="", wraplength=400, anchor="center", background="#333333", foreground="#ffffff")  # White text
result_label.grid(row=0, column=0, columnspan=2)

root.mainloop()
