from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root=Tk()
canvas = Canvas(root)
canvas.config(width=500,height=700,relief=RIDGE)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

f1 = Frame(canvas)
canvas.create_window(0, 0, anchor='s', window=f1)

def refresh():
    
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'), 
                     yscrollcommand=scroll_y.set)
                 
    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')


Label =ttk.Label(f1,text="Enter (File Path\File Name.xls)")
Label.pack()


Fname=ttk.Entry(f1,width=40)
Fname.pack()



b_pass=ttk.Button(f1,text="Import Data")
b_pass.pack()

Labe2 =ttk.Label(f1,text="Enter Column Name")
Labe2.pack()


Fcol=ttk.Entry(f1,width=30)
Fcol.pack()

b_col=ttk.Button(f1,text="Ok")
b_col.pack()

Labe3 =ttk.Label(f1,text="Choose your Option ! ")
Labe3.pack()

Mean=ttk.Entry(f1,width=25)
Mean.pack()

b_mean=ttk.Button(f1,text="Mean")
b_mean.pack()

Mediam=ttk.Entry(f1,width=25)
Mediam.pack()

b_median=ttk.Button(f1,text="Median")
b_median.pack()

Mode=ttk.Entry(f1,width=25)
Mode.pack()

b_mode=ttk.Button(f1,text="Mode")
b_mode.pack()

b_photo1=ttk.Button(f1,text="Skew")
b_photo1.pack()

#Labe4 =ttk.Label(f1,text="Choose your Option ( Graph Or Skew )! ")
#Labe4.pack()



Labe5 =ttk.Label(f1,text="Enter Columns Names To Find Relation Between Them")
Labe5.pack()

Labe6 =ttk.Label(f1,text="X-Axis")
Labe6.pack()

xaxis=ttk.Entry(f1,width=25)
xaxis.pack()

Labe7 =ttk.Label(f1,text="Y-Axis")
Labe7.pack()

yaxis=ttk.Entry(f1,width=25)
yaxis.pack()


b_photo=ttk.Button(f1,text="Graph")
b_photo.pack()

#a=PhotoImage(file='a.jpg')
#b_photo.config(image=a,componenet=LEFT)
def readFromExcel():
    df = pd.read_excel(Fname.get())
    print(df)
b_pass.config(command=readFromExcel)

def EnteredColumn():
    df = pd.read_excel(Fname.get())
    ax = sns.distplot(df[Fcol.get()], fit=norm, kde=False)
    fig = ax.get_figure()
    fig.savefig("output2.png")
    plt.clf()
b_col.config(command=EnteredColumn)    
    
def mean():
    df = pd.read_excel(Fname.get())
    Mean.delete(0, END)
    avg = df[Fcol.get()].mean()
    Mean.insert(0, avg)
b_mean.config(command=mean)



def median():
    df = pd.read_excel(Fname.get())
    Mediam.delete(0,END)
    med = df[Fcol.get()].median()
    Mediam.insert(0,med)
b_median.config(command=median)



def mode():
    df = pd.read_excel(Fname.get())
    Mode.delete(0, END)
    for mod in df[Fcol.get()].mode():
      Mode.insert(0, mod)
      Mode.insert(0, " ")
b_mode.config(command=mode)

Labe8 = ttk.Label(f1, text="The Graph ")
pic=ttk.Button(f1,text='Gragh_pic')
def graph(): 
    df = pd.read_excel(Fname.get())
    sns.set(style="whitegrid", color_codes=True)
    sns_plot = sns.barplot(x = xaxis.get(), y = yaxis.get(), data=df)
    plt.xticks(rotation = 90)
    plt.tight_layout()
    fig = sns_plot.get_figure()
    fig.savefig("output.png")
    plt.clf()
    root.photo = PhotoImage(file='output.png')
    Labe8.pack()
    pic.config(image=root.photo, compound=CENTER)
    pic.pack()
    refresh()
    
b_photo.config(command=graph)



Labe9 = ttk.Label(f1, text='The Skewness of the Column you entered is')
pic1 = ttk.Button(f1, text='Skew_pic')
def skew():
    df = pd.read_excel(Fname.get())
    ax = sns.distplot(df[Fcol.get()], fit=norm, kde=False)
    fig = ax.get_figure()
    fig.savefig("output2.png") 
    plt.clf()
    root.photo2 = PhotoImage(file='output2.png')
    Labe9.pack()
    pic1.config(image=root.photo2, compound=CENTER)
    pic1.pack()
    refresh()
b_photo1.config(command=skew)

refresh()
root.mainloop()


