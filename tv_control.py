from tkinter import *
import os
from tkinter import messagebox

def connect():
    tv_ip = ip_entry.get()
    os.system(f"adb connect {tv_ip}")

    app.destroy()
    main_window()

def main_window():
    def up():
        os.system("adb shell input keyevent 19")

    def down():
        os.system("adb shell input keyevent 20")

    def left():
        os.system("adb shell input keyevent 21")

    def right():
        os.system("adb shell input keyevent 22")

    def back():
        os.system("adb shell input keyevent 4")

    def ok():
        os.system("adb shell input keyevent 23")

    def home():
        os.system("adb shell input keyevent 3")

    def volume_up():
        os.system("adb shell input keyevent 24")

    def volume_down():
        os.system("adb shell input keyevent 25")

    def on_close():
        os.system("adb disconnect")
        app.destroy()

    def disconnect():
        disconnect_y_n = messagebox.askyesno("Disconnect?", "Are you sure that you want to disconnect?")

        if disconnect_y_n:
            os.system("adb disconnect")
            app.destroy()

    def write():
        def write_text():
            text_to_write = write_entry.get()
            os.system(f"adb shell input text {text_to_write}")

        def delete():
            write_entry.delete(0, END)

        write_window = Tk()
        write_window.config(bg="#1f1f1f")
        write_window.title("tv control [write]")
        write_window.geometry("200x200")

        write_entry = Entry(write_window, bg="#1f1f2f", fg="white", border=5, font=("Arial", 15, "bold"))
        write_entry.pack(expand=True)

        done_button = Button(write_window, bg="lime", text="done", command=write_text)
        done_button.pack(anchor="sw")

        delete_button = Button(write_window, bg="red", text="delete", command=delete)
        delete_button.pack(anchor="se")

        write_window.bind("<Return>", lambda: write_text())

        write_window.mainloop()

    app = Tk()

    app.title("TV control [main]")
    app.config(bg="#1f1f1f")
    app.geometry("400x400")

    row_1 = Frame(app, height=30, bg="#1f1f1f")
    row_1.pack(fill="x")

    row_2 = Frame(app, height=30, bg="#1f1f1f")
    row_2.pack(fill="x", pady=25, padx=25)

    row_3 = Frame(app, height=30, bg="#1f1f1f")
    row_3.pack(fill="x", padx=25)

    row_4 = Frame(app, height=30, bg="#1f1f1f")
    row_4.pack(fill="x", pady=25)

    up_button = Button(row_1, text=" up ", font=("Arial", 14, "bold"), command=up)
    up_button.pack(side=LEFT, padx=25)

    down_button = Button(row_1, text="down", font=("Arial", 14, "bold"), command=down)
    down_button.pack(side=LEFT, padx=25)

    left_button = Button(row_1, text="left", font=("Arial", 14, "bold"), command=left)
    left_button.pack(side=LEFT, padx=25)

    right_button = Button(row_2, text="right", font=("Arial", 14, "bold"), command=right)
    right_button.pack(side=LEFT)

    back_button = Button(row_2, text="back", font=("Arial", 14, "bold"), command=back)
    back_button.pack(side=LEFT, padx=25)

    ok_button = Button(row_2, text=" ok ", font=("Arial", 14, "bold"), command=ok)
    ok_button.pack(side=LEFT, padx=25)

    home_button = Button(row_3, text="home", font=("Arial", 14, "bold"), command=home)
    home_button.pack(side=LEFT)

    volume_up_button = Button(row_3, text="volume up", font=("Arial", 14, "bold"), command=volume_up)
    volume_up_button.pack(side=LEFT, padx=25)

    volume_down_button = Button(row_3, text="volume down", font=("Arial", 14, "bold"), command=volume_down)
    volume_down_button.pack(side=LEFT)

    disconnect_button = Button(row_4, text="disconnect", font=("Arial", 14, "bold"), command=disconnect)
    disconnect_button.pack(side=LEFT, padx=25)

    write_button = Button(row_4, text="write", font=("Arial", 14, "bold"), command=write)
    write_button.pack(side=LEFT, padx=25)

    app.protocol("WM_DELETE_WINDOW", lambda: on_close())

    app.mainloop()

app = Tk()

app.title("TV control [connect]")
app.config(bg="#1f1f1f")
app.geometry("300x300")

information_text = Label(app, bg="#1f1f1f", fg="white", font=("Arial", 14, "bold"), text="Enter the Ip of the TV")
information_text.pack()

ip_entry = Entry(app, bg="#1f1f2f", fg="white", font=("Arial", 14, "bold"), border=5)
ip_entry.pack(expand=True)

submit_button = Button(app, bg="lime", text="submit", command=connect)
submit_button.pack(anchor="sw")

app.bind("<Return>", lambda: connect())

app.mainloop()
