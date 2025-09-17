import customtkinter as ctk
import tkinter.messagebox as tkmb


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Welcome to Fun School!")


def login():

    teacher = "teacher"
    student = "1111"

    new_window = ctk.CTkToplevel(app)

    new_window.title("New Window")

    new_window.geometry("350x150")

    if user_entry.get() == teacher :
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully to teacher account.")
        ctk.CTkLabel(new_window,text="Fun School is best for learning ANYTHING !!").pack()
    elif user_entry.get() == student:
        tkmb.showwarning(title="Login Successful",message="You have logged in successfully to student account.")
    else:
        tkmb.showerror(title="Login Failed",message="Invalid password")



label = ctk.CTkLabel(app,text="This is the login page of Fun School")

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text='Fun School Login System')
label.pack(pady=12,padx=10)


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Password", show="*")
user_entry.pack(pady=12,padx=10)


button = ctk.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)


app.mainloop()