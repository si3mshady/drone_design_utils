import tkinter as tk
from tkinter import ttk

# Function to calculate the estimated maximum current draw and recommend an ESC
def calculate_esc():
    # Get values from entries
    prop_size = prop_size_entry.get()
    battery_type = battery_type_entry.get()
    motor_spec = motor_spec_entry.get()

    # Simple assumption: Estimated Maximum Current Draw = 15A (this can be replaced with a more accurate formula)
    max_current_draw = 15  # Placeholder value
    recommended_esc_current = max_current_draw * 1.2

    # Update labels with results
    max_current_draw_label.config(text=f"Estimated Maximum Current Draw: ~{max_current_draw}A")
    recommended_esc_label.config(text=f"Recommended ESC Current Rating: {recommended_esc_current:.1f}A")

# Initialize main window
root = tk.Tk()
root.title("ESC Selector Tool")
root.configure(bg='#1a1a1a')  # Dark grey background

# Create style for sophisticated look
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', foreground='#00aaff', background='#1a1a1a', font=('Helvetica', 12))
style.configure('TEntry', foreground='#00aaff', background='#1a1a1a', fieldbackground='#1a1a1a', font=('Helvetica', 12))
style.configure('TButton', background='#1a1a1a', foreground='#00aaff', font=('Helvetica', 12, 'bold'))
style.configure('TFrame', background='#1a1a1a')

# Main frame
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields section
input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10 10 10 10")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Prop Size (e.g., 10x45)").grid(row=0, column=0, padx=10, pady=5, sticky='e')
prop_size_entry = ttk.Entry(input_frame)
prop_size_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Battery Type (e.g., 3S)").grid(row=1, column=0, padx=10, pady=5, sticky='e')
battery_type_entry = ttk.Entry(input_frame)
battery_type_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(input_frame, text="Motor Spec (e.g., 935KV/2213)").grid(row=2, column=0, padx=10, pady=5, sticky='e')
motor_spec_entry = ttk.Entry(input_frame)
motor_spec_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_esc)
calculate_button.grid(row=1, column=0, pady=10)

# Result labels
result_frame = ttk.Frame(main_frame, padding="10 10 10 10")
result_frame.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E))

max_current_draw_label = ttk.Label(result_frame, text="Estimated Maximum Current Draw: ~15A")
max_current_draw_label.grid(row=0, column=0, columnspan=2, pady=5)

recommended_esc_label = ttk.Label(result_frame, text="Recommended ESC Current Rating: 18A")
recommended_esc_label.grid(row=1, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
