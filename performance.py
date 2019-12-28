# Hossein Ramezanian 

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as msg
import csv
from functions import *
from lecturer import *
from student import *
from collections import defaultdict
import tkinter
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import glob


class Performance(tk.Toplevel):

    def __init__(self, parent):
        super().__init__()


        self.title("Short Assessment System - Team 8")
        self.geometry("480x380")
        self.resizable(False, False)
        self.configure(background="#ffffff")
        self.iconbitmap('images/app_icon.ico')


        heading_font = tkFont.nametofont("TkHeadingFont")
        heading_font.configure(size=18)

        caption_font = tkFont.nametofont("TkCaptionFont")
        caption_font.configure(slant='italic')
        

        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", background="#ffffff")
        style.configure("TLabel", background="#ffffff")
        style.configure("TRadiobutton", background="#ffffff")
        

        self.f1 = tk.Frame(self, bg='white')
        self.f1.grid(row=0, column=0, columnspan=2, padx=(30,0), pady=(20, 10), sticky="NSEW")        
        self.appicon = tk.PhotoImage(file="images/app_icon.png")

        self.header_label1 = ttk.Label(self.f1, image=self.appicon)
        self.header_label1.pack(side='right')

        self.header_label2 = ttk.Label(self.f1, text="Summative Test Statistics", font=tkFont.nametofont("TkHeadingFont"), width=30)
        self.header_label2.pack(side='left')

        self.sub_label = ttk.Label(self, text="Select a Summative test below to view statistics...")
        self.sub_label.grid(row=1, column=0, padx=(30,0), pady=(0, 10), sticky='W')



        self.testlist = [x[0] for x in read_csv('data/tests.csv')[1:] if get_test_type(int(x[0])) == 'Summative']

        


        self.f2 = tk.Frame(self, bg='white')
        self.f2.grid(row=2, column=0, columnspan=2, sticky="NSEW")

        self.test_combo = ttk.Combobox(self.f2, state="readonly", values=self.testlist)
        self.test_combo.grid(row=0, column=0, padx=(30, 0), pady=(0, 20), sticky='WE')
        self.test_combo.bind("<<ComboboxSelected>>", self.load_stats)


        self.attempt_label1 = ttk.Label(self.f2, text="—", font=tkFont.nametofont("TkHeadingFont"))
        self.attempt_label1.grid(row=1, column=0, padx=(30, 0), sticky='WE')



        self.mark_label1 = ttk.Label(self.f2, text="—", font=tkFont.nametofont("TkHeadingFont"))
        self.mark_label1.grid(row=3, column=0, padx=(30, 0), sticky='WE')

        self.mark_label2 = ttk.Label(self.f2, text="Average Mark")
        self.mark_label2.grid(row=4, column=0, padx=(30, 0), sticky='WE')



        self.f3 = tk.Frame(self.f2, bg='white')
        self.f3.grid(row=1, column=1, rowspan=5, sticky="NSEW")

        self.average_label = ttk.Label(self.f3, text="Average mark per question:")
        self.average_label.grid(row=0, column=0, columnspan=2, padx=(30, 0), pady=(0, 5), sticky='W')
        
        self.q1_label = ttk.Label(self.f3, text="Question 1:")
        self.q1_label.grid(row=1, column=0, padx=(30, 0), sticky='W')

        self.q2_label = ttk.Label(self.f3, text="Question 2:")
        self.q2_label.grid(row=2, column=0, padx=(30, 0), sticky='W')

        self.q3_label = ttk.Label(self.f3, text="Question 3:")
        self.q3_label.grid(row=3, column=0, padx=(30, 0), sticky='W')

        self.q4_label = ttk.Label(self.f3, text="Question 4:")
        self.q4_label.grid(row=4, column=0, padx=(30, 0), sticky='W')

        self.q5_label = ttk.Label(self.f3, text="Question 5:")
        self.q5_label.grid(row=5, column=0, padx=(30, 0), sticky='W')

        self.q6_label = ttk.Label(self.f3, text="Question 6:")
        self.q6_label.grid(row=6, column=0, padx=(30, 0), sticky='W')

        self.q7_label = ttk.Label(self.f3, text="Question 7:")
        self.q7_label.grid(row=7, column=0, padx=(30, 0), sticky='W')

        self.q8_label = ttk.Label(self.f3, text="Question 8:")
        self.q8_label.grid(row=8, column=0, padx=(30, 0), sticky='W')

        self.q9_label = ttk.Label(self.f3, text="Question 9:")
        self.q9_label.grid(row=9, column=0, padx=(30, 0), sticky='W')

        self.q10_label = ttk.Label(self.f3, text="Question 10:")
        self.q10_label.grid(row=10, column=0, padx=(30, 0), sticky='W')



        self.q1 = tk.StringVar() 
        self.q2 = tk.StringVar()
        self.q3 = tk.StringVar()
        self.q4 = tk.StringVar()
        self.q5 = tk.StringVar()
        self.q6 = tk.StringVar()
        self.q7 = tk.StringVar()
        self.q8 = tk.StringVar()
        self.q9 = tk.StringVar()
        self.q10 = tk.StringVar()
        
        self.clear_display()
        
        
        self.q1_mark = ttk.Label(self.f3, textvariable=self.q1)
        self.q1_mark.grid(row=1, column=1, padx=(15, 0), sticky='W')

        self.q2_mark = ttk.Label(self.f3, textvariable=self.q2)
        self.q2_mark.grid(row=2, column=1, padx=(15, 0), sticky='W')

        self.q3_mark = ttk.Label(self.f3, textvariable=self.q3)
        self.q3_mark.grid(row=3, column=1, padx=(15, 0), sticky='W')

        self.q4_mark = ttk.Label(self.f3, textvariable=self.q4)
        self.q4_mark.grid(row=4, column=1, padx=(15, 0), sticky='W')

        self.q5_mark = ttk.Label(self.f3, textvariable=self.q5)
        self.q5_mark.grid(row=5, column=1, padx=(15, 0), sticky='W')

        self.q6_mark = ttk.Label(self.f3, textvariable=self.q6)
        self.q6_mark.grid(row=6, column=1, padx=(15, 0), sticky='W')

        self.q7_mark = ttk.Label(self.f3, textvariable=self.q7)
        self.q7_mark.grid(row=7, column=1, padx=(15, 0), sticky='W')

        self.q8_mark = ttk.Label(self.f3, textvariable=self.q8)
        self.q8_mark.grid(row=8, column=1, padx=(15, 0), sticky='W')

        self.q9_mark = ttk.Label(self.f3, textvariable=self.q9)
        self.q9_mark.grid(row=9, column=1, padx=(15, 0), sticky='W')

        self.q10_mark = ttk.Label(self.f3, textvariable=self.q10)
        self.q10_mark.grid(row=10, column=1, padx=(15, 0), sticky='W')



        if len(self.testlist) == 0 : 
            msg.showerror("No Summative Tests", "There are no Summative tests to show.\nClick on 'Create New Test' to create one.")

            

        self.focus_force()

        

    def load_stats(self, event) :
        self.clear_display()
        
        selected_test = self.test_combo.get()
        responses = []
        correct = []
        question_marks = []


        student_ids= []
        try :
            with open('data/test' + selected_test + '.csv') as csvfile:
                rdr = csv.reader(csvfile)
            
                for count, row in enumerate(rdr) :
            
                    if count != 0 : # skip header of CSV
                        responses += [[int(x) for x in row[1:] if x]]  # get non-empty integer values
                        student_ids.append(row[0])


            if len(responses) == 0 :
                raise TypeError("Nobody has taken this test yet.")


            self.attempt_label1['text'] = str(len(responses))

            correct = get_correct_answers(selected_test)



            for count, question in enumerate(correct) :

                student_answers = [i[count] for i in responses]
                correct_answer = correct[count]


                matches = [i for i in student_answers if correct_answer == i]

                percent = round((len(matches)/len(student_answers))*100, 2)

                
                question_marks += [percent]
                



            max_question, min_question = 0, 0
            
            if len(question_marks) >= 2 :
                max_question = question_marks.index(max(question_marks)) + 1
                min_question = question_marks.index(min(question_marks)) + 1

            

            for count, mark in enumerate(question_marks) :
                if max_question == min_question :   
                    self.set_variables(count + 1, str(mark) + "%")

                elif max_question == count + 1 :
                    self.set_variables(count + 1, str(mark) + "%\tHighest")

                elif min_question == count + 1 :
                    self.set_variables(count + 1, str(mark) + "%\tLowest")

                else :
                    self.set_variables(count + 1, str(mark) + "%")

        
            self.mark_label1['text'] = str(round(sum(question_marks) / len(question_marks), 2)) + "%"
            
            with open('data/test' + selected_test + '.csv') as file:
                reader = csv.reader(file)
                self = tkinter.Tk()#
                self.title("Performance")
                self.resizable(False,False)
                self.configure(background="#ffffff")
                self.iconbitmap('images/app_icon.ico')

                r = 0
                for col in reader:
                    c = 0
                    for row in col:

                        label = tkinter.Label(self, width = 10, height = 2, \
                                          text = row, relief = tkinter.RIDGE)
                        label.grid(row = r, column = c)
                        c += 1
                    r += 1
        

        except TypeError as e :
            msg.showerror("Error", e)
        except :
            msg.showerror("Error", "A critical error occurred when retrieving data for this particular test.\nPlease try again.")
        

    def clear_display(self) :
        self.attempt_label1['text'] = "—"
        self.mark_label1['text'] = "—"
        
        self.q1.set("—")
        self.q2.set("—")
        self.q3.set("—")
        self.q4.set("—")
        self.q5.set("—")
        self.q6.set("—")
        self.q7.set("—")
        self.q8.set("—")
        self.q9.set("—")
        self.q10.set("—")


    def set_variables(self, question, text) :
        if question == 1 :
            self.q1.set(text)
        elif question == 2 :
            self.q2.set(text)
        elif question == 3 :
            self.q3.set(text)
        elif question == 4 :
            self.q4.set(text)
        elif question == 5 :
            self.q5.set(text)
        elif question == 6 :
            self.q6.set(text)
        elif question == 7 :
            self.q7.set(text)
        elif question == 8 :
            self.q8.set(text)
        elif question == 9 :
            self.q9.set(text)
        elif question == 10 :
            self.q10.set(text)


if __name__ == "__main__":
    performance = Performance()
    performance.mainloop()

