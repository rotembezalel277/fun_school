import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

            if user_entry.get() == teacher:
                tkmb.showinfo(title="Login Successful", message="You have logged in successfully to teacher account.")
                ctk.CTkLabel(new_window, text="Fun School is best for learning ANYTHING !!").pack()
            elif user_entry.get() == student:
                tkmb.showinfo(title="Login Successful",
                                 message="You have logged in successfully to student account.")
                import games_page
            else:
                tkmb.showerror(title="Login Failed", message="Invalid password")

        label = ctk.CTkLabel(app, text="This is the login page of Fun School")

        label.pack(pady=20)

        frame = ctk.CTkFrame(master=app)
        frame.pack(pady=20, padx=40, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Fun School Login System')
        label.pack(pady=12, padx=10)

        user_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        user_entry.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text='Login', command=login)
        button.pack(pady=12, padx=10)


        checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
        checkbox.pack(pady=12, padx=10)

        app.mainloop()

# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()