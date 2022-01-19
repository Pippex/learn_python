from os import waitpid
import tkinter
from PIL import Image, ImageTk



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

communism_image = Image.open("communism.png")
communism_image = communism_image.resize((200, 200))
communism_image = ImageTk.PhotoImage(communism_image)
communism_label = tkinter.Label(frame, image=communism_image)
communism_label.place(x=100, y=100)

real_communism_image = tkinter.PhotoImage(file="real_communism.gif")
real_communism_label = tkinter.Label(frame, image=real_communism_image)
real_communism_label.place(x=300, y=300)

flag_8bit = Image.open("8bit_communist_flag.png")
flag_8bit = flag_8bit.resize((200, 200))
flag_8bit = ImageTk.PhotoImage(flag_8bit)
flag_8bit_label = tkinter.Label(frame, image=flag_8bit)
flag_8bit_label.place(x=100, y=300)

best_dentist = Image.open("the_best_dentist_is_communist.png")
best_dentist = best_dentist.resize((120, 200))
best_dentist = ImageTk.PhotoImage(best_dentist)
best_dentist_label = tkinter.Label(frame, image=best_dentist)
best_dentist_label.place(x=300, y=100)

what_are_you = tkinter.Label(frame, text="What are you?")
what_are_you.place(x=510, y=500)

to_gulag_entry = tkinter.Entry(frame)
to_gulag_entry.place(x=600, y=500)

#Creating a Quiz

proletary = tkinter.Label(frame2, text="Are you a proletary?")
proletary.grid(row=0,column=0, sticky="e")
answer_proletary = tkinter.Entry(frame2, bg="#F7CB15", cursor="@communist.cur")
answer_proletary.grid(row=0, column=1)

production_means = tkinter.Label(frame2, text="Do you have any means of production?")
production_means.grid(row=1, column=0, sticky="e")
answer_production_means = tkinter.Entry(frame2, bg="#F55D3E", cursor="@communist.cur")
answer_production_means.grid(row=1, column=1)

many_chinas = tkinter.Label(frame2, text="How many Chinas exists?")
many_chinas.grid(row=2, column=0, sticky="e")
answer_many_chinas = tkinter.Entry(frame2, bg="#F7CB15", cursor="@communist.cur")
answer_many_chinas.grid(row=2, column=1)

#Adds a question about tiananmmen square 1989 in the upper and right frame

tiananmmen_square = tkinter.Label(frame2, text="What happened in Tiananmmen Square in 1989?")
tiananmmen_square.grid(row=3, column=0, sticky="e")
answer_tiananmmen = tkinter.Entry(frame2, bg="#F55D3E", cursor="@communist.cur")
answer_tiananmmen.grid(row=3, column=1)


root.mainloop()