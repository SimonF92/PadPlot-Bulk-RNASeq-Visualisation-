?import tkinter as tk
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
    global y
    
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    
def debug_options():
    root = tk.Tk()
    root.title("PadPlot_Debug v1.0")
    #tk.Label(root, text="Padplot cannot function unless given an appropriare file. Common errors include").grid(row=0, column=0, padx=10, pady=10,sticky='w')
    tk.Label(root, text="Please ensure the following requirements are met:").grid(row=1, column=0, padx=10, pady=1,sticky='w')
    tk.Label(root, text="1) The file is a .csv and not a .xls file").grid(row=2, column=0, padx=10,sticky='w')
    tk.Label(root, text="2) The top row of the .csv file consists of column names").grid(row=3, column=0, padx=10,sticky='w')
    tk.Label(root, text="3) The .csv file consists only of columns").grid(row=4, column=0, padx=10,sticky='w')


    root.mainloop()   
    
def exitout():
    root.destroy()
    sys.exit()
    
      
def plot_options(): 
    global v
    global df
    global headers
    global k
    global pvalue
    global val
    global b
    global h
    global colo
    global text
    global root

    
    root = tk.Tk()
    val = tk.DoubleVar()
    root.title("PadPlot_Heatmap v1.0")
    tk.Label(root, text='File Path:').grid(row=0, column=1,padx=10, pady=10,sticky='e')
    


    v = tk.StringVar()
    

    
    #entry = tk.Entry(root, textvariable=v).grid(row=0, column=2,sticky='w')
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=0, column=2,sticky='w')
        

    
    tk.Label(root,text="p-cutoff (higher means less genes on plot):").grid(row=21,column=1,padx=10, pady=10,sticky='e')
    
    w = tk.Scale(root, variable=val, from_=1, to=10,orient=tk.HORIZONTAL, resolution=0.5).grid(row=21,column=2,sticky='w')
    
    tk.Label(root,text="Define the colour of your Heatmap:").grid(row=25,column=1,padx=10, pady=10,sticky='e')
    
    
    
    MODES = {
        "Yellow, Orange and Red":"YlOrRd",
        "Orange and Red":"OrRd",
        "Purple and Red":"PuRd",
        "Red and Purple":"RdPu",
        "Hot":"hot",
        "Standard": "gist_heat",
    }
 

    def boxtext(new_value):
        global colo
        #display.config(text = MODES[new_value])
        colo=MODES[new_value]
        
    var = tk.StringVar()
    var.set("Standard") # initialize
    #create a dropdown list
    

    p = tk.OptionMenu(root, var, *MODES, command=boxtext).grid(row=25,column=2,columnspan=2,sticky='w')
    
    #display= tk.Label(root)
    #display.grid(row=25,column=3)

    b = tk.StringVar()
    tk.Label(root, text='Assign plot title (or Padplot will automatically detect): ').grid(row=32, column=1, padx=10, pady=10,sticky="w")
    entry = tk.Entry(root, textvariable=b).grid(row=32, column=2, padx=10, pady=10,sticky='w')

    tk.Button(root, text='Proceed to Labelling of Group 1',command=root.destroy).grid(row=34, column=2, padx=10, pady=10, sticky='e')
    
    tk.Button(root, text='Debug Options',command=debug_options).grid(row=34, column=1, padx=10, pady=10, sticky='w')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=35, column=1, padx=10, pady=10, sticky='w')
    #return cancel

    root.mainloop()
    
    df= pd.read_csv(csv_file_path)
    headers= list(df.columns.values)
    



def gene_names_selection():
    global gene_names
    global g_1
    global root
    
    gene_names = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            gene_names[ix]=(cb_v[ix].get())
    
    root = tk.Tk()
    root.title("PadPlot_Heatmap v1.0")
    
    tk.Label(root, text='Please select the column name which contains the Gene names [one column only]').grid(row=0, column=0, columnspan=4)  
    
    tk.Button(root, text='Proceed to Labelling of Group1',command=root.destroy).grid(row=7, column=3, columnspan=3,pady=10, padx=10, sticky='e')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=9, column=0, padx=10, pady=10, sticky='w')
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb[ix].grid(row=(ix+1), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb[ix].grid(row=(ix-4), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb[ix].grid(row=(ix-9), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb[ix].grid(row=(ix-14), column=3, sticky='w')
        else:
            cb[ix].grid(row=(ix-19), column=4, sticky='w')
        gene_names.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    gene_names = [i for i in gene_names if i != "0"]    
    
    
def group_selection_one():
    global control_group
    global g_1
    global root
    control_group = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            control_group[ix]=(cb_v[ix].get())
    
    root = tk.Tk()
    root.title("PadPlot_Heatmap v1.0")
    
    tk.Label(root, text='Please select any column name which contains the data for your "Group1"').grid(row=0, column=0,columnspan=3)  

    g_1 = tk.StringVar()
    tk.Label(root, text='Title for Group_1: ').grid(row=16, column=0, pady=10,padx=10,sticky='e')    
    entry = tk.Entry(root, textvariable=g_1).grid(row=16, column=1,sticky='w')
    
    tk.Button(root, text='Proceed to Labelling of Group2',command=root.destroy).grid(row=19, column=3,columnspan=3,pady=10, padx=10)
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=20, column=0, padx=10, pady=10, sticky='w')
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb[ix].grid(row=(ix+1), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb[ix].grid(row=(ix-4), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb[ix].grid(row=(ix-9), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb[ix].grid(row=(ix-14), column=3, sticky='w')
        else:
            cb[ix].grid(row=(ix-19), column=4, sticky='w')
        control_group.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    control_group = [i for i in control_group if i != "0"]
    

    
def group_selection_two():
    global group_1
    global g_2
    global root
    group_1 = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            group_1[ix]=(cb_v[ix].get())
    
    root = tk.Tk() 
    root.title("PadPlot_Heatmap v1.0")
    
    tk.Label(root, text='Please select any column name which contains the data for your "Group2"').grid(row=0, column=0,columnspan=3)  

    g_2 = tk.StringVar()
    tk.Label(root, text='Title for Group_2: ').grid(row=16, column=0, pady=10,padx=10,sticky='e')    
    entry = tk.Entry(root, textvariable=g_2).grid(row=16, column=1,sticky='w')
    
   
    tk.Button(root, text='Proceed to Plot',command=root.destroy).grid(row=19, column=3, columnspan=3,pady=10, padx=10)
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=20, column=0, padx=10, pady=10, sticky='w')
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb[ix].grid(row=(ix+1), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb[ix].grid(row=(ix-4), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb[ix].grid(row=(ix-9), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb[ix].grid(row=(ix-14), column=3, sticky='w')
        else:
            cb[ix].grid(row=(ix-19), column=4, sticky='w')
        group_1.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
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






    
plot_options()





p_cutoff= float(val.get())

gene_names_selection()
group_selection_one()
group_selection_two()
process_data()

p_cutoff= float(val.get())
p_cutoff
pvalue=0.05**(p_cutoff)
pvalue

colour=colo


lengthy= temp[temp['padj'] < pvalue]
length=lengthy.shape[0]
counts=length/len(samples)


if counts < 20:
    sns.set(font_scale=1.2)

elif counts > 20 and counts < 30:
    sns.set(font_scale=1)

elif counts > 30 and counts < 40:
    sns.set(font_scale=0.85)

elif counts > 40 and counts <50:
    sns.set(font_scale=0.7)

else:
    sns.set(font_scale=1.2)



#sns.set_style("white")
def save_fig():
    global path
    path= csv_file_path.split('/')
    strip=len(path)-1
    path = path[:strip]
    path= '/'.join(path)
    path
    x=figure
    x.savefig(path+ '/' + title + '_padplot_Heatmap.svg', format='svg', dpi=1200)
    root.destroy()
    return path


root = tk.Tk()
root.title("PadPlot_Heatmap v1.0")


#root.geometry("1000x1000") 
button = tk.Button(root, text="Cancel",command=root.destroy)
button.pack(side=tk.LEFT, padx=20, pady=20)
button2 = tk.Button(root, text="Save Figure to Parent Directory",command=save_fig)
button2.pack(side=tk.RIGHT, padx=20, pady=20)

figure = create_plot()
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.draw()
canvas.get_tk_widget().pack()


tk.mainloop()

csv_file_path.rstrip('/')

root = tk.Tk()
root.title("PadPlot_Heatmap v1.0")
tk.Label(root, text="If requested, figure was saved to \n \n " + path + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)


root.mainloop()


      
