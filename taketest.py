# Reddy Valluru

from tkinter import *
import tkinter.messagebox
from functions import *
import csv

class Quiz(tkinter.Toplevel):
    
    def __init__(self, parent, testid, studentid):
        super().__init__()

        self.title("Short Assessment System - Team 8")
        self.geometry("550x300")
        self.resizable(False, False)
        self.configure(background="#ffffff")

        test =get_test_questions(int(testid))

        

        self.q = []
        self.options = []
        self.a = []
        for items in test:
            self.q.append(items[0])
            del items[0]
            self.options.append(items)
            for element in items:
                if element.startswith("*") :
                    self.a.append(element)
        for count1, i in enumerate(self.options) :
            for count2, element in enumerate(i):
                self.options[count1][count2] = self.options[count1][count2].replace("*", "")
        for count3, i in enumerate(self.a) :
            self.a[count3]= self.a[count3].replace("*", "")

        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(self.qn)
        self.opts = self.create_options(5)
        self.display_q(self.qn)
        self.status_bar = self.create_status_bar()
        self.create_nav()
        self.list=[]
        self.testid=testid
        self.studentid=studentid

    def create_status_bar(self):
        status_bar = Label(self, text="Click To Answer", bd=1, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
        return status_bar

    def create_nav(self):
        self.button = Button(self, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(self, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, qn):
        w = Label(self, text=self.q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(self, text="foo", variable=self.opt_selected, value=b_val + 1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = self.q[qn]
        for op in self.options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def displayo_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = self.q[qn]
        for op in self.options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1
            
    def check_q(self, qn):

        if self.opt_selected.get() == (self.options[qn].index(self.a[qn]))+1:
            return True
        else:
            return False


    def print_results(self):
        results="Score: ", self.correct, "/", len(self.q)
        Percentage="Percentage: ", (self.correct * 100) / len(self.q), "%"
        tkinter.messagebox.showinfo("Final Result", results)

    def back_btn(self):

        if self.correct > 0:
            self.correct -= 1
        else:
            print("")
        self.qn = self.qn - 1

        if self.qn >= len(self.q):
            self.print_results()
        else:
            self.display_q(self.qn)

    def next_btn(self):
        self.list.append(self.opt_selected.get())
        if self.check_q(self.qn):
            self.status_bar['text'] = "...."
            self.correct += 1
        else:
            self.status_bar['text'] = "...."
        self.qn = self.qn + 1

        if self.qn >= len(self.q):
            self.print_results()
            #print(self.opt_selected.get())
            save_response(self.testid, self.studentid, self.list)
            print(self.list)
            self.destroy()
        else:
            self.display_q(self.qn)
            self.displayo_q(self.qn)




if __name__ == "__main__":
    quiz = Quiz()
    quiz.mainloop()
