import tkinter as tk

from tkinter.filedialog import askdirectory
import sys
import os
from datetime import datetime

now = datetime.now().time() 
now=now.strftime('%H%M')

#fig_dir= str(now) + "_PadPlot_Figures"
#if not 'workbookDir' in globals():
 #   workbookDir = os.getcwd()
    
#fullpath=workbookDir

'''    
fullpath = os.path.join(workbookDir, fig_dir)
if not os.path.exists(fullpath):
    os.mkdir(fullpath) 
    
'''
    


def error_handling(e):
    root = tk.Tk()
    root.title("PadPlot_Error_Detector")
    tk.Label(root, text="PadPlot Detected an Error and exited.").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(root, text="The error is printed below. Did you select the correct columns during assignments?").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(root, text="Error= " + str(e)).grid(row=2, column=0, padx=10, pady=10)
    tk.Label(root, text="In order to fix, please restart the kernel and try again.").grid(row=3, column=0, padx=10, pady=10)
    tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=20, column=0, padx=10, pady=10, sticky='w',columnspan=4)

    root.mainloop()
    
    sys.exit()
            

def heatmap():
    
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    import pandas as pd
    import sys
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import numpy as np
    import seaborn as sns; sns.set_style("white")
    import matplotlib.image as mpimg
    from matplotlib.figure import Figure
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    
    global df
    global x
    global figure
    global g


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



        tk.Label(root,text="Number of Genes to display:").grid(row=21,column=1,padx=10, pady=10,sticky='e')

        w = tk.Scale(root, variable=val, from_=10, to=100,orient=tk.HORIZONTAL, resolution=5).grid(row=21,column=2,sticky='w')

        tk.Label(root,text="Define the colour of your Heatmap:").grid(row=25,column=1,padx=10, pady=10,sticky='e')



        MODES = {
            "Yellow, Orange and Red":"YlOrRd",
            "Orange and Red":"OrRd",
            "Blue and Red":"bwr",
            "Red and Purple":"RdPu",
            "Hot":"hot",
            "Standard": "magma",
            "Currently  Undefined": "null"
        }


        def boxtext(new_value):
            global colo
            #display.config(text = MODES[new_value])
            colo=MODES[new_value]

        var = tk.StringVar()
        var.set("Currently  Undefined") # initialize
        #create a dropdown list


        p = tk.OptionMenu(root, var, *MODES, command=boxtext).grid(row=25,column=2,columnspan=2,sticky='w')

        #display= tk.Label(root)
        #display.grid(row=25,column=3)

        b = tk.StringVar()
        tk.Label(root, text='Assign plot title (or Padplot will automatically detect): ').grid(row=32, column=1, padx=10, pady=10,sticky="w")
        entry = tk.Entry(root, textvariable=b).grid(row=32, column=2, padx=10, pady=10,sticky='w')

        tk.Button(root, text='Proceed to detecting Gene Names',command=root.destroy).grid(row=34, column=2, padx=10, pady=10, sticky='e')

        tk.Button(root, text='Debug Options',command=debug_options).grid(row=34, column=1, padx=10, pady=10, sticky='w')

        tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=35, column=1, padx=10, pady=10, sticky='w',columnspan=4)
        #return cancel

        root.mainloop()

        df= pd.read_csv(csv_file_path)
        headers= list(df.columns.values)
        
        
        
        #return df
        #return val



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

        tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=9, column=0, padx=10, pady=10, sticky='w',columnspan=4)

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

        tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=20, column=0, padx=10, pady=10, sticky='w',columnspan=4)

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

        tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=20, column=0, padx=10, pady=10, sticky='w',columnspan=4)

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

        try:
            if counts < 81:
                g = sns.clustermap(temp.groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap=colour,metric = 'correlation',z_score=0) 
            #g.set_title(title)
            else:
                g = sns.clustermap(temp.groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap=colour,metric = 'correlation',z_score=0,yticklabels=False)

        except Exception as e: 
            error_handling(e)
            
       
            
            
        return g.fig



    
        
   
    plot_options()







    try:
        gene_names_selection()
    except Exception as e: 
            error_handling(e)
        
    try:    
        group_selection_one()
    except Exception as e: 
            error_handling(e)
        
    try:    
        group_selection_two()
    except Exception as e: 
            error_handling(e)
    
    global cutoff
    cutoff= int(val.get())
 
    
    df=df.head(cutoff)



    counts=cutoff

    if counts < 20:
        sns.set(font_scale=1)

    elif counts > 20 and counts < 30:
        sns.set(font_scale=0.9)

    elif counts > 30 and counts < 40:
        sns.set(font_scale=0.8)

    elif counts > 40 and counts <50:
        sns.set(font_scale=0.7)

    elif counts > 50 and counts <60:
        sns.set(font_scale=0.6)

    elif counts > 60 and counts <80:
        sns.set(font_scale=0.6)

    else:
        sns.set(font_scale=1.2)

        
    try:    
        process_data()
    except Exception as e: 
            error_handling(e)



    try:
        colour=colo
    except Exception as e: 
        error_handling(e)



    figure = create_plot()


    global path
    global title
    #sns.set_style("white")
    def save_fig():
        global path
        path= csv_file_path.split('/')
        strip=len(path)-1
        path = path[:strip]
        path= '/'.join(path)
        path
        figure
        figure.savefig(fullpath + '//' + now + '_' + title + '_padplot_Heatmap.svg', format='svg', dpi=1200)
        root.destroy()
        return path


    root = tk.Tk()
    root.title("PadPlot_Heatmap v1.0")


    #root.geometry("1000x1000") 
    button = tk.Button(root, text="Cancel",command=root.destroy)
    button.pack(side=tk.LEFT, padx=20, pady=20)
    button2 = tk.Button(root, text="Save Figure to Parent Directory",command=save_fig)
    button2.pack(side=tk.RIGHT, padx=20, pady=20)

    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


    tk.mainloop()

    csv_file_path.rstrip('/')

    root = tk.Tk()
    root.title("PadPlot_Heatmap v1.0")
    tk.Label(root, text="If requested, figure was saved to \n \n " + fullpath + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)
    tk.Button(root, text='Finish',command=exitout).grid(row=35, column=0, padx=10, pady=10, sticky='w',columnspan=3)

    root.mainloop()
    
    

def volcano():
    
    global df
    global dfmod20
    global figure
    global top_genes
    
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    #from tkinter import *
    import pandas as pd
    
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
        #return dfmod20

    def label_custom_genes():
        global df_select
        df_select= df[df['Gene'].isin(custom_list)]
        df_select['x']= df_select['L2FC']
        df_select['y']= df_select['-logp']
        df_select['Gene2']= df_select['Gene']
        df_select

    def plot():
        try:
            global ax
            size=int(k.get())

            ax = figure.subplots()
            sns.scatterplot(data= df,x= 'L2FC',y= '-logp', ax=ax,s=size, hue='p-adjusted <' + str(p_value) + ' + L2FC < 2' , legend=False)
            ax.set_title(title) 
            ax.set_xlabel('Log2 Fold Change',size=15)
            ax.set_ylabel('p-value (-log)',size=15)
            texts= []

            for x,y,s in zip(dfmod20.x,dfmod20.y,dfmod20.Gene2):
                texts.append(ax.text(x,y,s,size=10))

            for x,y,s in zip(df_select.x,df_select.y,df_select.Gene2):
                texts.append(ax.text(x,y,s,size=10))

            #adjust_text(texts,arrowprops=dict(arrowstyle="-",color="black",lw=0.5))

            adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1),
                        arrowprops=dict(arrowstyle="-",color="black",lw=0.5))
            
            ax.legend(loc=2)
            
        except Exception as e: 
            error_handling(e)

    def create_figure() -> Figure:
        global figure
        figure = Figure(figsize=(10, 8))

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
        global filt
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

        filt = tk.StringVar()
        filt.set("30") # initialize

        for text, mode in MODES:
            b = tk.Radiobutton(root, text=text,variable=filt, value=mode)
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

        tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=28, column=1, padx=10, pady=10, sticky='w')

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

        tk.Button(root, text='Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=40, column=0, padx=10, pady=10, sticky='w',columnspan=3)

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

        gene_filter=int(filt.get())

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
        figure.savefig(fullpath + '//' + now + '_' + title + '_padplot_Heatmap.svg', format='svg', dpi=1200)
        figure.savefig(fullpath + '//' + now + '_' + title + '_padplot_Heatmap.png', format='png', dpi=800)
        #figure.savefig(title + '_padplot_Volcano.svg', format='svg', dpi=1200)
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



    try:
        plot_options()
    except Exception as e: 
            error_handling(e)

    try:
        gene_names_selection()
    except Exception as e: 
            error_handling(e)

    try:
        process_data()
    except Exception as e: 
            error_handling(e)





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
    tk.Label(root, text="If requested, figure was saved to \n \n " + fullpath + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)
    tk.Button(root, text='Finish',command=exitout).grid(row=35, column=0, padx=10, pady=10, sticky='w',columnspan=3)

    root.mainloop()
    
    error=0

def pca():
    
    global df
    global figure 
    
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

        tk.Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=35, column=1, padx=10, pady=10, sticky='w',columnspan=3)
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

        tk.Button(root, text='Proceed to Labelling of Group 2',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)



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
        if num_groups==2:
            tk.Button(root, text='Proceed to Plotting',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)
        else:
            tk.Button(root, text='Proceed to Labelling of Group 3',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)


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
        if num_groups==3:
            tk.Button(root, text='Proceed to Plotting',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)
        else:
             tk.Button(root, text='Proceed to Labelling of Group 4',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)



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

        tk.Button(root, text='Proceed to Plotting',command=root.destroy).grid(row=26, column=3,columnspan=2,pady=10, padx=10)



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

    '''


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
        
        '''

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
                        ax=ax,s=400, hue='Group',legend=False)
        ax.set_title(title) 
        #ax.legend(loc=2)
        ax.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
        ax.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')

        texts= []

        for x,y,s in zip(principaldf.x,(principaldf.y),principaldf.Sample):
            texts.append(ax.text(x,y,s,size=15))

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
        
        try:
            Figure = create_figure()
            canvas.figure = Figure
            canvas.draw()
        except Exception as e: 
            error_handling(e)

    def save_fig():
        x=figure
        figure.savefig(fullpath + '//' + now + '_' + title + '_padplot_PCA.svg', format='svg', dpi=1200)
        #figure.savefig(title+ '_padplot_PCA.svg', format='svg', dpi=1200)
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
    global num_groups
    num_groups=int(k.get())
    group_selection_one()
    group_selection_two()

    if num_groups==3:
        group_selection_three()
        try:
            process_data()
        except Exception as e: 
            error_handling(e)
    elif num_groups==4:
        group_selection_three()
        group_selection_four()
        try:
            process_data()
        except Exception as e: 
            error_handling(e)      
    else:
        try:
            process_data()
        except Exception as e: 
            error_handling(e)


    sns.set_style("white")

    root = tk.Tk()
    root.title("PadPlot_PCA v1.8")
    
    get_path_for_svg()

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
    tk.Label(root, text="If requested, figure was saved to \n \n " + fullpath + "\n \n Thank you for using padplot!").grid(row=0, column=0, padx=100, pady=100)
    tk.Button(root, text='Finish',command=exitout).grid(row=35, column=0, padx=10, pady=10, sticky='w',columnspan=3)

    root.mainloop()
    
    error=0

    
if not 'workbookDir' in globals():
    workbookDir = os.getcwd()
    
def exitout():
    root.destroy()
    sys.exit()


def sel_pca():
    global sel
    sel=1
    
    root.destroy()

def sel_volcano():
    global sel
    sel=2
    
    root.destroy()

def sel_heatmap():
    global sel
    sel=3
    
    root.destroy()
    
def get_figure_path():
        global vv
        global fullpath
        #global y

        fullpath= askdirectory()
        print(fullpath)
        vv.set(fullpath)
    
root = tk.Tk()
root.title("PadPlot_Main v1.2") 
tk.Label(root, text="Welcome to PadPlot, as a safety feature, Padplot will not create or remove folders.\n PadPlot will write figures to a folder of your choice.").grid(row=0, column=0, padx=20, pady=20,columnspan=5)
#tk.Label(root, text='Choose a folder to save plots to:').grid(row=1, column=1,padx=20, pady=20,sticky="e")
tk.Button(root, text='Choose a folder to write your figures to',command=get_figure_path).grid(row=1, column=2,padx=20, pady=20)
tk.Label(root, text="Please choose your plot").grid(row=3, column=0, padx=20, pady=20,columnspan=5)
button = tk.Button(root, text="PCA",command=sel_pca).grid(row=4, column=1,pady=10, padx=10)
button2 = tk.Button(root, text="Volcano",command=sel_volcano).grid(row=4, column=2,pady=10, padx=10)
button3 = tk.Button(root, text="Heat Map",command=sel_heatmap).grid(row=4, column=3,pady=10, padx=10)
tk.Label(root, text="PadPlot authored by SimonF92, contact me at s.fisher.1@research.gla.ac.uk").grid(row=15, column=0, padx=20, pady=20,columnspan=5)
button4= tk.Button(root, text='Cancel',command=exitout).grid(row=35, column=1, padx=10, pady=10, sticky='w')
root.mainloop()
 
    
if sel == 1:
    pca()
elif sel == 2:
    volcano()
else:
    heatmap()
    
'''
if len(os.listdir(fullpath)) == 0: # Check is empty..
    shutil.rmtree(fullpath)
    
else:
    pass
    
'''


