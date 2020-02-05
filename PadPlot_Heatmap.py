import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import subprocess
import webbrowser
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import adjustText
from adjustText import adjust_text
import seaborn as sns; sns.set_style("white")
import matplotlib.image as mpimg
from matplotlib.figure import Figure
import typing
from typing import Callable
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
import seaborn as sns

def doNothing():
    print("nothing")
    
def get_title():
    global title
    y = csv_file_path.split('/')
    y = y[-1]
    title = y.rstrip('.csv')
    print(title)
    
def import_csv_data():
    global v
    global csv_file_path
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)

def plot_options(): 
    global v
    global df
    global headers
    global k
    global pvalue
    global var
    global b
    
    root = tk.Tk()
    var = tk.DoubleVar()
    root.title("PadPlot_Heatmap v1.0")
    tk.Label(root, text='File Path').grid(row=0, column=0)
    v = tk.StringVar()
    entry = tk.Entry(root, textvariable=v).grid(row=0, column=3)
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
    
    tk.Label(root,text="Define the negative power exponent of p-value \n (increasing exponent means less genes):").grid(row=21,padx=10, pady=10,sticky='E')
    
    w = tk.Scale(root, variable=var, from_=1, to=10,resolution=0.5).grid(row=22)
    
    tk.Label(root,text="Define the colour of your Heatmap:").grid(row=25,padx=10, pady=10,sticky='E')
    
    
    'YlOrRd', 'OrRd', 'PuRd', 'RdPu',
    
    MODES = [
        ("Yellow, Orange and Red", "YlOrRd"),
        ("Orange and Red", "OrRd"),
        ("Purple and Red", "PuRd"),
        ("Red and Purple", "RdPu"),
        ("Hot", "hot"),
        ("Standard", "gist_heat"),
    ]

    k = tk.StringVar()
    k.set("gist_heat") # initialize

    for text, mode in MODES:
        c = tk.Radiobutton(root, text=text,variable=k, value=mode)
        c.grid(sticky=tk.W,column=3)
        
    b = tk.StringVar()
    tk.Label(root, text='Assign plot title (or Padplot will automatically detect): ').grid(row=32, column=0, padx=10, pady=10,sticky="E")
    entry = tk.Entry(root, textvariable=b).grid(row=32, column=3, padx=10, pady=10)

    tk.Button(root, text='Proceed to Labelling of Group 1',command=root.destroy).grid(row=34, column=0)  

    root.mainloop()
    
    df= pd.read_csv(csv_file_path)
    headers= list(df.columns.values)


def gene_names_selection():
    global gene_names
    global g_1
    gene_names = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            gene_names[ix]=(cb_v[ix].get())
    
    root = tk.Tk() 
    
    tk.Label(root, text='Please select the column name which contains the Gene names [one column only]').grid(row=0, column=0)  
    
    tk.Button(root, text='Proceed to Labelling of Group1',command=root.destroy).grid(row=7, column=0,pady=10, padx=10)
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        cb[ix].grid(row=ix, column=3, sticky='w')
        gene_names.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    gene_names = [i for i in gene_names if i != "0"]    
    
    
def group_selection_one():
    global control_group
    global g_1
    control_group = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            control_group[ix]=(cb_v[ix].get())
    
    root = tk.Tk() 
    
    tk.Label(root, text='Please select any column name which contains the data for your "Group1"').grid(row=0, column=0)  

    g_1 = tk.StringVar()
    tk.Label(root, text='Title for Group_1: ').grid(row=4, column=0, pady=10,padx=10)    
    entry = tk.Entry(root, textvariable=g_1).grid(row=5, column=0)
    
    tk.Button(root, text='Proceed to Labelling of Group2',command=root.destroy).grid(row=7, column=0,pady=10, padx=10)
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        cb[ix].grid(row=ix, column=3, sticky='w')
        control_group.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    control_group = [i for i in control_group if i != "0"]
    

    
def group_selection_two():
    global group_1
    global g_2
    group_1 = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            group_1[ix]=(cb_v[ix].get())
    
    root = tk.Tk() 
    
    tk.Label(root, text='Please select any column name which contains the data for your "Group2"').grid(row=0, column=0)  

    g_2 = tk.StringVar()
    tk.Label(root, text='Title for Group_2: ').grid(row=4, column=0, pady=10,padx=10)    
    entry = tk.Entry(root, textvariable=g_2).grid(row=5, column=0)
    
   
    tk.Button(root, text='Proceed to Plot/ Group 3',command=root.destroy).grid(row=7, column=0)
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        cb[ix].grid(row=ix, column=3, sticky='w')
        group_1.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    group_1 = [i for i in group_1 if i != "0"]
    
def process_data():
    global temp
    global gene
    global title
    global samples
    
    samples=control_group+group_1
    cols = [x for x in headers if x not in samples]
    
    gp1=str(g_1.get())
    gp2=str(g_2.get())

    g1= [gp1]
    g2= [gp2]

    grouping= (g1 * len(control_group)) + (g2 * len(group_1))
    
    temp = (
    #remember we made headers and cols earlier, these are variables
    df[headers]
    .melt(id_vars = cols, 
         var_name = 'Sample',
          value_name = 'Expression'
         )
    
    )

    low_samples = control_group


    temp['Group'] = temp['Sample'].apply(lambda x : gp1 if x in low_samples else gp2)
    temp.head()


    gene=gene_names[0]
    gene
    
    custom_title= str(b.get())
    if len(custom_title) < 1:
        get_title()
    else:
        title=custom_title
    
def create_plot(): 
    
    
    if counts < 50:
        g = sns.clustermap(temp[temp['padj'] < pvalue].groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap=colour,metric = 'correlation',z_score=0) 
    #g.set_title(title)
    else:
        g = sns.clustermap(temp[temp['padj'] < pvalue].groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap=colour,metric = 'correlation',z_score=0,yticklabels=False)
    
    return g.fig

def save_fig():
    x=figure
    x.savefig(path+ '/' + title + '_padplot_Heatmap.svg', format='svg', dpi=1200)
    root.destroy()

def exit_gui():
    root = tk.Tk()
    root.title("PadPlot v2.0")
    w = tk.Label(root, text="Hello, world!")
    w.pack
    
    root.mainloop
    
def get_path_for_svg():
    global path
    path= csv_file_path.split('/')
    strip=len(path)-1
    path = path[:strip]
    path= '/'.join(path)
    path


    
plot_options()

p_cutoff= float(var.get())

gene_names_selection()
group_selection_one()
group_selection_two()
process_data()

p_cutoff= float(var.get())
p_cutoff
pvalue=0.05**(p_cutoff)
pvalue

colour=str(k.get())


lengthy= temp[temp['padj'] < pvalue]
length=lengthy.shape[0]
counts=length/len(samples)


if counts < 20:
    sns.set(font_scale=1.2)
    
elif counts > 20 and counts < 30:
    sns.set(font_scale=1)
    
elif counts > 30 and counts < 40:
    sns.set(font_scale=0.8)

elif counts > 40 and counts <50:
    sns.set(font_scale=0.5)
    
else:
    sns.set(font_scale=1.2)



#sns.set_style("white")

root = tk.Tk()
figure = create_plot()
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

button = tk.Button(root, text="Proceed to file options",command=root.destroy)
button.pack()

tk.mainloop()


get_path_for_svg()


root=tk.Tk()

tk.Button(root, text='Looks good, save my Figure',command=save_fig).grid(row=1, column=0, padx=50, pady=50)
tk.Button(root, text='Make changes',command=root.destroy).grid(row=1, column=1, padx=50, pady=50 )  

root.mainloop()



csv_file_path.rstrip('/')
root = tk.Tk()
root.title("PadPlot_Volcano v2.0")
tk.Label(root, text="If requested, figure was saved to \n \n " + path + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)

    
root.mainloop()