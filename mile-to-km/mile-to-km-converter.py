from tkinter import *
# constants for the conversion
# 1 mile = 1.60934 km
MILE_CONST = 1.60934

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * MILE_CONST
    kilometer_label_result.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=70, pady=20)

# input field
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

kilometer_label_result = Label(text="0")
kilometer_label_result.grid(column=1, row=1)

callable_button = Button(text="Calculate", command=miles_to_km)
callable_button.grid(column=1, row=2)
window.mainloop()

