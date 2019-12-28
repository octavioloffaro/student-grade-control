# John Disandolo

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
import csv
from functions import *
from lecturer import *
from student import *


class Welcome(tk.Tk):
    """
    LOGIN WINDOW (STARTUP)

    Example login for student:
        -  ID:        123456
        -  Password:  DQSteam8

    Example login for lecturer:
        -  Username:  Mr. Example
        -  Password:  DQSteam8
        
        -  Username:  DannyGriff98
        -  Password:  DannyGriff98
    
    """

    def __init__(self):
        super().__init__()

        # set up window
        self.title("Short Assessment System - Team 8")
        self.geometry("500x300")
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

        self.header_label2 = ttk.Label(self.f1, text="Sign in", font=tkFont.nametofont("TkHeadingFont"))
        self.header_label2.pack(side='left')

        self.sub_label = ttk.Label(self, text="I'm signing in as...")
        self.sub_label.grid(row=1, column=0, padx=(30,0), sticky='W')


        # radiobuttons for selecting between existing/new lecturer and student
        self.v = tk.IntVar()
        self.exlect_rad = ttk.Radiobutton(self, text="an existing lecturer", variable=self.v, value=1, command=self.change_text)
        self.exlect_rad.grid(row=2, column=0, padx=(40,0), pady=(5,0), sticky='W')

        self.nwlect_rad = ttk.Radiobutton(self, text="a new lecturer", variable=self.v, value=2, command=self.change_text)
        self.nwlect_rad.grid(row=3, column=0, padx=(40,0), sticky='W')

        self.student_rad = ttk.Radiobutton(self, text="a student", variable=self.v, value=3, command=self.change_text)
        self.student_rad.grid(row=4, column=0, padx=(40,0), pady=(10,0), sticky='W')


        # note to explain student login details
        self.note_label = ttk.Label(self, text="If you are a student, you should\nhave received your login details\nby email.", font=tkFont.nametofont("TkCaptionFont"))
        self.note_label.grid(row=5, column=0, padx=(40, 60), pady=(20,0), sticky='W')
        

        # entry widgets w/ respective labels
        self.username_label = ttk.Label(self, text="Username:".ljust(20))
        self.username_label.grid(row=1, column=1, sticky='W')
        
        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.grid(row=2, column=1, sticky='W', pady=(5,0))

        self.password_label = ttk.Label(self, text="Password:".ljust(20))
        self.password_label.grid(row=4, column=1, sticky='W')
        
        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.grid(row=5, column=1, sticky='NW')


        # sign in button
        self.arrow_img = tk.PhotoImage(file="images/right_arrow.png")
        self.ok_button = ttk.Button(self, image=self.arrow_img, text="  Sign in".ljust(15), compound="right", command=self.verify_details)
        self.ok_button.grid(row=6, column=1, sticky='SE')


        # allow user to type into username entry straightaway
        self.v.set(1)
        self.username_entry.focus_set()

        # let the user sign in by pressing the return key
        self.bind("<Return>", self.verify_details)
        


    def change_text(self) :
        """
        Change the text of the entry headers when the user
        clicks a radiobutton.
        
        """

        if self.v.get() == 2 :       # new lecturer
            self.header_label2['text'] = "Sign up"
            self.ok_button['text'] = "  Sign up".ljust(15)
            self.username_label['text'] = "Create a username:"
            self.password_label['text'] = "Create a password:"

        elif self.v.get() == 3 :     # student
            self.header_label2['text'] = "Sign in"
            self.ok_button['text'] = "  Sign in".ljust(15)
            self.username_label['text'] = "Your StudentID:"
            self.password_label['text'] = "Password:"
            
        else :                      # existing lecturer (default)
            self.header_label2['text'] = "Sign in"
            self.ok_button['text'] = "  Sign in".ljust(15)
            self.username_label['text'] = "Username:"
            self.password_label['text'] = "Password:"
        
    
    def verify_details(self, event=None) :
        """
        Verify entry details are valid and correct.

        """
        
        try :
            if not(1 <= self.v.get() <= 3) :
                # no radiobutton selected
                raise Exception("Please select from the options on the left of the window.")

            if self.username_entry.get() == "" or self.password_entry.get() == "" :
                # one of both entry widgets left blank
                raise Exception("Please fill in all required fields.")

            if len(self.password_entry.get()) <= 5 :
                # password is too short
                raise Exception("Your password must be more than 5 characters long.")

            if len(self.username_entry.get()) > 15 and not(self.v.get() == 3) :
                # password is too short
                raise Exception("Your username should not be more than 15 characters.")
            
     
            if self.v.get() == 1 :      # existing lecturer
                self.login_user(self.username_entry.get(), self.password_entry.get(), True)
                
            elif self.v.get() == 2 :    # new lecturer
                self.create_lecturer(self.username_entry.get(), self.password_entry.get())
            
            else :                      # student
                self.login_user(self.username_entry.get(), self.password_entry.get(), False)


        except Exception as e:
            msg.showerror("Error", "An error occurred:\n" + str(e))


    def login_user(self, username, password, is_lecturer) :
        """
        Login an existing user according to their details entered.

        """

        if is_lecturer :
            data = read_csv('data/lecturers.csv')

        else :
            data = read_csv('data/students.csv')

            
        for count, row in enumerate(data) :
    
            if count != 0 : # skip header of CSV
                if row[0] == username :                
                    if row[1] == self.encrypt_string(password) :                     
                        self.destroy()

                        if is_lecturer :
                            Lecturer(username)

                        else :
                            Student(username)
                            
                        return

        msg.showerror("Incorrect Details", "Your username or password seem to be incorrect.\nPlease try again.")
        return


    def create_lecturer(self, username, password) :
        """
        Create a new lecturer account with given details.

        """
        
        with open('data/lecturers.csv', 'a', newline='') as csvfile : 
            writer = csv.writer(csvfile)
            writer.writerow([username, self.encrypt_string(password)])

        self.login_user(username, password, True)


    def encrypt_string(self, decrypted) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        key = "SOPURVHNFKMJQAIEBWDCLYTXZGsopurvhnfkmjqaiebwdclytxzg"
        enc = ""

        for char in decrypted:
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
                char = key[alphabet.index(char)]
            enc = enc + char

        return enc


    def decrypt_string(self, encrypted) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        key = "SOPURVHNFKMJQAIEBWDCLYTXZGsopurvhnfkmjqaiebwdclytxzg"
        dec = ""

        for char in encrypted:
            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
                char = alphabet[key.index(char)]
            dec = dec + char

        return dec

    
        
if __name__ == "__main__":
    welcome = Welcome()
    welcome.mainloop()

