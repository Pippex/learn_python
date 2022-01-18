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
frame.config(bg="#B4E1FF")
frame.config(width=500, height=500)
frame2.config(width=500, height=100)
frame2.config(bg="#F5FFC6")
frame3.config(width=100, height=600)
frame3.config(bg="#F5FFC6")

lgbt = tkinter.Label(frame2, text="Let's Go Brandooooooooooon T", fg="#000000", font=("Comic Sans MS", 50))
#lgbt.place(x=300, y=300)
lgbt.pack()


root.mainloop()