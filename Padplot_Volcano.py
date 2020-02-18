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



def doNothing():
    print("nothing")
    
    
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
    
def import_csv_data():
    global v
    global csv_file_path
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    
def get_title():
    global title
    y = csv_file_path.split('/')
    y = y[-1]
    title = y.rstrip('.csv')
    print(title)
    
def label_top_genes():
    global dfmod20
    df['x']= df['L2FC'[0:top_genes]]
    df['y']= df['-logp'[0:top_genes]]
    df['Gene2']= df['Gene'[0:top_genes]]
    dfmod=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    dfmod20=dfmod.iloc[0:top_genes]
    dfmod20    
    
def label_custom_genes():
    global df_select
    df_select= df[df['Gene'].isin(custom_list)]
    df_select['x']= df_select['L2FC']
    df_select['y']= df_select['-logp']
    df_select['Gene2']= df_select['Gene']
    df_select
    
def plot():
    global ax
    size=int(k.get())
    
    ax = figure.subplots()
    sns.scatterplot(data= df,x= 'L2FC',y= '-logp', ax=ax,s=size, hue='p-adjusted <' + str(p_value) + ' + L2FC < 2' )
    ax.set_title(title) 
    ax.set_xlabel('Log2 Fold Change')
    ax.set_ylabel('p-value (-log)')
    texts= []

    for x,y,s in zip(dfmod20.x,dfmod20.y,dfmod20.Gene2):
        texts.append(ax.text(x,y,s,size=10))
        
    for x,y,s in zip(df_select.x,df_select.y,df_select.Gene2):
        texts.append(ax.text(x,y,s,size=10))

    #adjust_text(texts,arrowprops=dict(arrowstyle="-",color="black",lw=0.5))
    
    adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1),arrowprops=dict(arrowstyle="-",color="black",lw=0.5))

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

def plot_options(): 
    global v
    global q
    global p
    global l
    global e
    global b
    global k
    global df
    global headers
    
    root = tk.Tk()
    root.title("PadPlot_Volcano v2.0")
    tk.Label(root, text='File Path:').grid(row=0, column=1,padx=10, pady=10,sticky='e')
    

    v = tk.StringVar()
    
    #entry = tk.Entry(root, textvariable=v).grid(row=0, column=2,sticky='w')
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=0, column=2,sticky='w')

    q = tk.StringVar()
    tk.Label(root, text='Label the most significant genes (between 5 and 50) or leave blank: ').grid(row=3, column=1, padx=10, pady=10,sticky='E')
    entry = tk.Entry(root, textvariable=q).grid(row=3, column=2, padx=10, pady=10)
    
    l = tk.StringVar()
    tk.Label(root, text='Label certain genes (separated by ",") or leave blank: ').grid(row=5, column=1, padx=10, pady=10, sticky='E')
    entry = tk.Entry(root, textvariable=l).grid(row=5, column=2, padx=10, pady=10)
    
    p = tk.StringVar()
    tk.Label(root, text='Cutoff p-value (adjusted): ').grid(row=7, column=1, padx=10, pady=10, sticky='E')
    entry = tk.Entry(root, textvariable=p).grid(row=7, column=2, padx=10, pady=10)
    
    tk.Label(root,text="Filter outliers for a better plot (StDs from mean):").grid(column=1, row=9,padx=10, pady=10,sticky="E")

    MODES = [
        ("15", "15"),
        ("30", "30"),
        ("50", "50"),
        ("None", "1000"),
    ]

    e = tk.StringVar()
    e.set("30") # initialize

    for text, mode in MODES:
        b = tk.Radiobutton(root, text=text,variable=e, value=mode)
        b.grid(sticky=tk.W,column=2)

    b = tk.StringVar()
    tk.Label(root, text='Assign plot title (or Padplot will automatically detect): ').grid(row=19, column=1, padx=10, pady=10,sticky="E")
    entry = tk.Entry(root, textvariable=b).grid(row=19, column=2, padx=10, pady=10)
    
    tk.Label(root,text="Define the size of your points:").grid(row=21,column=1,padx=10, pady=10,sticky='E')
    
    MODES = [
        ("Small", "10"),
        ("Medium", "20"),
        ("Large", "50"),
        ("Very Large", "100"),
    ]

    k = tk.StringVar()
    k.set("20") # initialize

    for text, mode in MODES:
        c = tk.Radiobutton(root, text=text,variable=k, value=mode)
        c.grid(sticky=tk.W,column=2)


    tk.Button(root, text='Proceed',command=root.destroy).grid(row=27, column=2) 
    
    tk.Button(root, text='Debug Options',command=debug_options).grid(row=27, column=1, padx=10, pady=10, sticky='w')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=28, column=1, padx=10, pady=10, sticky='w')

    root.mainloop()
    
    df= pd.read_csv(csv_file_path)
    headers= list(df.columns.values)
    
def gene_names_selection():
    global Fold_changes
    global g_1
    global root
    global padjs
    global gene_names
    
    Fold_changes = []
    padjs= []
    gene_names= []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            Fold_changes[ix]=(cb_v[ix].get())
    
    root = tk.Tk()
    root.title("PadPlot_Volcano v1.0")
    
    tk.Label(root, text='Please select the column name which contains the Log2 Fold changes [one column only]').grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    tk.Label(root, text='Please select the column name which contains the Adjusted p-values [one column only]').grid(row=8, column=0, columnspan=4, padx=10, pady=10) 
    
    tk.Label(root, text='Please select the column name which contains the Gene names [one column only]').grid(row=16, column=0, columnspan=4, padx=10, pady=10)
    
    tk.Button(root, text='Proceed to Plot (Please be patient)',command=root.destroy).grid(row=40, column=3, columnspan=3,pady=10, padx=10, sticky='e')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=40, column=0, padx=10, pady=10, sticky='w')
    
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
        Fold_changes.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
    


      
    
    def chkbox_checked2():
        for ix, item in enumerate(cb2):
            padjs[ix]=(cb_v2[ix].get())
    
    cb2 = []
    cb_v2= []
    for ix, text in enumerate(headers):
        cb_v2.append(tk.StringVar())
        off_value=0
        cb2.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v2[ix],
                             command=chkbox_checked2))
        if ix < 5:
            cb2[ix].grid(row=((ix+1)+10), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb2[ix].grid(row=((ix-4)+10), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb2[ix].grid(row=((ix-9)+10), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb2[ix].grid(row=((ix-14)+10), column=3, sticky='w')
        else:
            cb2[ix].grid(row=((ix-19)+10), column=4, sticky='w')
        padjs.append(off_value)
        cb2[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')

    
    def chkbox_checked3():
        for ix, item in enumerate(cb3):
            gene_names[ix]=(cb_v3[ix].get())
    
    cb3 = []
    cb_v3= []
    for ix, text in enumerate(headers):
        cb_v3.append(tk.StringVar())
        off_value=0
        cb3.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v3[ix],
                             command=chkbox_checked3))
        if ix < 5:
            cb3[ix].grid(row=((ix+1)+20), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb3[ix].grid(row=((ix-4)+20), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb3[ix].grid(row=((ix-9)+20), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb3[ix].grid(row=((ix-14)+20), column=3, sticky='w')
        else:
            cb3[ix].grid(row=((ix-19)+20), column=4, sticky='w')
        gene_names.append(off_value)
        cb3[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()

    Fold_changes = [i for i in Fold_changes if i != "0"]
    padjs = [i for i in padjs if i != "0"]
    gene_names = [i for i in gene_names if i != "0"]
    
def process_data():
    global df
    global custom_list
    global p_value
    global title
    
    p_value= float(p.get())
    print(str(p_value))

    custom_list= l.get()
    custom_list=custom_list.split(',')
    print(custom_list)

    custom_title= str(b.get())
    if len(custom_title) < 1:
        get_title()
    else:
        title=custom_title

    df= pd.read_csv(csv_file_path)

    fc_df = df.filter(Fold_changes)
    #fc_df= fc_df.iloc[:,0]
    fc_df.columns= ['L2FC']
    print(fc_df)

    p_df = df.filter(padjs)
    p_df.columns= ['p-value (Adjusted)']
    print(p_df)

    gene_df = df.filter(gene_names)
    #gene_df = gene_df.filter(regex='Name|name|NAME')
    gene_df.columns= ['Gene']
    print(gene_df)

    df['L2FC'] = fc_df
    df['padj'] = p_df
    df['Gene'] = gene_df

    df['-logp'] = - np.log(df['padj'])
    df['p(-log10)'] = - np.log10(df['padj'])
    print(df)

    df['Significant'] = (np.abs(df['L2FC']) > 2).replace({True : '>2', False : '<=2'})
    df['0.05 Threshold'] = df['padj'] < p_value
    df['p-adjusted <' + str(p_value) + ' + L2FC < 2'] = (df['0.05 Threshold'] == True) & (df['Significant'] == '>2') 

    gene_filter=int(e.get())

    df['test']=df['p(-log10)']
    df['test_2']=df['L2FC']
    df['outlier']=np.abs(df.test-df.test.mean()) <= (gene_filter*df.test.std())
    df['outlier_2']=np.abs(df.test_2-df.test_2.mean()) <= (gene_filter*df.test_2.std())
    df = df[df.outlier]
    df = df[df.outlier_2]
    df 

    
'''
def save_fig():
    x=figure
    x.savefig(path+ '/' + title + '_padplot_Volcano.svg', format='svg', dpi=1200)
    root.destroy()
    
'''

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

gene_names_selection()

process_data()




    
tops=int(q.get())

if tops > 4:
    top_genes = tops
    label_top_genes()

else:
    dfmod20 = pd.DataFrame(columns=['x','y','Gene2'])

label_custom_genes()   


  
    
sns.set_style("white")

root = tk.Tk()
root.title("PadPlot_Volcano v2.0")

button = tk.Button(root, text="Cancel",command=root.destroy)
button.pack(side=tk.LEFT, padx=20, pady=20)
button2 = tk.Button(root, text="Save Figure to Parent Directory",command=save_fig)
button2.pack(side=tk.RIGHT, padx=20, pady=20)

canvas = init_gui(root, update_function=redraw_figure)

#button = tk.Button(root, text="Proceed to file options",command=root.destroy)
#button.pack()

root.mainloop() 







get_path_for_svg()


csv_file_path.rstrip('/')
root = tk.Tk()
root.title("PadPlot_Volcano v2.0")
tk.Label(root, text="If requested, figure was saved to \n \n " + path + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)

    
root.mainloop()
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



def doNothing():
    print("nothing")
    
    
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
    
def import_csv_data():
    global v
    global csv_file_path
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    
def get_title():
    global title
    y = csv_file_path.split('/')
    y = y[-1]
    title = y.rstrip('.csv')
    print(title)
    
def label_top_genes():
    global dfmod20
    df['x']= df['L2FC'[0:top_genes]]
    df['y']= df['-logp'[0:top_genes]]
    df['Gene2']= df['Gene'[0:top_genes]]
    dfmod=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    dfmod20=dfmod.iloc[0:top_genes]
    dfmod20    
    
def label_custom_genes():
    global df_select
    df_select= df[df['Gene'].isin(custom_list)]
    df_select['x']= df_select['L2FC']
    df_select['y']= df_select['-logp']
    df_select['Gene2']= df_select['Gene']
    df_select
    
def plot():
    global ax
    size=int(k.get())
    
    ax = figure.subplots()
    sns.scatterplot(data= df,x= 'L2FC',y= '-logp', ax=ax,s=size, hue='p-adjusted <' + str(p_value) + ' + L2FC < 2' )
    ax.set_title(title) 
    ax.set_xlabel('Log2 Fold Change')
    ax.set_ylabel('p-value (-log)')
    texts= []

    for x,y,s in zip(dfmod20.x,dfmod20.y,dfmod20.Gene2):
        texts.append(ax.text(x,y,s,size=10))
        
    for x,y,s in zip(df_select.x,df_select.y,df_select.Gene2):
        texts.append(ax.text(x,y,s,size=10))

    #adjust_text(texts,arrowprops=dict(arrowstyle="-",color="black",lw=0.5))
    
    adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1),arrowprops=dict(arrowstyle="-",color="black",lw=0.5))

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

def plot_options(): 
    global v
    global q
    global p
    global l
    global e
    global b
    global k
    global df
    global headers
    
    root = tk.Tk()
    root.title("PadPlot_Volcano v2.0")
    tk.Label(root, text='File Path:').grid(row=0, column=1,padx=10, pady=10,sticky='e')
    

    v = tk.StringVar()
    
    #entry = tk.Entry(root, textvariable=v).grid(row=0, column=2,sticky='w')
    tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=0, column=2,sticky='w')

    q = tk.StringVar()
    tk.Label(root, text='Label the most significant genes (between 5 and 50) or leave blank: ').grid(row=3, column=1, padx=10, pady=10,sticky='E')
    entry = tk.Entry(root, textvariable=q).grid(row=3, column=2, padx=10, pady=10)
    
    l = tk.StringVar()
    tk.Label(root, text='Label certain genes (separated by ",") or leave blank: ').grid(row=5, column=1, padx=10, pady=10, sticky='E')
    entry = tk.Entry(root, textvariable=l).grid(row=5, column=2, padx=10, pady=10)
    
    p = tk.StringVar()
    tk.Label(root, text='Cutoff p-value (adjusted): ').grid(row=7, column=1, padx=10, pady=10, sticky='E')
    entry = tk.Entry(root, textvariable=p).grid(row=7, column=2, padx=10, pady=10)
    
    tk.Label(root,text="Filter outliers for a better plot (StDs from mean):").grid(column=1, row=9,padx=10, pady=10,sticky="E")

    MODES = [
        ("15", "15"),
        ("30", "30"),
        ("50", "50"),
        ("None", "1000"),
    ]

    e = tk.StringVar()
    e.set("30") # initialize

    for text, mode in MODES:
        b = tk.Radiobutton(root, text=text,variable=e, value=mode)
        b.grid(sticky=tk.W,column=2)

    b = tk.StringVar()
    tk.Label(root, text='Assign plot title (or Padplot will automatically detect): ').grid(row=19, column=1, padx=10, pady=10,sticky="E")
    entry = tk.Entry(root, textvariable=b).grid(row=19, column=2, padx=10, pady=10)
    
    tk.Label(root,text="Define the size of your points:").grid(row=21,column=1,padx=10, pady=10,sticky='E')
    
    MODES = [
        ("Small", "10"),
        ("Medium", "20"),
        ("Large", "50"),
        ("Very Large", "100"),
    ]

    k = tk.StringVar()
    k.set("20") # initialize

    for text, mode in MODES:
        c = tk.Radiobutton(root, text=text,variable=k, value=mode)
        c.grid(sticky=tk.W,column=2)


    tk.Button(root, text='Proceed',command=root.destroy).grid(row=27, column=2) 
    
    tk.Button(root, text='Debug Options',command=debug_options).grid(row=27, column=1, padx=10, pady=10, sticky='w')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=28, column=1, padx=10, pady=10, sticky='w')

    root.mainloop()
    
    df= pd.read_csv(csv_file_path)
    headers= list(df.columns.values)
    
def gene_names_selection():
    global Fold_changes
    global g_1
    global root
    global padjs
    global gene_names
    
    Fold_changes = []
    padjs= []
    gene_names= []
    def chkbox_checked():
        for ix, item in enumerate(cb):
            Fold_changes[ix]=(cb_v[ix].get())
    
    root = tk.Tk()
    root.title("PadPlot_Volcano v2.0")
    
    tk.Label(root, text='Please select the column name which contains the Log2 Fold changes [one column only]').grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    tk.Label(root, text='Please select the column name which contains the Adjusted p-values [one column only]').grid(row=8, column=0, columnspan=4, padx=10, pady=10) 
    
    tk.Label(root, text='Please select the column name which contains the Gene names [one column only]').grid(row=16, column=0, columnspan=4, padx=10, pady=10)
    
    tk.Button(root, text='Proceed to Plot (Please be patient)',command=root.destroy).grid(row=40, column=3, columnspan=3,pady=10, padx=10, sticky='e')
    
    tk.Button(root, text='Cancel',command=exitout).grid(row=40, column=0, padx=10, pady=10, sticky='w')
    
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
        Fold_changes.append(off_value)
        cb[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
    


      
    
    def chkbox_checked2():
        for ix, item in enumerate(cb2):
            padjs[ix]=(cb_v2[ix].get())
    
    cb2 = []
    cb_v2= []
    for ix, text in enumerate(headers):
        cb_v2.append(tk.StringVar())
        off_value=0
        cb2.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v2[ix],
                             command=chkbox_checked2))
        if ix < 5:
            cb2[ix].grid(row=((ix+1)+10), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb2[ix].grid(row=((ix-4)+10), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb2[ix].grid(row=((ix-9)+10), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb2[ix].grid(row=((ix-14)+10), column=3, sticky='w')
        else:
            cb2[ix].grid(row=((ix-19)+10), column=4, sticky='w')
        padjs.append(off_value)
        cb2[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')

    
    def chkbox_checked3():
        for ix, item in enumerate(cb3):
            gene_names[ix]=(cb_v3[ix].get())
    
    cb3 = []
    cb_v3= []
    for ix, text in enumerate(headers):
        cb_v3.append(tk.StringVar())
        off_value=0
        cb3.append(tk.Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                             variable=cb_v3[ix],
                             command=chkbox_checked3))
        if ix < 5:
            cb3[ix].grid(row=((ix+1)+20), column=0, sticky='w')
        elif ix >4 and ix < 10:
            cb3[ix].grid(row=((ix-4)+20), column=1, sticky='w')
        elif ix >9 and ix < 15:
            cb3[ix].grid(row=((ix-9)+20), column=2, sticky='w')
        elif ix >14 and ix < 20:
            cb3[ix].grid(row=((ix-14)+20), column=3, sticky='w')
        else:
            cb3[ix].grid(row=((ix-19)+20), column=4, sticky='w')
        gene_names.append(off_value)
        cb3[-1].deselect()
    label = tk.Label(root, width=20)
    #label.grid(row=ix+1, column=0, sticky='w')
    root.mainloop()

    Fold_changes = [i for i in Fold_changes if i != "0"]
    padjs = [i for i in padjs if i != "0"]
    gene_names = [i for i in gene_names if i != "0"]
    
def process_data():
    global df
    global custom_list
    global p_value
    global title
    
    p_value= float(p.get())
    print(str(p_value))

    custom_list= l.get()
    custom_list=custom_list.split(',')
    print(custom_list)

    custom_title= str(b.get())
    if len(custom_title) < 1:
        get_title()
    else:
        title=custom_title

    df= pd.read_csv(csv_file_path)

    fc_df = df.filter(Fold_changes)
    #fc_df= fc_df.iloc[:,0]
    fc_df.columns= ['L2FC']
    print(fc_df)

    p_df = df.filter(padjs)
    p_df.columns= ['p-value (Adjusted)']
    print(p_df)

    gene_df = df.filter(gene_names)
    #gene_df = gene_df.filter(regex='Name|name|NAME')
    gene_df.columns= ['Gene']
    print(gene_df)

    df['L2FC'] = fc_df
    df['padj'] = p_df
    df['Gene'] = gene_df

    df['-logp'] = - np.log(df['padj'])
    df['p(-log10)'] = - np.log10(df['padj'])
    print(df)

    df['Significant'] = (np.abs(df['L2FC']) > 2).replace({True : '>2', False : '<=2'})
    df['0.05 Threshold'] = df['padj'] < p_value
    df['p-adjusted <' + str(p_value) + ' + L2FC < 2'] = (df['0.05 Threshold'] == True) & (df['Significant'] == '>2') 

    gene_filter=int(e.get())

    df['test']=df['p(-log10)']
    df['test_2']=df['L2FC']
    df['outlier']=np.abs(df.test-df.test.mean()) <= (gene_filter*df.test.std())
    df['outlier_2']=np.abs(df.test_2-df.test_2.mean()) <= (gene_filter*df.test_2.std())
    df = df[df.outlier]
    df = df[df.outlier_2]
    df 

    
'''
def save_fig():
    x=figure
    x.savefig(path+ '/' + title + '_padplot_Volcano.svg', format='svg', dpi=1200)
    root.destroy()
    
'''

def save_fig():
    global path
    path= csv_file_path.split('/')
    strip=len(path)-1
    path = path[:strip]
    path= '/'.join(path)
    path
    x=figure
    x.savefig(path+ '/' + title + '_padplot_Volcano.svg', format='svg', dpi=1200)
    root.destroy()
    return path

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

gene_names_selection()

process_data()




    
tops=int(q.get())

if tops > 4:
    top_genes = tops
    label_top_genes()

else:
    dfmod20 = pd.DataFrame(columns=['x','y','Gene2'])

label_custom_genes()   


  
    
sns.set_style("white")

root = tk.Tk()
root.title("PadPlot_Volcano v2.0")

button = tk.Button(root, text="Cancel",command=root.destroy)
button.pack(side=tk.LEFT, padx=20, pady=20)
button2 = tk.Button(root, text="Save Figure to Parent Directory",command=save_fig)
button2.pack(side=tk.RIGHT, padx=20, pady=20)

canvas = init_gui(root, update_function=redraw_figure)

#button = tk.Button(root, text="Proceed to file options",command=root.destroy)
#button.pack()

root.mainloop() 







get_path_for_svg()


csv_file_path.rstrip('/')
root = tk.Tk()
root.title("PadPlot_Volcano v2.0")
tk.Label(root, text="If requested, figure was saved to \n \n " + path + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)

    
root.mainloop()
