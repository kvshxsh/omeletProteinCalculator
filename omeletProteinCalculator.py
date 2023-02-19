import tkinter as tk
from tkinter import messagebox, Toplevel
import tkinter.messagebox as messagebox


def calculate_protein():
        eggs = float(eggs_entry.get())
        bread = float(bread_entry.get())

        protein_eggs = 6 #grams
        protein_bread = 2 #grams
        protein_omelet = (eggs*protein_eggs) + (bread*protein_bread)

        result_label.config(text="The omelet has %0.1f grams of protein" % protein_omelet)

# Create the main window
window = tk.Tk()
window.geometry("600x400")
window.title("Omelet Protein Calculator")
window.configure(bg='teal')


# Create widgets
label_font = ("Arial", 20)
label_font1 = ('Arial', 18)
entry_font = ('Arial', 15)

eggs_label = tk.Label(text="Input the number of eggs the omelet contains:", font=label_font, background = 'teal')
eggs_entry = tk.Entry(width=50, font=entry_font, background = 'white')
bread_label = tk.Label(text="Input the number of bread loaves the omelet contains:", font=label_font1, background = 'teal')
bread_entry = tk.Entry(width = 50, font=entry_font,background = 'white')
result_label = tk.Label(text="", font=label_font, background = 'teal')
calculate_button = tk.Button(text="Calculate Protein", command=calculate_protein, font=label_font, background = 'teal')



# Add widgets to the window
eggs_label.pack()
eggs_entry.pack()
bread_label.pack()
bread_entry.pack()
calculate_button.pack()
result_label.pack()
# Run the main loop
window.mainloop()
 
