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
    global s 
    
    root = tk.Tk()
    val = tk.DoubleVar()
    root.title("PadPlot_PCA v1.8")
    tk.Label(root, text='File Path:').grid(row=0, column=1,padx=10, pady=10,sticky='e')
    


    v = tk.StringVar()
    

    
    #entry = tk.Entry(root, textvariable=v).grid(row=0, column=2,sticky='w')
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=0, column=2,sticky='w')
        

    
    tk.Label(root,text="Define the number of groups:").grid(column=1,row=21,padx=10, pady=10,sticky='E')
    
    
    MODES = [
        ("Two", "2"),
        ("Three", "3"),
        ("Four", "4")
    ]

    k = tk.IntVar()
    k.set("2") # initialize

    for text, mode in MODES:
        c = tk.Radiobutton(root, text=text,variable=k, value=mode)
        c.grid(sticky=tk.W,column=2)
        
        
        
    tk.Label(root,text="Define plot type:").grid(column=1,row=30,padx=10, pady=10,sticky='E')
    
    
    
    STYLE = [
        ("Standard (Recommended)", "10"),
        ("Density (EXPERIMENTAL)", "20"),

    ]

    s = tk.IntVar()
    s.set("10") # initialize

    for thing, style in STYLE:
        b = tk.Radiobutton(root, text=thing,variable=s, value=style)
        b.grid(sticky=tk.W,column=2)
          

    tk.Button(root, text='Proceed to Labelling of Group 1',command=root.destroy).grid(row=34, column=2, padx=10, pady=10, sticky='e')
    
    tk.Button(root, text='Debug Options',command=debug_options).grid(row=34, column=1, padx=10, pady=10, sticky='w')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=35, column=1, padx=10, pady=10, sticky='w')
    #return cancel 

    root.mainloop()
    
    
    df= pd.read_csv(csv_file_path)
    headers= list(df.columns.values)

    
def group_selection_one():
    global control_group
    global g_1
    
    control_group = []
    
    def chkbox_checked():
        for ix, item in enumerate(cb2):
            control_group[ix]=(cb_v2[ix].get())
    
    root = tk.Tk() 
    root.title("PadPlot_PCA v1.8")
    tk.Label(root, text='Please select any column name which contains the data for your "Group1"').grid(row=0, column=0, columnspan=3)  

    g_1 = tk.StringVar()
    tk.Label(root, text='Title for Group_1: ').grid(row=25, column=0, pady=10,padx=10,sticky="e")    
    entry = tk.Entry(root, textvariable=g_1).grid(row=25, column=1,sticky="w")
    
    tk.Button(root, text='Proceed to Labelling of Group2',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)
    
    
    
    cb2 = []
    cb_v2= []
    for ix, text in enumerate(headers):
        cb_v2.append(tk.StringVar())
        off_value=0
        cb2.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v2[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb2[ix].grid(row=((ix+1)), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb2[ix].grid(row=((ix-4)), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb2[ix].grid(row=((ix-9)), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb2[ix].grid(row=((ix-14)), column=3, sticky='w')
        else:
            cb2[ix].grid(row=((ix-19)), column=4, sticky='w')
        control_group.append(off_value)
        cb2[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')   
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    control_group = [i for i in control_group if i != "0"]
    
    
def group_selection_two():
    global group_1
    global g_2
    
    group_1 = []
    
    def chkbox_checked():
        for ix, item in enumerate(cb2):
            group_1[ix]=(cb_v2[ix].get())
    
    root = tk.Tk() 
    root.title("PadPlot_PCA v1.8")
    tk.Label(root, text='Please select any column name which contains the data for your "Group2"').grid(row=0, column=0, columnspan=3)  

    g_2 = tk.StringVar()
    tk.Label(root, text='Title for Group_2: ').grid(row=25, column=0, pady=10,padx=10,sticky="e")    
    entry = tk.Entry(root, textvariable=g_2).grid(row=25, column=1,sticky="w")
    
    tk.Button(root, text='Proceed to Labelling of Group3',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)
    
    
    
    cb2 = []
    cb_v2= []
    for ix, text in enumerate(headers):
        cb_v2.append(tk.StringVar())
        off_value=0
        cb2.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v2[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb2[ix].grid(row=((ix+1)), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb2[ix].grid(row=((ix-4)), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb2[ix].grid(row=((ix-9)), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb2[ix].grid(row=((ix-14)), column=3, sticky='w')
        else:
            cb2[ix].grid(row=((ix-19)), column=4, sticky='w')
        group_1.append(off_value)
        cb2[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')   
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    group_1 = [i for i in group_1 if i != "0"]    
    
    
def group_selection_three():
    global group_2
    global g_3
    
    group_2 = []
    
    def chkbox_checked():
        for ix, item in enumerate(cb2):
            group_2[ix]=(cb_v2[ix].get())
    
    root = tk.Tk() 
    root.title("PadPlot_PCA v1.8")
    tk.Label(root, text='Please select any column name which contains the data for your "Group3"').grid(row=0, column=0, columnspan=3)  

    g_3 = tk.StringVar()
    tk.Label(root, text='Title for Group_3: ').grid(row=25, column=0, pady=10,padx=10,sticky="e")    
    entry = tk.Entry(root, textvariable=g_3).grid(row=25, column=1,sticky="w")
    
    tk.Button(root, text='Proceed to Labelling of Group3',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)
    
    
    
    cb2 = []
    cb_v2= []
    for ix, text in enumerate(headers):
        cb_v2.append(tk.StringVar())
        off_value=0
        cb2.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v2[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb2[ix].grid(row=((ix+1)), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb2[ix].grid(row=((ix-4)), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb2[ix].grid(row=((ix-9)), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb2[ix].grid(row=((ix-14)), column=3, sticky='w')
        else:
            cb2[ix].grid(row=((ix-19)), column=4, sticky='w')
        group_2.append(off_value)
        cb2[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')   
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    group_2 = [i for i in group_2 if i != "0"]   
    
def group_selection_four():
    global group_3
    global g_4
    
    group_3 = []
    
    def chkbox_checked():
        for ix, item in enumerate(cb2):
            group_3[ix]=(cb_v2[ix].get())
    
    root = tk.Tk() 
    root.title("PadPlot_PCA v1.8")
    tk.Label(root, text='Please select any column name which contains the data for your "Group4"').grid(row=0, column=0, columnspan=3)  

    g_4 = tk.StringVar()
    tk.Label(root, text='Title for Group_4: ').grid(row=25, column=0, pady=10,padx=10,sticky="e")    
    entry = tk.Entry(root, textvariable=g_4).grid(row=25, column=1,sticky="w")
    
    tk.Button(root, text='Proceed to Labelling of Group4',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)
    
    
    
    cb2 = []
    cb_v2= []
    for ix, text in enumerate(headers):
        cb_v2.append(tk.StringVar())
        off_value=0
        cb2.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v2[ix],
                             command=chkbox_checked))
        if ix < 5:
            cb2[ix].grid(row=((ix+1)), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb2[ix].grid(row=((ix-4)), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb2[ix].grid(row=((ix-9)), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb2[ix].grid(row=((ix-14)), column=3, sticky='w')
        else:
            cb2[ix].grid(row=((ix-19)), column=4, sticky='w')
        group_3.append(off_value)
        cb2[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')   
    label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()


    group_3 = [i for i in group_3 if i != "0"] 
    
    
    
    
def groupp_selection_three():
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
    
def groupp_selection_four():
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
    global gp1
    global gp2
    global gp3
    global gp4
    
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
    principaldf['x']=principaldf['PC1 ' + '(' + str(pc1) + '% of variance' + ' )']
    principaldf['y']=principaldf['PC2 ' + '(' + str(pc2) + '% of variance' + ' )']



def plot():
    global ax
    #size=int(k.get())
    
    sns.set(font_scale=1.3)
    sns.set_style("white")
    
    ax = figure.subplots()
    sns.scatterplot(data= principaldf,x= 'PC1 ' + '(' + str(pc1) + '% of variance' + ' )',
                    y= 'PC2 ' + '(' + str(pc2) + '% of variance' + ' )', 
                    ax=ax,s=150, hue='Group',legend=False)
    ax.set_title(title) 
    #ax.legend(loc=2)
    ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
    ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
    
    texts= []

    for x,y,s in zip(principaldf.x,(principaldf.y),principaldf.Sample):
        texts.append(ax.text(x,y,s,size=10))
        
    adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1),
                arrowprops=dict(arrowstyle="-",color="black",lw=0.5))
    
def plot2group():
    global ax 
    group1=principaldf[principaldf['Group'].str.contains(gp1)]
    group2=principaldf[principaldf['Group'].str.contains(gp2)]
    
    sns.set(font_scale=1.3)
    sns.set_style("white")
    
    ax=figure.subplots()


    sns.kdeplot(group1.x,group1.y,cmap="Reds",ax=ax,shade=True,shade_lowest=False, n_levels=30)

   
    sns.kdeplot(group2.x,group2.y,cmap="Blues",ax=ax,shade=True,shade_lowest=False, n_levels=30)

    ax.set_title(title) 

    ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
    ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')

    
def plot3group():
    global ax 
     
    group1=principaldf[principaldf['Group'].str.contains(gp1)]
    group2=principaldf[principaldf['Group'].str.contains(gp2)]
    group3=principaldf[principaldf['Group'].str.contains(gp3)]

    
    sns.set(font_scale=1.3)
    sns.set_style("white")
    
    ax=figure.subplots()


    sns.kdeplot(group1.x,group1.y,cmap="Reds",ax=ax,shade=True,shade_lowest=False, n_levels=30)   
    sns.kdeplot(group2.x,group2.y,cmap="Blues",ax=ax,shade=True,shade_lowest=False, n_levels=30)
    sns.kdeplot(group3.x,group3.y,cmap="Greens",ax=ax,shade=True,shade_lowest=False, n_levels=30)

    ax.set_title(title) 

    ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
    ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
    
def plot4group():
    global ax 
    
    group1=principaldf[principaldf['Group'].str.contains(gp1)]
    group2=principaldf[principaldf['Group'].str.contains(gp2)]
    group3=principaldf[principaldf['Group'].str.contains(gp3)]
    group4=principaldf[principaldf['Group'].str.contains(gp4)]
    
    sns.set(font_scale=1.3)
    sns.set_style("white")
    
    ax=figure.subplots()


    sns.kdeplot(group1.x,group1.y,cmap="Reds",ax=ax,shade=True,shade_lowest=False, n_levels=30)   
    sns.kdeplot(group2.x,group2.y,cmap="Blues",ax=ax,shade=True,shade_lowest=False, n_levels=30)
    sns.kdeplot(group3.x,group3.y,cmap="Greens",ax=ax,shade=True,shade_lowest=False, n_levels=30)
    sns.kdeplot(group4.x,group4.y,cmap="Purples",ax=ax,shade=True,shade_lowest=False, n_levels=30)

    ax.set_title(title) 

    ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
    ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
    
    
                
'''

def plot():
    global ax
    #size=int(k.get())
    
    sns.set(font_scale=1.3)
    sns.set_style("white")
    
    ax = figure.subplots()
    sns.kdeplot(principaldf.x,principaldf.y,shade=True)
    ax.set_title(title) 
    #ax.legend(loc=2)
    ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
    ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
    
    
    texts= []

    for x,y,s in zip(principaldf.x,(principaldf.y),principaldf.Sample):
        texts.append(ax.text(x,y,s,size=10))
        
    adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1),
                arrowprops=dict(arrowstyle="-",color="black",lw=0.5))
                

'''

def create_figure() -> Figure:
    global figure
    figure = Figure(figsize=(8, 8))
    ss=int(s.get())
    if ss==10:
        plot()
        
    elif num_groups==3:
        plot3group()
        
    elif num_groups==4:
        plot4group()
        
    else:
        plot2group()
    
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
root.title("PadPlot_PCA v1.8")

button = tk.Button(root, text="Cancel",command=root.destroy)
button.pack(side=tk.LEFT, padx=20, pady=20)
button2 = tk.Button(root, text="Save Figure to Parent Directory",command=save_fig)
button2.pack(side=tk.RIGHT, padx=20, pady=20)

canvas = init_gui(root, update_function=redraw_figure)

#button = tk.Button(root, text="Proceed to file options",command=root.destroy)
#button.pack()

root.mainloop() 


csv_file_path.rstrip('/')
root = tk.Tk()
root.title("PadPlot_PCA v1.8")
tk.Label(root, text="If requested, figure was saved to \n \n " + path + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)

    
root.mainloop()

