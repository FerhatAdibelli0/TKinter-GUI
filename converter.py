from tkinter import *

def clicked():
    try:
        # Convert input to float and calculate kilometers
        miles = float(text_input.get())
        kilometers = miles * 1.60934  # Conversion factor from miles to kilometers
        # Update the result label
        text_result.config(text=f"{kilometers:.2f} Km")
    except ValueError:
        # Handle invalid input
        text_result.config(text="Invalid input")

window = Tk()
window.title("Mile to KM Converter")
window.maxsize(width=400, height=400)
window.config(padx=10, pady=50)

# Entry widget for user input
text_input = Entry(width=25)
text_input.grid(column=1, row=0)

# Labels for Miles and Km
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# Label to show "is equal to"
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

# Label to show the result
text_result = Label(text="")
text_result.grid(column=1, row=1)

# Button to perform conversion
click_button = Button(text="Convert", command=clicked)
click_button.grid(column=1, row=2)

window.mainloop()