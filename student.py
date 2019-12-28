# John Disandolo

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
import csv
from datetime import datetime
from functions import *
from taketest import *
from results import *


class Student(tk.Tk):
    """
    STUDENT WELCOME WINDOW
    
    """

    studentid = ""

    def __init__(self, current_user=""):
        super().__init__()

        # set up window
        self.title("Short Assessment System - Team 8")
        self.geometry("550x220")
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

        self.header_label2 = ttk.Label(self.f1, text="Welcome Student" + current_user, font=tkFont.nametofont("TkHeadingFont"))
        self.header_label2.pack(side='left')

        self.sub_label = ttk.Label(self, text="Enter a TestID into the box below...")
        self.sub_label.grid(row=1, column=0, padx=(30,0), sticky='W')



        # configure buttons with icons
        self.f2 = tk.Frame(self, bg='#ffffff')
        self.f2.grid(row=2, column=0, columnspan=2, padx=(30,0), sticky="NSEW")


        # entry widgets w/ respective labels
        self.testid_entry = ttk.Entry(self.f2)
        self.testid_entry.grid(row=0, column=0, columnspan=3, sticky='WE', pady=(20,10))
        
        
        self.pencil_img = tk.PhotoImage(file="images/pencil_small.png")
        self.test_button = ttk.Button(self.f2, image=self.pencil_img, text="  Take the test", compound="left", command=lambda:self.take_test(current_user), width=20)
        self.test_button.grid(row=1, column=0, sticky='W')

        self.tick_img = tk.PhotoImage(file="images/tick_small.png")
        self.stats_button = ttk.Button(self.f2, image=self.tick_img, text="  Marks & feedback", compound="left", command=lambda:self.marks_feedback(current_user), width=20)
        self.stats_button.grid(row=1, column=1, padx=(5, 0), sticky='W')

        self.signout_button = ttk.Button(self.f2, text="Sign out and exit", command=self.sign_out, width=20)
        self.signout_button.grid(row=1, column=2, padx=(5, 0), sticky='NSW')


        # allow user to type into testid entry straightaway
        self.testid_entry.focus_set()
        self.focus_force()
        



    def take_test(self, current_user) :
        testid = self.testid_entry.get()
        
        if is_valid_id(self.testid_entry.get()) :
            if get_test_type(int(testid)) == 'Summative' and get_test_attempts(int(testid), int(current_user)) < 1 :
                Quiz(self, self.testid_entry.get(), current_user).grab_set()

            elif get_test_type(int(testid)) == 'Formative' and get_test_attempts(int(testid), int(current_user)) < 3 :
                Quiz(self, self.testid_entry.get(), current_user).grab_set()

            elif get_test_deadline(int(testid)) < datetime.now() :
                msg.showerror("Deadline Reached", "The deadline for this test has passed.\nYou can no longer take this test.")

            else :
                msg.showerror("Maximum Attempts Reached", "You have reached the maximum number of attempts allowed for this test.")
    

    def marks_feedback(self, current_user) :        
        if is_valid_id(self.testid_entry.get()) :
            Results(self, self.testid_entry.get(), current_user).grab_set()
            return
        

    def sign_out(self) :
        if msg.askokcancel("Exit Program", "The application will close and all unsaved work will be lost.\nClick OK to continue.") :
            exit()
    

        
if __name__ == "__main__":
    student = Student()
    student.mainloop()

