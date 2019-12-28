# Daniel Griffiths

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
from functions import *
from datetime import datetime
import csv


class CreateTest(tk.Toplevel):
    """
    TEST SCREEN
    
    """
    def __init__(self, parent):
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
        

        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", background="#ffffff")
        style.configure("TLabel", background="#ffffff")
        style.configure("TRadiobutton", background="#ffffff")
        

        # header and subtitle
        self.header_label = ttk.Label(self, text="Test Creation", font=tkFont.nametofont("TkHeadingFont"))
        self.header_label.grid(row=0, column=0, columnspan=2, padx=(30,0), pady=(20, 10), sticky='W')

        #radio buttons to choose test type

        self.sub_label = ttk.Label(self, text="Test Type:")
        self.sub_label.grid(row=1, column=0, padx=(30,0), pady= (5,0), sticky='W')
        
        self.Form = tk.StringVar()
        
        self.Form_rad = ttk.Radiobutton(self, text="Formative Test", variable=self.Form, value="Formative")
        self.Form_rad.grid(row=1, column=2, padx=(30,0), pady= (5,0), sticky='W')

        self.Form_rad = ttk.Radiobutton(self, text="Summative Test", variable=self.Form, value="Summative")
        self.Form_rad.grid(row=1, column=3, padx=(30,0), pady= (5,0), sticky='W')

        self.Form.set("Formative")

        self.Question = 1

        self.QuestionTitle = StringVar()
        self.QuestionTitle.set("Question" + str(self.Question))


        self.Qnum = ttk.Label (self, textvariable=self.QuestionTitle)
        self.Qnum.grid(row=2, column=0, padx=(55,0), pady= (20,0), sticky='W')

        self.f1 = tk.Frame(self, bg='#ffffff')
        self.f1.grid(row=3, column=0, columnspan=4, padx=(30,0), sticky="NSEW")        

        self.Question_textBox = ttk.Entry(self.f1, foreground="grey",width= 57)
        self.Question_textBox.grid(row=0, column=1, pady= (20,0), sticky="WE")
        self.Question_textBox.insert(0, "Enter Question Here")
        self.Question_textBox.bind('<FocusIn>', self.question_entry_click)
        self.Question_textBox.bind('<FocusOut>', self.on_focusout)

        self.Answer_textBox = tk.Text(self.f1, foreground="grey", height = 5, width = 30, font=tkFont.nametofont("TkCaptionFont"))
        self.Answer_textBox.grid(row=1, column=1, pady= (10,0), sticky="WE")
        self.Answer_textBox.insert(1.0, "Enter Answers Here\nPlease put * before correct answer")
        self.Answer_textBox.bind('<FocusIn>', self.answer_entry_click)
        self.Answer_textBox.bind('<FocusOut>', self.on_focusout)

        self.right_arrow_img = tk.PhotoImage(file="images/right_arrow.png")
        self.next_button = tk.Button(self.f1, bg = "#ffffff", image=self.right_arrow_img, compound="right", width=20, relief = "flat", command=self.Nextbutton)
        self.next_button.grid(row=1, column=2, sticky='E')

        self.left_arrow_img = tk.PhotoImage(file="images/left_arrow.png")
        self.prev_button = tk.Button(self.f1, bg = "#ffffff", image=self.left_arrow_img, compound="right", width=20, relief = "flat", command=self.Prevbutton)
        self.prev_button.grid(row=1, column=0, sticky='W')

        self.Question_textBox.focus_set()

        self.Questions = [["",""] for i in range(11)]
        self.Valid = True

    def question_entry_click(self, event):
        """function that gets called whenever entry is clicked"""
        if self.Question_textBox.get() == "Enter Question Here":
           self.Question_textBox.delete(0, "end") # delete all the text in the entry
           self.Question_textBox.config(foreground="black")
    def answer_entry_click(self, event):
        text = self.Answer_textBox.get(1.0, END)
        if text == "Enter Answers Here\nPlease put * before correct answer\n":
           self.Answer_textBox.delete(1.0, END) # delete all the text in the entry
           self.Answer_textBox.insert(1.0, '') #Insert blank for user input
           self.Answer_textBox.config(foreground="black")
    def deadline_entry_click(self, event):
        """function that gets called whenever entry is clicked"""
        if self.Question_textBox.get() == "Enter Deadline Date (e.g DD/MM/YYYY HH:MM)":
           self.Question_textBox.delete(0, "end") # delete all the text in the entry
           self.Question_textBox.config(foreground="black")
    def emails_entry_click(self, event):
        text = self.Answer_textBox.get(1.0, END)
        if text == "Enter Emails and Press next To Submit\n":
           self.Answer_textBox.delete(1.0, END) # delete all the text in the entry
           self.Answer_textBox.insert(1.0, '') #Insert blank for user input
           self.Answer_textBox.config(foreground="black")
    def on_focusout(self, event):
        if self.Question_textBox.get() == '':
            self.Question_textBox.insert(0, "Enter Question Here")
            self.Question_textBox.config(foreground="grey")
        text = self.Answer_textBox.get(1.0, END)
        if text == "\n":
            self.Answer_textBox.insert(1.0, "Enter Answers Here\nPlease put * before correct answer")
            self.Answer_textBox.config(foreground="grey")
    def on_focusouts(self, event):
        if self.Question_textBox.get() == '':
            self.Question_textBox.insert(0, "Enter Deadline Date (e.g DD/MM/YYYY HH:MM)")
            self.Question_textBox.config(foreground="grey")
        text = self.Answer_textBox.get(1.0, END)
        if text == "\n":
            self.Answer_textBox.insert(1.0, "Enter Emails and Press next To Submit")
            self.Answer_textBox.config(foreground="grey")
    def Nextbutton(self):
        if self.Question == 12:
            try:
                if datetime.strptime(self.Question_textBox.get(), "%d/%m/%Y %H:%M") < datetime.now():
                    msg.showerror("error", "This Date Has Past")
                elif self.Answer_textBox.get(1.0, END) == "Enter Emails and Press next To Submit\n":
                    msg.showerror("Error", "Please Enter At Least One Email")
                else:
                    for items in self.Answer_textBox.get(1.0, END).split("\n"):
                        if items != "":
                            id_exists = True
                            Studentid = 0
                            
                            while id_exists :
                                id_exists = False
                                
                                # generate random 6-digit testid
                                Studentid = randint(100000, 999999)
                                      
                                for count, row in enumerate(read_csv('data/students.csv')) :
                                        
                                    if count != 0 : # skip header of CSV
                                        if int(row[0]) == Studentid :                
                                            id_exists = True
                            with open('data/students.csv', 'a', newline='') as csvfile : 
                                writer = csv.writer(csvfile)
                                writer.writerow([Studentid, Studentid, items])
                    for elements in self.Questions:
                        if elements[0] == "":
                            self.Questions.remove(elements)
                        elements[1] = elements[1].replace("\n", "**")
                        if elements[1] == "**":
                            elements[1] = ""
                    self.Questions.insert(0,self.Question_textBox.get())
                    self.Questions.insert(0,self.Form.get())
                    save_test(self.Questions)
                    msg.showinfo("Submission Complete", "The test has been submitted")
                    self.destroy()
            except:
                msg.showerror("Error", "Please enter a deadline as shown DD/MM/YYYY HH:MM")

        if self.Question <= 10:
            try:
                if self.Answer_textBox.get(1.0, END).count("*") != 1 and self.Answer_textBox.get(1.0, END) != "\n":
                    raise Exception("You Can Only Have One Correct Answer")
                    

                elif not (2 <= self.Answer_textBox.get(1.0, END).count("\n") <= 5) and self.Answer_textBox.get(1.0, END) != "\n":
                    raise Exception("You Must Have More Than 1 and Less Than 6 Answers")

                elif (self.Answer_textBox.get(1.0, END) != "" and self.Answer_textBox['foreground'] == 'black') and (self.Question_textBox.get() == "" or self.Question_textBox.get() == "Enter Question Here") and self.Answer_textBox.get(1.0, END) != "\n":
                    raise Exception("You Must Include A Question ")

                elif self.Answer_textBox.get(1.0, END) != "" and self.Answer_textBox['foreground'] == 'black' and self.Answer_textBox.get(1.0, END) != "\n":
                    self.Valid = False
                    for answer in self.Answer_textBox.get(1.0,END).split("\n"):
                        if answer != "":
                            if answer[0] == "*":
                                self.Valid = True
                                break
                    if self.Valid == False:
                        raise Exception("Please Start Correct Answer With A *")
                if self.Valid == True:
                    self.Question += 1
                    self.QuestionTitle.set("Question" + str(self.Question))

                    if self.Answer_textBox['foreground'] == 'grey' :
                        self.Answer_textBox.delete(1.0,END)

                    if self.Question_textBox.get() == 'Enter Question Here' :
                        self.Question_textBox.delete(0,END)
                                        
                    
                    ##if self.Answer_textBox.get(1.0, END) != "" and self.Answer_textBox['foreground'] != 'grey':
                    self.Questions[self.Question - 2] = [self.Question_textBox.get(), self.Answer_textBox.get(1.0, END)]
                    self.Question_textBox.delete(0,END)
                    self.Answer_textBox.delete(1.0,END)

                    if self.Questions[self.Question - 1][0] == "":

                        self.Answer_textBox["foreground"] = "grey"
                        self.Answer_textBox.grid(row=1, column=1, pady= (10,0), sticky="WE")
                        self.Answer_textBox.insert(1.0, "Enter Answers Here\nPlease put * before correct answer")
                    else:
                        self.Question_textBox["foreground"] = "black"
                        self.Question_textBox.insert(0, self.Questions[self.Question - 1][0])
                        self.Answer_textBox["foreground"] = "black"
                        self.Answer_textBox.insert(1.0, self.Questions[self.Question - 1][1])

                    self.Question_textBox.focus_set()
                
                    if self.Question == 11:
                        self.focus_set()
                        self.Question += 1
                        self.QuestionTitle.set("Quiz summary")
                        self.Question_textBox.delete(0,END)
                        self.Answer_textBox.delete(1.0,END)
                        self.Question_textBox["foreground"] = "grey"
                        self.Question_textBox.insert(0, "Enter Deadline Date (e.g DD/MM/YYYY HH:MM)")
                        self.Question_textBox.bind('<FocusIn>', self.deadline_entry_click)
                        self.Question_textBox.bind('<FocusOut>', self.on_focusouts)
                        self.Answer_textBox.insert(1.0, "Enter Emails and Press next To Submit")
                        self.Answer_textBox.bind('<FocusIn>', self.emails_entry_click)
                        self.Answer_textBox.bind('<FocusOut>', self.on_focusouts)

                        for elements in self.Questions:
                            elements[1] = elements[1].replace("\n", "**")
                            if elements[1] == "**":
                                elements[1] = ""
            except Exception as e:
                msg.showerror("Error", e)
                 
    def Prevbutton(self):
        if 2 <= self.Question <= 11:
            self.Question -= 1
            self.QuestionTitle.set("Question" + str(self.Question))
            self.Question_textBox.delete(0,END)
            self.Answer_textBox.delete(1.0,END)
            self.getquestion = self.Questions[self.Question-1][0]
            self.getanswer = self.Questions[self.Question-1][1]
            if self.getanswer != "\n":
                self.Question_textBox.insert(0, self.getquestion)
                self.Answer_textBox.insert(1.0, self.getanswer[:-1])
                self.Answer_textBox["foreground"] = "black"
                self.Question_textBox["foreground"] = "black"
            else:
                self.Answer_textBox["foreground"] = "grey"
                self.Answer_textBox.insert(1.0, "Enter Answers Here\nPlease put * before correct answer")

        self.Question_textBox.focus_set()
            
if __name__ == "__main__":
    creation = CreateTest()
    creation.mainloop()
