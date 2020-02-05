import tkinter as tk
from tkinter.filedialog import askopenfilename
#from tkinter import *
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
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
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
    
    root = tk.Tk()
    root.title("PadPlot_PCA v1.0")
    tk.Label(root, text='File Path').grid(row=0, column=0)
    v = tk.StringVar()
    entry = tk.Entry(root, textvariable=v).grid(row=0, column=3)
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
    
    tk.Label(root,text="Define the number of groups:").grid(row=21,padx=10, pady=10,sticky='E')
    
    
    MODES = [
        ("Two", "2"),
        ("Three", "3"),
        ("Four", "4")
    ]

    k = tk.IntVar()
    k.set("2") # initialize

    for text, mode in MODES:
        c = tk.Radiobutton(root, text=text,variable=k, value=mode)
        c.grid(sticky=tk.W,column=3)

    tk.Button(root, text='Proceed to Labelling of Group 1',command=root.destroy).grid(row=27, column=0)  

    root.mainloop()
    
    df= pd.read_csv(csv_file_path)
    headers= list(df.columns.values)
    
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
    
def group_selection_three():
    global group_2
    global g_3
    group_2 = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            group_2[ix]=(cb_v[ix].get())
    
    root = tk.Tk() 
    
    tk.Label(root, text='Please select any column name which contains the data for your "Group3"').grid(row=0, column=0)  
    
    g_3 = tk.StringVar()
    tk.Label(root, text='Title for Group_3: ').grid(row=4, column=0, pady=10,padx=10)    
    entry = tk.Entry(root, textvariable=g_3).grid(row=5, column=0)
    
    tk.Button(root, text='Proceed to Plot/ Group 4',command=root.destroy).grid(row=7, column=0)
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        cb[ix].grid(row=ix, column=3, sticky='w')
        group_2.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    group_2 = [i for i in group_2 if i != "0"]
    
def group_selection_four():
    global group_3
    global g_4
    group_3 = []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            group_3[ix]=(cb_v[ix].get())
    
    root = tk.Tk() 
    
    tk.Label(root, text='Please select any column name which contains the data for your "Group4"').grid(row=0, column=0)  

    g_4 = tk.StringVar()
    tk.Label(root, text='Title for Group_4: ').grid(row=4, column=0, pady=10,padx=10)    
    entry = tk.Entry(root, textvariable=g_4).grid(row=5, column=0)
    
    tk.Button(root, text='Proceed to Plot',command=root.destroy).grid(row=5, column=0)
    
    cb = []
    cb_v = []
    for ix, text in enumerate(headers):
        cb_v.append(tk.StringVar())
        off_value=0
        cb.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v[ix],
                             command=chkbox_checked))
        cb[ix].grid(row=ix, column=3, sticky='w')
        group_3.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    group_3 = [i for i in group_3 if i != "0"]
    
def process_data():
    global principaldf
    global pc1
    global pc2
    if num_groups==3:
        pca_df=df[control_group+group_1+group_2]
    elif num_groups==4:
        pca_df=df[control_group+group_1+group_2+group_3]
    else:
        pca_df=df[control_group+group_1]
        
    genes=len(pca_df)
    pca_df=pca_df.transpose()
    pca_df['Sample']=pca_df.index

    gp1=str(g_1.get())
    g1= [gp1]
    g1=g1* len(control_group)
    gp2=str(g_2.get())
    g2= [gp2]
    g2=g2*len(group_1)
    if num_groups==3:
        gp3=str(g_3.get())
        g3= [gp3]
        g3=g3*len(group_2)
        grouping= g1+g2+g3
    elif num_groups==4:
        gp3=str(g_3.get())
        g3= [gp3]
        g3=g3*len(group_2)
        gp4=str(g_4.get())
        g4= [gp4]
        g4=g4*len(group_3)
        grouping= g1+g2+g3+g4
    else:
        grouping=g1+g2

    pca_df['Group']= grouping
    pca_df


    features = range(0,genes,1)
    x=pca_df.loc[:,features].values
    y=pca_df.loc[:,['Sample']].values
    x=StandardScaler().fit_transform(x)

    pca=PCA(n_components=2)
    principalComponents=pca.fit_transform(x)
    ex_variance=np.var(principalComponents,axis=0)
    ex_variance_ratio=ex_variance/np.sum(ex_variance)
    pc1=round((ex_variance_ratio[0] * 100), 1)
    pc2=round((ex_variance_ratio[1] * 100), 1)
    pc2

    principaldf=pd.DataFrame(data=principalComponents,columns=['PC1 ' + '(' + str(pc1) + '% of variance' + ' )','PC2 ' + '(' + str(pc2) + '% of variance' + ' )'])#,raise_missing=False)
    principaldf['Sample']=pca_df.index
    principaldf['Group']= grouping
    principaldf

def plot():
    global ax
    #size=int(k.get())
    
    ax = figure.subplots()
    sns.scatterplot(data= principaldf,x= 'PC1 ' + '(' + str(pc1) + '% of variance' + ' )',y= 'PC2 ' + '(' + str(pc2) + '% of variance' + ' )', ax=ax,s=150, hue='Group' )
    ax.set_title(title) 
    ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
    ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')


def create_figure() -> Figure:
    global figure
    figure = Figure(figsize=(8, 8))
           
    plot()
    
    return figure
      
def init_gui(root, update_function: Callable) -> FigureCanvasTkAgg:
    def event_key_press(event):
        print("you pressed {}".format(event.key))
        update_function()
        key_press_handler(event, canvas)
    global init_figure
    # create empty figure and draw
    init_figure = create_figure()
    canvas = FigureCanvasTkAgg(init_figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # call key press event
    canvas.mpl_connect("key_press_event", event_key_press)
    
    '''
    canvas.pack(anchor=tk.NW)
    button = tk.Button(text="button")
    button.pack(side=tk.RIGHT, anchor=tk.SE)
    '''
    return init_figure
    return canvas

def redraw_figure():

    Figure = create_figure()
    canvas.figure = Figure
    canvas.draw()
    
def save_fig():
    x=figure
    x.savefig(path+ '/' + title + '_padplot_PCA.svg', format='svg', dpi=1200)
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
get_title()
group_selection_one()
group_selection_two()
global num_groups
num_groups=int(k.get())
if num_groups==3:
    group_selection_three()
    process_data()
elif num_groups==4:
    group_selection_three()
    group_selection_four()
    process_data()       
else:
    process_data()


sns.set_style("white")

root = tk.Tk()
root.title("PadPlot_PCA v1.0")
canvas = init_gui(root, update_function=redraw_figure)

button = tk.Button(root, text="Proceed to file options",command=root.destroy)
button.pack()

root.mainloop() 


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