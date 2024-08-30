import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = tkinter.Label(text="testing...", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def click_me():
    # my_label.config(text=data.get())
    my_label["text"] = data.get()


button = tkinter.Button(text="First New Button", command=click_me)
button.grid(column=1, row=1)

button = tkinter.Button(text="Second New Button", command=click_me)
button.grid(column=3, row=0)

data = tkinter.Entry(width=50)
data.grid(column=4, row=2)

window.mainloop()
