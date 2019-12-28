# John Disandolo

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
import csv
from functions import *
from creation import *
from stats import *
from performance import *


class Lecturer(tk.Tk):
    """
    LECTURER WELCOME WINDOW
    
    """

    def __init__(self, current_user=""):
        super().__init__()


        # set up window
        self.title("Short Assessment System - Team 8")
        self.geometry("550x300")
        self.resizable(False, False)
        self.configure(background="#ffffff")
        self.iconbitmap('images/app_icon.ico')


        # configure default heading font and control styles
        heading_font = tkFont.nametofont("TkHeadingFont")
        heading_font.configure(size=18)

        caption_font = tkFont.nametofont("TkCaptionFont")
        caption_font.configure(slant='italic')
        

        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", background="#ffffff")
        style.configure("TLabel", background="#ffffff")
        style.configure("TRadiobutton", background="#ffffff")
        

        # header and subtitle
        self.f1 = tk.Frame(self, bg='#ffffff')
        self.f1.grid(row=0, column=0, columnspan=2, padx=(30,0), pady=(20, 10), sticky="NSEW")        
        self.appicon = tk.PhotoImage(file="images/app_icon.png")

        self.header_label1 = ttk.Label(self.f1, image=self.appicon)
        self.header_label1.pack(side='right')

        self.header_label2 = ttk.Label(self.f1, text="Welcome " + current_user, font=tkFont.nametofont("TkHeadingFont"), width=35)
        self.header_label2.pack(side='left')

        self.sub_label = ttk.Label(self, text="What would you like to do?")
        self.sub_label.grid(row=1, column=0, padx=(30,0), pady=(0, 30), sticky='W')


        # configure buttons with icons
        self.f2 = tk.Frame(self, bg='#ffffff')
        self.f2.grid(row=2, column=0, columnspan=2, padx=(30,0), sticky="NSEW")
        
        self.pencil_img = tk.PhotoImage(file="images/pencil.png")
        self.test_button = ttk.Button(self.f2, image=self.pencil_img, text="Create New Test", compound="top", command=self.create_test, width=20)
        self.test_button.grid(row=0, column=0, padx=(30, 0), sticky='W')

        self.tick_img = tk.PhotoImage(file="images/tick.png")
        self.stats_button = ttk.Button(self.f2, image=self.tick_img, text="Formative Test Stats", compound="top", command=self.test_stats, width=20)
        self.stats_button.grid(row=0, column=1, padx=(5, 0), sticky='W')

        self.student_img = tk.PhotoImage(file="images/student.png")
        self.performance_button = ttk.Button(self.f2, image=self.student_img, text="Student Performance", compound="top", command=self.student_performance, width=20)
        self.performance_button.grid(row=0, column=2, padx=(5, 0), sticky='W')

        self.signout_button = ttk.Button(self.f2, text="Sign out and exit", command=self.sign_out, width=20)
        self.signout_button.grid(row=1, column=0, columnspan=3, padx=(30, 0), pady=(5, 0), sticky='WE')


        # focus on this window
        self.focus_force()
        


    def create_test(self) :
        CreateTest(self).grab_set()
        return
    

    def test_stats(self) :
        Stats(self).grab_set()
        return
    

    def student_performance(self) :
        Performance(self).grab_set()
        return


    def sign_out(self) :
        if msg.askokcancel("Exit Program", "The application will close and all unsaved work will be lost.\nClick OK to continue.") :
            exit()
    

        
if __name__ == "__main__":
    lecturer = Lecturer()
    lecturer.mainloop()

