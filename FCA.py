from tkinter import *
root = Tk()
root.title('FCA')
#root.iconbitmap('Portal.ico')

class App:
    def __init__(self,master):
        my_frame = Frame(master)
        my_frame.pack()

        self.my_button = Button(master, text="Click", command=self.clicker)
        self.my_button.pack(pady=20)

    def clicker(self):
        print("Clicked!")

e = App(root)

root.mainloop()