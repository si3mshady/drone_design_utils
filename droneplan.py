import tkinter as tk
from tkinter import ttk

# Function to calculate weights and thrust
def calculate():
    try:
        # Get values from entries
        motor_weight = int(motor_weight_entry.get())
        esc_weight = int(esc_weight_entry.get())
        frame_weight = int(frame_weight_entry.get())
        rc_receiver_weight = int(rc_receiver_weight_entry.get())
        battery_weight = int(battery_weight_entry.get())
        props_weight = int(props_weight_entry.get())
        telemetry_weight = int(telemetry_weight_entry.get())
        fc_weight = int(fc_weight_entry.get())
        pdb_weight = int(pdb_weight_entry.get())
        ppm_encoder_weight = int(ppm_encoder_weight_entry.get())
        gps_weight = int(gps_weight_entry.get())
        misc_weight = int(misc_weight_entry.get())
        twr_goal = float(twr_goal_entry.get())

        # Get multipliers
        motor_multiplier = int(motor_multiplier_entry.get())
        esc_multiplier = int(esc_multiplier_entry.get())
        props_multiplier = int(props_multiplier_entry.get())

        # Calculate total weight
        total_weight = (motor_weight * motor_multiplier) + (esc_weight * esc_multiplier) + frame_weight + rc_receiver_weight + battery_weight + (props_weight * props_multiplier) + telemetry_weight + fc_weight + pdb_weight + ppm_encoder_weight + gps_weight + misc_weight
        required_thrust = total_weight * twr_goal  # Use the user-defined TWR goal

        # Update labels
        total_weight_label.config(text=f"Total Weight (g): {total_weight}")
        required_thrust_label.config(text=f"Required Thrust (g): {required_thrust:.1f}")
    except ValueError:
        total_weight_label.config(text="Error: Please enter valid numerical values")
        required_thrust_label.config(text="")

# Function to reset all fields to zero
def reset_fields():
    entries = [motor_weight_entry, esc_weight_entry, frame_weight_entry, rc_receiver_weight_entry, battery_weight_entry, props_weight_entry, telemetry_weight_entry, fc_weight_entry, pdb_weight_entry, ppm_encoder_weight_entry, gps_weight_entry, misc_weight_entry, motor_multiplier_entry, esc_multiplier_entry, props_multiplier_entry, twr_goal_entry]
    for entry in entries:
        entry.delete(0, tk.END)
        entry.insert(0, "0")

# Initialize main window
root = tk.Tk()
root.title("Sophisticated Drone Weight and Thrust Calculator")

# Colors from the earthy color scheme
colors = {
    'charcoal': '#264653',
    'persian_green': '#2A9D8F',
    'saffron': '#E9C46A',
    'sandy_brown': '#F4A261',
    'burnt_sienna': '#E76F51',
    'light_cyan': '#E0FBFC'
}

# Configure window background color
root.configure(bg=colors['light_cyan'])

# Create style for sophisticated look
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', foreground=colors['charcoal'], background=colors['light_cyan'], font=('Helvetica', 12))
style.configure('TEntry', foreground=colors['charcoal'], background=colors['light_cyan'], fieldbackground=colors['light_cyan'], font=('Helvetica', 12))
style.configure('TButton', background=colors['burnt_sienna'], foreground=colors['light_cyan'], font=('Helvetica', 12, 'bold'))
style.configure('TFrame', background=colors['light_cyan'])

# Main frame
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Make the grid responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

# Part weights section
part_frame = ttk.LabelFrame(main_frame, text="Part Weights (g)", padding="10 10 10 10")
part_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

labels = ["Motor Weight", "ESC Weight", "Frame Weight", "RC Receiver Weight", "Battery Weight", "Props Weight", "Telemetry Weight", "FC Weight", "PDB Weight", "PPM Encoder Weight", "GPS Weight", "Misc Weight"]
entries = []

for i, label in enumerate(labels):
    ttk.Label(part_frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='e')
    entry = ttk.Entry(part_frame)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky='we')
    part_frame.columnconfigure(1, weight=1)
    entries.append(entry)

(motor_weight_entry, esc_weight_entry, frame_weight_entry, rc_receiver_weight_entry, battery_weight_entry, props_weight_entry, telemetry_weight_entry, fc_weight_entry, pdb_weight_entry, ppm_encoder_weight_entry, gps_weight_entry, misc_weight_entry) = entries

# Default values
motor_weight_entry.insert(0, "55")
esc_weight_entry.insert(0, "28")
frame_weight_entry.insert(0, "272")
rc_receiver_weight_entry.insert(0, "20")
battery_weight_entry.insert(0, "266")
props_weight_entry.insert(0, "40")
telemetry_weight_entry.insert(0, "20")
fc_weight_entry.insert(0, "50")
pdb_weight_entry.insert(0, "20")
ppm_encoder_weight_entry.insert(0, "10")
gps_weight_entry.insert(0, "20")
misc_weight_entry.insert(0, "20")

# Multipliers section
multiplier_frame = ttk.LabelFrame(main_frame, text="Multipliers", padding="10 10 10 10")
multiplier_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(multiplier_frame, text="Motor Multiplier").grid(row=0, column=0, padx=10, pady=5, sticky='e')
motor_multiplier_entry = ttk.Entry(multiplier_frame)
motor_multiplier_entry.grid(row=0, column=1, padx=10, pady=5, sticky='we')
multiplier_frame.columnconfigure(1, weight=1)
motor_multiplier_entry.insert(0, "4")

ttk.Label(multiplier_frame, text="ESC Multiplier").grid(row=1, column=0, padx=10, pady=5, sticky='e')
esc_multiplier_entry = ttk.Entry(multiplier_frame)
esc_multiplier_entry.grid(row=1, column=1, padx=10, pady=5, sticky='we')
esc_multiplier_entry.insert(0, "1")

ttk.Label(multiplier_frame, text="Props Multiplier").grid(row=2, column=0, padx=10, pady=5, sticky='e')
props_multiplier_entry = ttk.Entry(multiplier_frame)
props_multiplier_entry.grid(row=2, column=1, padx=10, pady=5, sticky='we')
props_multiplier_entry.insert(0, "4")

# TWR Goal section
twr_frame = ttk.LabelFrame(main_frame, text="TWR Goal", padding="10 10 10 10")
twr_frame.grid(row=2, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

ttk.Label(twr_frame, text="TWR Goal").grid(row=0, column=0, padx=10, pady=5, sticky='e')
twr_goal_entry = ttk.Entry(twr_frame)
twr_goal_entry.grid(row=0, column=1, padx=10, pady=5, sticky='we')
twr_goal_entry.insert(0, "2")
twr_frame.columnconfigure(1, weight=1)

# Buttons frame
buttons_frame = ttk.Frame(main_frame, padding="10 10 10 10")
buttons_frame.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E))

# Calculate button
calculate_button = ttk.Button(buttons_frame, text="Calculate", command=calculate)
calculate_button.grid(row=0, column=0, padx=5, pady=5, sticky='we')

# Reset button
reset_button = ttk.Button(buttons_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=1, padx=5, pady=5, sticky='we')

buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)

# Labels for displaying results
result_frame = ttk.Frame(main_frame, padding="10 10 10 10")
result_frame.grid(row=4, column=0, pady=10, sticky=(tk.W, tk.E))

total_weight_label = ttk.Label(result_frame, text="Total Weight (g):")
total_weight_label.grid(row=0, column=0, columnspan=2, pady=5, sticky='we')

required_thrust_label = ttk.Label(result_frame, text="Required Thrust (g):")
required_thrust_label.grid(row=1, column=0, columnspan=2, pady=5, sticky='we')

result_frame.columnconfigure(0, weight=1)
result_frame.columnconfigure(1, weight=1)

# Run the application
root.mainloop()
