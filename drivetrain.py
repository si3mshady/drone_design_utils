import tkinter as tk
from tkinter import messagebox

class DroneConfigurator:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Configurator")
        self.steps = [
            "Step 1: Enter Total Weight and Thrust-to-Weight Ratio",
            "Step 2: Calculate Thrust Requirements",
            "Step 3: Select Propellers",
            "Step 4: Choose Motors",
            "Step 5: Select Battery",
            "Step 6: Configure ESCs",
            "Step 7: Summary"
        ]
        self.current_step = 0
        self.total_weight = 0
        self.twr = 0
        self.thrust_per_motor = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text=self.steps[self.current_step], font=("Arial", 16))
        self.label.pack(pady=20)

        self.entry1 = tk.Entry(self.root, font=("Arial", 14))
        self.entry2 = tk.Entry(self.root, font=("Arial", 14))
        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 14), command=self.next_step)
        
        self.entry1.pack(pady=10)
        self.entry2.pack(pady=10)
        self.next_button.pack(pady=20)

        self.update_step()

    def update_step(self):
        self.label.config(text=self.steps[self.current_step])
        
        if self.current_step == 0:
            self.entry1.config(state='normal')
            self.entry2.config(state='normal')
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry1.insert(0, "Enter total weight in grams")
            self.entry2.insert(0, "Enter TWR (e.g., 2 for 2:1)")
        else:
            self.entry1.config(state='disabled')
            self.entry2.config(state='disabled')

        if self.current_step > 0:
            self.entry1.pack_forget()
            self.entry2.pack_forget()
        else:
            self.entry1.pack(pady=10)
            self.entry2.pack(pady=10)

    def next_step(self):
        if self.current_step == 0:
            try:
                self.total_weight = float(self.entry1.get())
                self.twr = float(self.entry2.get())
                self.calculate_thrust()
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers for weight and TWR.")
                return

        if self.current_step == 1:
            self.show_thrust_requirements()

        if self.current_step == 2:
            self.show_propeller_selection()

        if self.current_step == 3:
            self.show_motor_selection()

        if self.current_step == 4:
            self.show_battery_selection()

        if self.current_step == 5:
            self.show_esc_configuration()

        if self.current_step == 6:
            self.show_summary()

        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_step()

    def calculate_thrust(self):
        self.total_thrust = self.total_weight * self.twr
        self.thrust_per_motor = self.total_thrust / 4

    def show_thrust_requirements(self):
        messagebox.showinfo("Thrust Requirements",
                            f"Total Thrust Needed: {self.total_thrust} grams\n"
                            f"Thrust per Motor: {self.thrust_per_motor} grams")

    def show_propeller_selection(self):
        self.propellers = "5 to 6-inch propellers"
        messagebox.showinfo("Propeller Selection",
                            f"Recommended Propellers: {self.propellers}")

    def show_motor_selection(self):
        self.motors = "2205 2300KV motors" if self.thrust_per_motor <= 500 else "Check motor thrust data charts for appropriate motors"
        messagebox.showinfo("Motor Selection",
                            f"Recommended Motors: {self.motors}")

    def show_battery_selection(self):
        self.battery = "3S (11.1V) or 4S (14.8V) LiPo battery, 1500mAh to 2200mAh, 75C"
        messagebox.showinfo("Battery Selection",
                            f"Recommended Battery: {self.battery}")

    def show_esc_configuration(self):
        self.escs = "30A ESCs with BLHeli or SimonK firmware"
        messagebox.showinfo("ESC Configuration",
                            f"Recommended ESCs: {self.escs}")

    def show_summary(self):
        summary = (f"Total Thrust Needed: {self.total_thrust} grams\n"
                   f"Thrust per Motor: {self.thrust_per_motor} grams\n"
                   f"Recommended Propellers: {self.propellers}\n"
                   f"Recommended Motors: {self.motors}\n"
                   f"Recommended Battery: {self.battery}\n"
                   f"Recommended ESCs: {self.escs}")
        messagebox.showinfo("Summary", summary)


if __name__ == "__main__":
    root = tk.Tk()
    app = DroneConfigurator(root)
    root.mainloop()
