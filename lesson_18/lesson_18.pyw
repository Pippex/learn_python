import tkinter


root = tkinter.Tk()

root.title("Hello Constanza")
root.resizable(True, True)
root.iconbitmap("cat.ico")
#root.geometry("500x500")
root.config(bg="green")

frame = tkinter.Frame()
frame2 = tkinter.Frame()
frame3 = tkinter.Frame()
frame3.pack(side="left", anchor="n", fill="y")
frame2.pack(side="top", anchor="w", fill="x")
frame.pack(side="top", anchor="w", fill="both", expand=True)
frame.config(bg="red")
frame.config(width=500, height=500)
frame2.config(width=500, height=100)
frame2.config(bg="black")
frame3.config(width=100, height=600)
frame3.config(bg="black")

lgbt = tkinter.Label(frame2, text="Let's Go Brandooooooooooon T", fg="white")
lgbt.place(x=100, y=35)

root.mainloop()