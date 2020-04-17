from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import numpy as np
import adjustText
from adjustText import adjust_text
import seaborn as sns; sns.set_style("white")
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from datetime import datetime
import sys
import os
import matplotlib


global fullpath
global num_groups
global var6
global csv_file_path
global read 

def import_csv_data():
        global v
        global csv_file_path
        global read 
        csv_file_path = askopenfilename()
        read = 1
        #return read
        

def pca():
    global df
    global fig
    global var6
    global control_group
    global g_1
    global group_1
    global g_2
    global group_2
    global g_3
    global group_3
    global g_4

    


    now = datetime.now().time() 
    now=now.strftime('%H%M')

    #fullpath= "C:\\Users\\2087455F\\Desktop"


    df=pd.read_csv(csv_file_path)
    headers= list(df.columns.values)

    num_groups=int(var420.get())

    #num_groups=4


    #global group_selection_3

    def group_selection():
        global control_group
        global g_1

        global group_1
        global g_2

        global group_2
        global g_3

        global group_3
        global g_4

        control_group = []

        def chkbox_checked():
            for ix, item in enumerate(cb):
                control_group[ix]=(cb_v[ix].get())

        root = Tk() 
        root.title("PadPlot_PCA v1.8")
        Label(root, text='Please select any column name which contains the data for your "Group1"').grid(row=0, column=0, columnspan=3)  

        Label(root, text='Please select any column name which contains the data for your "Group2"').grid(row=10, column=0, columnspan=3)  


        cb = []
        cb_v= []
        for ix, text in enumerate(headers):
            cb_v.append(StringVar())
            off_value=0
            cb.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                                 variable=cb_v[ix],
                                 command=chkbox_checked))
            if ix < 5:
                cb[ix].grid(row=((ix+1)), column=0, sticky='w')
            elif ix >4 and ix < 10:
                cb[ix].grid(row=((ix-4)), column=1, sticky='w')
            elif ix >9 and ix < 15:
                cb[ix].grid(row=((ix-9)), column=2, sticky='w')
            elif ix >14 and ix < 20:
                cb[ix].grid(row=((ix-14)), column=3, sticky='w')
            else:
                cb[ix].grid(row=((ix-19)), column=4, sticky='w')
            control_group.append(off_value)
            cb[-1].deselect()
        label = Label(root, width=20)
        #label.grid(row=ix+1, column=0, sticky='w')   
        #label.grid(row=ix+1, column=0, sticky='w')
        #root.mainloop()


        control_group = [i for i in control_group if i != "0"]


        global group_1
        global g_2
        group_1 = []

        def chkbox_checked2():
            for ix, item in enumerate(cb2):
                group_1[ix]=(cb_v2[ix].get())

        #root = Tk() 
        #root.title("PadPlot_PCA v1.8")



        cb2 = []
        cb_v2= []
        for ix, text in enumerate(headers):
            cb_v2.append(StringVar())
            off_value=0
            cb2.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
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
            group_1.append(off_value)
            cb2[-1].deselect()
        label = Label(root, width=20)
        #label.grid(row=ix+1, column=0, sticky='w')   
        #label.grid(row=ix+1, column=0, sticky='w')
        #root.mainloop()


        group_1 = [i for i in group_1 if i != "0"]   


        def group_selection_3():
            global group_2
            global g_3

            group_2 = []

            def chkbox_checked3():
                for ix, item in enumerate(cb3):
                    group_2[ix]=(cb_v3[ix].get())

            cb3 = []
            cb_v3= []
            for ix, text in enumerate(headers):
                cb_v3.append(StringVar())
                off_value=0
                cb3.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
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
                group_2.append(off_value)
                cb3[-1].deselect()
            label = Label(root, width=20)

            group_2 = [i for i in group_2 if i != "0"]   

        def group_selection_4():
            global group_3
            global g_4

            group_3 = []

            def chkbox_checked4():
                for ix, item in enumerate(cb4):
                    group_3[ix]=(cb_v4[ix].get())

            #root = Tk() 
            #root.title("PadPlot_PCA v1.8")



            cb4 = []
            cb_v4= []
            for ix, text in enumerate(headers):
                cb_v4.append(StringVar())
                off_value=0
                cb4.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                                     variable=cb_v4[ix],
                                     command=chkbox_checked4))
                if ix < 5:
                    cb4[ix].grid(row=((ix+1)+30), column=0, sticky='w')
                elif ix >4 and ix < 10:
                    cb4[ix].grid(row=((ix-4)+30), column=1, sticky='w')
                elif ix >9 and ix < 15:
                    cb4[ix].grid(row=((ix-9)+30), column=2, sticky='w')
                elif ix >14 and ix < 20:
                    cb4[ix].grid(row=((ix-14)+30), column=3, sticky='w')
                else:
                    cb4[ix].grid(row=((ix-19)+30), column=4, sticky='w')
                group_3.append(off_value)
                cb4[-1].deselect()
            label = Label(root, width=20)
            #label.grid(row=ix+1, column=0, sticky='w')   
            #label.grid(row=ix+1, column=0, sticky='w')
            #root.mainloop()


            group_3 = [i for i in group_3 if i != "0"] 

        if num_groups==3:
            Label(root, text='Please select any column name which contains the data for your "Group3"').grid(row=20, column=0, columnspan=3)
            group_selection_3()
        elif num_groups==4:
            Label(root, text='Please select any column name which contains the data for your "Group3"').grid(row=20, column=0, columnspan=3)
            group_selection_3()
            Label(root, text='Please select any column name which contains the data for your "Group4"').grid(row=30, column=0, columnspan=3)
            group_selection_4()
        else:
            pass

        g_1 = StringVar()
        Label(root, text='Title for Group_1: ').grid(row=40, column=0, pady=10,padx=10,sticky="e")    
        entry = Entry(root, textvariable=g_1).grid(row=40, column=1,sticky="w")
        g_2 = StringVar()
        Label(root, text='Title for Group_2: ').grid(row=41, column=0, pady=10,padx=10,sticky="e")    
        entry = Entry(root, textvariable=g_2).grid(row=41, column=1,sticky="w")
        if num_groups==3:
            g_3 = StringVar()
            Label(root, text='Title for Group_3: ').grid(row=42, column=0, pady=10,padx=10,sticky="e")    
            entry = Entry(root, textvariable=g_3).grid(row=42, column=1,sticky="w")
        elif num_groups==4:
            g_3 = StringVar()
            Label(root, text='Title for Group_3: ').grid(row=42, column=0, pady=10,padx=10,sticky="e")    
            entry = Entry(root, textvariable=g_3).grid(row=42, column=1,sticky="w")
            g_4 = StringVar()
            Label(root, text='Title for Group_4: ').grid(row=43, column=0, pady=10,padx=10,sticky="e")    
            entry = Entry(root, textvariable=g_4).grid(row=43, column=1,sticky="w")

        Button(root, text='Proceed to Plot',command=root.destroy).grid(row=40, column=3, columnspan=3,pady=10, padx=10, sticky='e')
        root.mainloop()


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

    def init_plotter():
        global f
        global dataPlot



        f = Figure(figsize=(8,8), dpi=100)
        a = f.add_subplot(111)
        sns.scatterplot(data= principaldf,x= 'PC1 ' + '(' + str(pc1) + '% of variance' + ' )',
                        y= 'PC2 ' + '(' + str(pc2) + '% of variance' + ' )', 
                        ax=a,s=400, hue='Group',legend=False)


        dataPlot = FigureCanvasTkAgg(f, master=master)
        dataPlot.draw()
        #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
        dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)


    def applysliders():
        global fig
        global f
        global dataPlot
        global title
        global toggleexp
        global togglelabs
        global title
        global num_groups

        size=int(var2.get())
        #title=str(var5.get())
        toggleexp=int(var6.get())
        togglelabs=int(var7.get())   
        #title=str(var5.get())
        num_groups=int(var420.get())
        title="jobbybobby"
        
        f.clf()






        if num_groups== 2 and toggleexp==1:
            group1=principaldf[principaldf['Group'].str.contains(gp1)]
            group2=principaldf[principaldf['Group'].str.contains(gp2)]
            sns.set(font_scale=1.3)
            sns.set_style("white")
            #fig.clf()
            fig = Figure(figsize=(8,8), dpi=100)
            a = fig.add_subplot(111)
            sns.kdeplot(group1.x,group1.y,cmap="Reds",ax=a,shade=True,shade_lowest=False, n_levels=30)
            sns.kdeplot(group2.x,group2.y,cmap="Blues",ax=a,shade=True,shade_lowest=False, n_levels=30)
            #a.set_title(title) 
            a.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
            a.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
            ########a.set_title(title)
            dataPlot = FigureCanvasTkAgg(fig, master=master)

            dataPlot.draw()
            #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
            dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)

        if num_groups== 3 and toggleexp==1:
            group1=principaldf[principaldf['Group'].str.contains(gp1)]
            group2=principaldf[principaldf['Group'].str.contains(gp2)]
            group3=principaldf[principaldf['Group'].str.contains(gp3)]
            sns.set(font_scale=1.3)
            sns.set_style("white")
            #fig.clf()
            fig = Figure(figsize=(8,8), dpi=100)
            a = fig.add_subplot(111)
            sns.kdeplot(group1.x,group1.y,cmap="Reds",ax=a,shade=True,shade_lowest=False, n_levels=30)   
            sns.kdeplot(group2.x,group2.y,cmap="Blues",ax=a,shade=True,shade_lowest=False, n_levels=30)
            sns.kdeplot(group3.x,group3.y,cmap="Greens",ax=a,shade=True,shade_lowest=False, n_levels=30)
            #a.set_title(title) 
            a.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
            a.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
            ########a.set_title(title)
            dataPlot = FigureCanvasTkAgg(fig, master=master)
            dataPlot.draw()
            #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
            dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)

        if num_groups== 4 and toggleexp==1:
            group1=principaldf[principaldf['Group'].str.contains(gp1)]
            group2=principaldf[principaldf['Group'].str.contains(gp2)]
            group3=principaldf[principaldf['Group'].str.contains(gp3)]
            group4=principaldf[principaldf['Group'].str.contains(gp4)]
            sns.set(font_scale=1.3)
            sns.set_style("white")
            #fig.clf()
            fig = Figure(figsize=(8,8), dpi=100)
            a = fig.add_subplot(111)
            sns.kdeplot(group1.x,group1.y,cmap="Reds",ax=a,shade=True,shade_lowest=False, n_levels=30)   
            sns.kdeplot(group2.x,group2.y,cmap="Blues",ax=a,shade=True,shade_lowest=False, n_levels=30)
            sns.kdeplot(group3.x,group3.y,cmap="Greens",ax=a,shade=True,shade_lowest=False, n_levels=30)
            sns.kdeplot(group4.x,group4.y,cmap="Purples",ax=a,shade=True,shade_lowest=False, n_levels=30)
            #a.set_title(title) 
            a.set_xlabel('PC1 ' + '(' + str(pc1) + '% of variance' + ' )')
            a.set_ylabel('PC2 ' + '(' + str(pc2) + '% of variance' + ' )')
            
            dataPlot = FigureCanvasTkAgg(fig, master=master)
            dataPlot.draw()
            #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
            dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)
            ####a.set_title(title)

        elif toggleexp == 0:
            fig = Figure(figsize=(8,8), dpi=100)
            a = fig.add_subplot(111)
            sns.scatterplot(data= principaldf,x= 'PC1 ' + '(' + str(pc1) + '% of variance' + ' )',
                            y= 'PC2 ' + '(' + str(pc2) + '% of variance' + ' )', 
                            ax=a,s=size, hue='Group',legend=False)

            a.set_title(title)

            if togglelabs == 0:
                texts= []

                for x,y,s in zip(principaldf.x,(principaldf.y),principaldf.Sample):
                    texts.append(a.text(x,y,s,size=12))

                adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1),
                            arrowprops=dict(arrowstyle="-",color="black",lw=0.5))
                
            

            else:
                pass
            
            dataPlot = FigureCanvasTkAgg(fig, master=master)
            dataPlot.draw()
            #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
            dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)


        




    def save_fig():
        fig.savefig(fullpath + '//' + now + '_' + title + '_padplot_PCA.svg', format='svg', dpi=1200)
        #figure.savefig(title+ '_padplot_PCA.svg', format='svg', dpi=1200)
        #master.destroy()
        root = Tk()
        L = Label(root, text= ("Written to " + fullpath)).grid(row=6,column=0,padx=10, pady=10, )
        #figure.savefig(title+ '_padplot_PCA.svg', format='svg', dpi=1200)
        B = Button(root, text ="Close", command = root.destroy).grid(row=8,column=0,padx=10, pady=10, sticky='w')
        root.mainloop()
        
    def restart_main():
        master.destroy()
        main_gui()



    group_selection()

    control_group = [i for i in control_group if i != "0"]
    group_1 = [i for i in group_1 if i != "0"] 
    if num_groups==3:
        group_2 = [i for i in group_2 if i != "0"] 
    if num_groups==4:
        group_2 = [i for i in group_2 if i != "0"]
        group_3 = [i for i in group_3 if i != "0"]

    process_data()

    master = Tk()
    master.title("PadPlot_Live v1.2")

    var2= DoubleVar()
    var5 = StringVar()
    var6 = IntVar()
    var6.set(0)
    var7 = IntVar()
    var7.set(1)

    B = Button(master, text ="Initialise Plot", command = init_plotter).grid(row=1,column=1)
    var2 = DoubleVar()
    L = Label(master, text= "Define font-size").grid(row=3,column=1)
    point = Scale(master, from_=50, to=800,resolution=10,orient=HORIZONTAL,variable=var2)
    point.set(500)
    point.grid(row=3, column=2)

    L= Label(master, text="Choose plot style:").grid(row=5,column=1)
    R= Radiobutton(master, text="Standard",variable=var6, value=0).grid(row=5,column=2)
    R= Radiobutton(master, text="Density",variable=var6, value=1).grid(row=6,column=2)

    L= Label(master, text="Toggle labels on Standard Plot:").grid(row=7,column=1)
    R= Radiobutton(master, text="On",variable=var7, value=0).grid(row=7,column=2)
    R= Radiobutton(master, text="Off",variable=var7, value=1).grid(row=8,column=2)



    L = Label(master, text= "Define plot title").grid(row=9,column=1)
    E = Entry(master, textvariable=var5).grid(row=9,column=2)
    B = Button(master, text ="Update plot", command = applysliders).grid(row=10,column=1)
    B = Button(master, text ="Save plot", command = save_fig).grid(row=10,column=2)   
    B = Button(master, text ="Return to Main Menu", command = restart_main).grid(row=11,column=2)
    
    
    master.mainloop()
    
def volcano():
    global Fold_changes
    global g_1
    global root
    global padjs
    global gene_names
    global df

    #fullpath= "C:\\Users\\2087455F\\Desktop"



    now = datetime.now().time() 
    now=now.strftime('%H%M')



    df=pd.read_csv(csv_file_path)
    #l2fc=df["log2FoldChange"].tolist()
    #df["-logp"]=-(np.log(df["padj"]))
    #logp=df["-logp"].tolist()

    #col=0.05
    #coly=df["padj"]<col

    headers= list(df.columns.values)




    

    def exitout():
            root.destroy()
            sys.exit()

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

            root = Tk()
            root.title("PadPlot_Volcano v2.0")

            Label(root, text='Please select the column name which contains the Log2 Fold changes [one column only]').grid(row=0, column=0, columnspan=4, padx=10, pady=10)

            Label(root, text='Please select the column name which contains the Adjusted p-values [one column only]').grid(row=8, column=0, columnspan=4, padx=10, pady=10) 

            Label(root, text='Please select the column name which contains the Gene names [one column only]').grid(row=16, column=0, columnspan=4, padx=10, pady=10)

            Button(root, text='Proceed to Plot',command=root.destroy).grid(row=40, column=3, columnspan=3,pady=10, padx=10, sticky='e')

            #Button(root, text='Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=40, column=0, padx=10, pady=10, sticky='w',columnspan=3)

            cb = []
            cb_v = []
            for ix, text in enumerate(headers):
                cb_v.append(StringVar())
                off_value=0
                cb.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
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
            label = Label(root, width=20)
            #label.grid(row=ix+1, column=0, sticky='w')





            def chkbox_checked2():
                for ix, item in enumerate(cb2):
                    padjs[ix]=(cb_v2[ix].get())

            cb2 = []
            cb_v2= []
            for ix, text in enumerate(headers):
                cb_v2.append(StringVar())
                off_value=0
                cb2.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
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
            label = Label(root, width=20)
            #label.grid(row=ix+1, column=0, sticky='w')


            def chkbox_checked3():
                for ix, item in enumerate(cb3):
                    gene_names[ix]=(cb_v3[ix].get())

            cb3 = []
            cb_v3= []
            for ix, text in enumerate(headers):
                cb_v3.append(StringVar())
                off_value=0
                cb3.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
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
            label = Label(root, width=20)
            #label.grid(row=ix+1, column=0, sticky='w')
            root.mainloop()

            Fold_changes = [i for i in Fold_changes if i != "0"]
            padjs = [i for i in padjs if i != "0"]
            gene_names = [i for i in gene_names if i != "0"]

    def process_data():
        global df
        global Fold_changes
        global padjs
        global gene_names
        global l2fc
        global logp
        
        Fold_changes = [i for i in Fold_changes if i != "0"]
        padjs = [i for i in padjs if i != "0"]
        gene_names = [i for i in gene_names if i != "0"]
            
        fc_df = df.filter(Fold_changes)
        fc_df.columns= ['L2FC']

        p_df = df.filter(padjs)
        p_df.columns= ['p-value (Adjusted)']

        gene_df = df.filter(gene_names)
        gene_df.columns= ['Gene']

        df['L2FC'] = fc_df
        df['padj'] = p_df
        df['Gene'] = gene_df

        df['neglogp'] = - np.log(df['padj'])
        df['p(-log10)'] = - np.log10(df['padj'])
        
        l2fc=df["L2FC"].tolist()
        logp=df["neglogp"].tolist()
        



    def init_plotter():
        global f
        global dataPlot
        global df
        
        
        df=pd.read_csv(csv_file_path)
        
        process_data()
        
       

    
        
        col=0.05
        coly=df["padj"]<col
        
        



        f = Figure(figsize=(8,8), dpi=100)
        a = f.add_subplot(111)
        sns.scatterplot(l2fc,logp,s=10,hue=coly,ax=a)

        dataPlot = FigureCanvasTkAgg(f, master=master)
        dataPlot.draw()
        #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
        dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)



    def applysliders():
        global dataPlot    
        global dfmod20
        global df_select
        global df
        global coly
        global fig
        global title
        global legend_set

        df=pd.read_csv(csv_file_path)
        

        process_data()
        
        

        p=float(var.get())

        top_genes=int(var2.get())

        gene_filter=int(var3.get())

        title=str(var4.get())

        points=int(var5.get())
        
        legend_place=int(var840.get())

        custom_list=str(var6.get())
        custom_list=custom_list.split(',')


        df_select= df[df.Gene.isin(custom_list)]
        df_select['x']= df_select.L2FC
        df_select['y']= df_select.neglogp
        df_select['Gene2']= df_select.Gene

        df['test']=df['p(-log10)']
        df['test_2']=df['L2FC']
        df['outlier']=np.abs(df.test-df.test.mean()) <= (gene_filter*df.test.std())
        df['outlier_2']=np.abs(df.test_2-df.test_2.mean()) <= (gene_filter*df.test_2.std())
        df = df[df.outlier]
        df = df[df.outlier_2]

        df['x']= df.L2FC[0:top_genes]
        df['y']= df.neglogp[0:top_genes]
        df['Gene2']= df.Gene[0:top_genes]
        dfmod=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        dfmod20=dfmod.iloc[0:top_genes]
        dfmod20

        l2fc=df["log2FoldChange"].tolist()
        df["-logp"]=-(np.log(df["padj"]))
        logp=df["-logp"].tolist()


        coly=df["padj"]<p

        dataPlot.get_tk_widget().delete("all")
        dataPlot.get_tk_widget().pack_forget()

        fig = Figure(figsize=(8,8), dpi=100)
        a = fig.add_subplot(111)
        sns.scatterplot(l2fc,logp,s=points,hue=coly,ax=a)

        a.set_title(title)
        a.set_ylabel("-log p-value",fontsize=15)
        a.set_xlabel("log2 Fold Change",fontsize=15)

        legendlabel="FDR < " + str(p)



        if legend_place==0:
            a.get_legend().remove()        
        elif legend_place==1:
            #a.legend(loc="upper left")
            a.legend([legendlabel],loc="upper left")
        elif legend_place==2:
            #a.legend(loc="upper right")
            a.legend([legendlabel],loc="upper right")
        elif legend_place==3:
            #a.legend(loc='lower left')
            a.legend([legendlabel],loc="lower left")
        elif legend_place==4:
            #a.legend(loc='lower right')
            a.legend([legendlabel],loc='lower right')
        else:
            a.legend()

        texts=[]

        for x,y,s in zip(dfmod20.x,dfmod20.y+1,dfmod20.Gene2):
                    texts.append(a.text(x,y,s,size=10))

        for x,y,s in zip(df_select.x,df_select.y,df_select.Gene2):
                    texts.append(a.text(x,y,s,size=10))

        adjust_text(texts, precision=0.001,
            expand_text=(1.01, 1.05), expand_points=(1.01, 1.05),
            force_text=(0.25, 0.25), force_points=(0.01, 0.25),
            arrowprops=dict(arrowstyle='-', color='gray', alpha=.5))

        dataPlot = FigureCanvasTkAgg(fig, master=master)
        dataPlot.draw()
        #dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #dataPlot.get_tk_widget().grid(row=15,column=1,columnspan=5)
        dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)

    def save_fig():
        fig.savefig(fullpath + '//' + now + '_' + title + '_padplot_Volcano.svg', format='svg', dpi=1200)
        #figure.savefig(title+ '_padplot_PCA.svg', format='svg', dpi=1200)
        #master.destroy()
        root = Tk()
        L = Label(root, text= ("Written to " + fullpath)).grid(row=6,column=0,padx=10, pady=10, )
        #figure.savefig(title+ '_padplot_PCA.svg', format='svg', dpi=1200)
        B = Button(root, text ="Close", command = root.destroy).grid(row=8,column=0,padx=10, pady=10, sticky='w')
        root.mainloop()

    def restart_main():
        master.destroy()
        main_gui()




    gene_names_selection()

    process_data()

    

    master = Tk()
    master.title("PadPlot_Live v1.2")

    var = DoubleVar()
    var2 = DoubleVar()
    var3 = DoubleVar()
    var4 = StringVar()
    var5 = DoubleVar()
    var6 = StringVar()
    legend_set= IntVar()
    
    global dataPlot
    #df=pd.read_csv(csv_file_path)
    process_data()
    col=0.05
    coly=df["padj"]<col
    f = Figure(figsize=(8,8), dpi=100)
    a = f.add_subplot(111)
    sns.scatterplot(l2fc,logp,s=10,hue=coly,ax=a)
    dataPlot = FigureCanvasTkAgg(f, master=master)
    dataPlot.draw()
    dataPlot.get_tk_widget().grid(row=1,column=3,rowspan=30)
    
    



    B = Button(master, text ="Initialise Plot", command = init_plotter).grid(row=1,column=1)
    L = Label(master, text= "Define p-value for hue").grid(row=2,column=1)
    pval = Scale(master, from_=0.000001, to=0.1,resolution=0.001,orient=HORIZONTAL,variable=var)
    pval.set(0.05)
    pval.grid(row=2,column=2)
    L = Label(master, text= "Define top genes for labelling").grid(row=3,column=1)
    tops = Scale(master, from_=0, to=30,resolution=1,orient=HORIZONTAL,variable=var2).grid(row=3,column=2)
    L = Label(master, text= "Apply st-dev filtering to remove data outliers").grid(row=4,column=1)
    sds = Scale(master, from_=10, to=50,resolution=5,orient=HORIZONTAL,variable=var3).grid(row=4,column=2)
    L = Label(master, text= "Define size of points").grid(row=5,column=1)
    points = Scale(master, from_=2, to=40,resolution=1,orient=HORIZONTAL,variable=var5).grid(row=5,column=2)
    #points.set(20)
    #points.grid(row=5,column=2)
    L = Label(master, text= "Define plot title").grid(row=6,column=1)
    E = Entry(master, textvariable=var4).grid(row=6,column=2)
    L = Label(master, text= 'Provide a list of select genes, separated by ","').grid(row=7,column=1)
    E = Entry(master, textvariable=var6).grid(row=7,column=2)

    #L= Label(master,text="Toggle legend location:").grid(row=8,column=1)

    var840 = IntVar()
    var840.set(2)
    L= Label(master, text="Choose legend location:").grid(row=8,column=1)
    R= Radiobutton(master, text="Top Left",variable=var840, value=1).grid(row=8,column=2)
    R= Radiobutton(master, text="Top Right",variable=var840, value=2).grid(row=9,column=2)
    R= Radiobutton(master, text="Bottom Left",variable=var840, value=3).grid(row=10,column=2)
    R= Radiobutton(master, text="Bottom Right",variable=var840, value=4).grid(row=11,column=2)
    R= Radiobutton(master, text="No Legend",variable=var840, value=0).grid(row=12,column=2)
    
    '''
    MODES = {
        "No Legend":0,
        "Top Left":1,
        "Top Right":2,
        "Bottom Left":3,
        "Bottom Right":4,
        "Automatic":5
    }

    def boxtext(new_value):
        global legend_set
        legend_set=MODES[new_value]

    legend_set.set(5) 
    Opt = OptionMenu(master, legend_set, *MODES, command=boxtext).grid(row=8,column=2)
    '''


    B = Button(master, text ="Update plot", command = applysliders).grid(row=13,column=1)
    B = Button(master, text ="Save plot", command = save_fig).grid(row=13,column=2)
    B = Button(master, text ="Return to Main Menu", command = restart_main).grid(row=14,column=2)




    master.mainloop()
    
def heatmap():
    
    now = datetime.now().time() 
    now=now.strftime('%H%M')

    #fullpath= "C:\\Users\\2087455F\\Desktop"


    df=pd.read_csv(csv_file_path)
    #df=df.head(500)
    headers= list(df.columns.values)

    global gene_names
    global control_group
    global group_1


    def gene_names_selection():
        global gene_names
        global control_group
        global group_1
        global pval


        gene_names = []
        def chkbox_checked():
            for ix, item in enumerate(cb):
                gene_names[ix]=(cb_v[ix].get())

        root = Tk()
        root.title("PadPlot_Heatmap v1.0")

        Label(root, text='Please select the column name which contains the Gene Names [one column only]').grid(row=0, column=0, columnspan=4)  

        Label(root, text='Please select any column name which contains the data for your "Group1"').grid(row=10, column=0,columnspan=3)  

        Label(root, text='Please select any column name which contains the data for your "Group2"').grid(row=20, column=0,columnspan=3)

        Label(root, text='Please select any column name which contains the Adjusted P-value [one column only]').grid(row=30, column=0,columnspan=3)  
        #Button(root, text='Proceed to Labelling of Group1',command=root.destroy).grid(row=7, column=3, columnspan=3,pady=10, padx=10, sticky='e')
        Button(root, text='Proceed to Plot',command=root.destroy).grid(row=40, column=3, columnspan=3,pady=10, padx=10, sticky='e')
        #Button(root, text='CANCEL: Wipe variables here then hit "X" to cleanly exit',command=exitout).grid(row=9, column=0, padx=10, pady=10, sticky='w',columnspan=4)

        cb = []
        cb_v = []
        for ix, text in enumerate(headers):
            cb_v.append(StringVar())
            off_value=0
            cb.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
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
        label = Label(root, width=20)


        control_group = []
        def chkbox_checked1():
            for ix, item in enumerate(cb1):
                control_group[ix]=(cb_v1[ix].get())

        cb1 = []
        cb_v1 = []
        for ix, text in enumerate(headers):
            cb_v1.append(StringVar())
            off_value=0
            cb1.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                                 variable=cb_v1[ix],
                                 command=chkbox_checked1))
            if ix < 5:
                cb1[ix].grid(row=(ix+1)+10, column=0, sticky='w')
            elif ix >4 and ix < 10:
                cb1[ix].grid(row=(ix-4)+10, column=1, sticky='w')
            elif ix >9 and ix < 15:
                cb1[ix].grid(row=(ix-9)+10, column=2, sticky='w')
            elif ix >14 and ix < 20:
                cb1[ix].grid(row=(ix-14)+10, column=3, sticky='w')
            else:
                cb1[ix].grid(row=(ix-19)+10, column=4, sticky='w')
            control_group.append(off_value)
            cb1[-1].deselect()
        label = Label(root, width=20)


        group_1 = []
        def chkbox_checked2():
            for ix, item in enumerate(cb2):
                group_1[ix]=(cb_v2[ix].get())

        cb2 = []
        cb_v2 = []
        for ix, text in enumerate(headers):
            cb_v2.append(StringVar())
            off_value=0
            cb2.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                                 variable=cb_v2[ix],
                                 command=chkbox_checked2))
            if ix < 5:
                cb2[ix].grid(row=(ix+1)+20, column=0, sticky='w')
            elif ix >4 and ix < 10:
                cb2[ix].grid(row=(ix-4)+20, column=1, sticky='w')
            elif ix >9 and ix < 15:
                cb2[ix].grid(row=(ix-9)+20, column=2, sticky='w')
            elif ix >14 and ix < 20:
                cb2[ix].grid(row=(ix-14)+20, column=3, sticky='w')
            else:
                cb2[ix].grid(row=(ix-19)+20, column=4, sticky='w')
            group_1.append(off_value)
            cb2[-1].deselect()
        label = Label(root, width=20)


        pval = []
        def chkbox_checked3():
            for ix, item in enumerate(cb3):
                pval[ix]=(cb_v3[ix].get())

        cb3 = []
        cb_v3 = []
        for ix, text in enumerate(headers):
            cb_v3.append(StringVar())
            off_value=0
            cb3.append(Checkbutton(root, text=text, onvalue=text,offvalue=off_value,
                                 variable=cb_v3[ix],
                                 command=chkbox_checked3))
            if ix < 5:
                cb3[ix].grid(row=(ix+1)+30, column=0, sticky='w')
            elif ix >4 and ix < 10:
                cb3[ix].grid(row=(ix-4)+30, column=1, sticky='w')
            elif ix >9 and ix < 15:
                cb3[ix].grid(row=(ix-9)+30, column=2, sticky='w')
            elif ix >14 and ix < 20:
                cb3[ix].grid(row=(ix-14)+30, column=3, sticky='w')
            else:
                cb3[ix].grid(row=(ix-19)+30, column=4, sticky='w')
            pval.append(off_value)
            cb3[-1].deselect()
        label = Label(root, width=20)

        pval = [i for i in pval if i != "0"]
        gene_names = [i for i in gene_names if i != "0"]
        control_group = [i for i in control_group if i != "0"]
        group_1 = [i for i in group_1 if i != "0"]

        root.mainloop()

    def process_data():
        global temp
        global gene
        global title
        global samples
        global gene_names
        global control_group
        global group_1
        global pval

        gene_names = [i for i in gene_names if i != "0"]
        control_group = [i for i in control_group if i != "0"]
        group_1 = [i for i in group_1 if i != "0"]
        pval = [i for i in pval if i != "0"]

        samples=control_group+group_1
        cols = [x for x in headers if x not in samples]

        gp1="placehld"
        gp2="placehld_2"

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

    def init_plotter():
        global f
        global dataPlot
        global temp_adj
        global pval
        
        pvalley=pval[0]
        temp_adj=temp.where(temp[pvalley]<0.05)


        def plot():
            g= sns.clustermap(temp_adj.groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap="Greys",metric = 'correlation',z_score=0)
            return g.fig


        figure= plot()
        dataPlot = FigureCanvasTkAgg(figure, master=master)
        dataPlot.draw()
        dataPlot.get_tk_widget().grid(row=1,column=3,rowspan= 30)

    def applysliders():
        global f
        global dataPlot
        global temp_adj
        global figure
        global title
        global pval
        global colo
        global p

        p=float(var6.get())
        fontsize=float(var2.get())
        xfont=float(var3.get())
        title= str(var5.get())
        #colo=str(var4.get())
        colo=colo
        title=str(var5.get())

        pvalley=pval[0]

        temp_adj=temp.where(temp[pvalley]<p)
        sns.set(font_scale=fontsize)


        def plot():
            g= sns.clustermap(temp_adj.groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap=colo,metric = 'correlation',z_score=0)
            g.ax_heatmap.set_xticklabels(g.ax_heatmap.get_xmajorticklabels(), fontsize = xfont)
            return g.fig


        figure= plot()
        dataPlot = FigureCanvasTkAgg(figure, master=master)
        dataPlot.draw()
        dataPlot.get_tk_widget().grid(row=1,column=3,rowspan= 30)
        
        #temp_adj=None
        #p=None

        #return figure


    def save_fig():
        figure.savefig(fullpath + '//' + now + '_' + title + '_padplot_Heatmap.svg', format='svg', dpi=1200)
        root = Tk()
        L = Label(root, text= ("Written to " + fullpath)).grid(row=6,column=0,padx=10, pady=10, )
        #figure.savefig(title+ '_padplot_PCA.svg', format='svg', dpi=1200)
        B = Button(root, text ="Close", command = root.destroy).grid(row=8,column=0,padx=10, pady=10, sticky='w')
        root.mainloop()


    gene_names_selection()
    process_data()
    
    def restart_main():
        master.destroy()
        main_gui()





    master = Tk()
    master.title("PadPlot_Live v1.2")

    var = DoubleVar()
    var2 = DoubleVar()
    var3 = DoubleVar()
    colo = StringVar()
    var5 = StringVar()
    var6 = DoubleVar()

    B = Button(master, text ="Initialise Plot", command = init_plotter).grid(row=1,column=1)
    #L = Label(master, text= "Define p-value for hue").grid(row=2,column=1)
    #E1 = Entry(master, textvariable=var)
    #E1.insert(END, '5')
    #E1.grid(row=2,column=2)
    
    L = Label(master, text= "Define p-value for hue").grid(row=2,column=1)
    pval = Scale(master, from_=0.0000000001, to=0.1,resolution=0.000000001,orient=HORIZONTAL,variable=var6)
    pval.set(0.05)
    pval.grid(row=2,column=2)
    
    L = Label(master, text= "Define Gene-Names font-size").grid(row=3,column=1)
    font = Scale(master, from_=0.01, to=2,resolution=0.01,orient=HORIZONTAL,variable=var2)
    font.set(1)
    font.grid(row=3,column=2)
    L = Label(master, text= "Define Sample-Names font-size").grid(row=4,column=1)
    fontx = Scale(master, from_=5, to=20,resolution=1,orient=HORIZONTAL,variable=var3)
    fontx.set(10)
    fontx.grid(row=4,column=2)

    L = Label(master,text="Define colour:").grid(row=5,column=1)



    MODES = {
        "Yellow, Orange and Red":"YlOrRd",
        "Orange and Red":"OrRd",
        "Blue and Red":"bwr",
        "Red and Purple":"RdPu",
        "Hot":"hot",
        "Standard": "magma",
        
    }


    def boxtext(new_value):
        global colo
        colo=MODES[new_value]


    colo.set("magma") 
    p = OptionMenu(master, colo, *MODES, command=boxtext).grid(row=5,column=2)
    L = Label(master, text= "Define plot title").grid(row=6,column=1)
    E = Entry(master, textvariable=var5).grid(row=6,column=2)

    #B = Button(master, text ="Update plot", command = applysliders).grid(row=10,column=1)
    B = Button(master, text ="Update plot", command = applysliders).grid(row=7,column=1)
    B = Button(master, text ="Save plot", command = save_fig).grid(row=7,column=2)
    B = Button(master, text ="Return to Main Menu", command = restart_main).grid(row=8,column=2)
    master.mainloop()

def main_gui():
    global var420
    global read
    
    read=0

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

            global fullpath
            #global y

            fullpath= askdirectory()
            #print(fullpath)
        
    def debug_options():
        root = Tk()
        root.title("PadPlot_Debug v1.0")
        #tk.Label(root, text="Padplot cannot function unless given an appropriare file. Common errors include").grid(row=0, column=0, padx=10, pady=10,sticky='w')
        Label(root, text="Please ensure the following requirements are met:").grid(row=1, column=0, padx=10, pady=1,sticky='w')
        Label(root, text="1) The file is a .csv and not a .xls file").grid(row=2, column=0, padx=10,sticky='w')
        Label(root, text="2) The top row of the .csv file consists of column names").grid(row=3, column=0, padx=10,sticky='w')
        Label(root, text="3) The .csv file consists only of columns").grid(row=4, column=0, padx=10,sticky='w')
        B = Button(root, text ="Close", command = root.destroy).grid(row=8,column=0,padx=10, pady=10, sticky='w')
    


    root = Tk()
    root.title("PadPlot_Main v1.2") 
    #root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    
    Label(root, text="Welcome to PadPlot, as a safety feature, Padplot will not create or remove folders.\n PadPlot will write figures to a folder of your choice.").grid(row=0, column=1, padx=20, pady=20,columnspan=5)
    #tk.Label(root, text='Choose a folder to save plots to:').grid(row=1, column=1,padx=20, pady=20,sticky="e")
    
    Button(root, text='Choose an RNA-seq csv file to plot',command=import_csv_data).grid(row=1, column=2,padx=20, pady=20)
    if read ==1:
        fileread= Label(root, text="File Read").grid(row=2,column=0,padx=20, pady=20,columnspan=5)
    else:
        pass
    root.update()
    Button(root, text='Choose a folder to save plots to',command=get_figure_path).grid(row=3, column=2,padx=20, pady=20)
    
    
    var420 = IntVar()
    var420.set(2)
    L= Label(root, text="Choose number of Groups:").grid(row=5,column=0,padx=20, pady=20,columnspan=5)
    R= Radiobutton(root, text="Two",variable=var420, value=2).grid(row=6,column=1,sticky="e")
    R= Radiobutton(root, text="Three",variable=var420, value=3).grid(row=6,column=2)
    R= Radiobutton(root, text="Four",variable=var420, value=4).grid(row=6,column=3,stick="w")
    
    Label(root, text="Please choose your plot").grid(row=8, column=0, padx=20, pady=20,columnspan=5)
    button = Button(root, text="PCA",command=sel_pca).grid(row=9, column=1,pady=10, padx=10)
    button2 = Button(root, text="Volcano",command=sel_volcano).grid(row=9, column=2,pady=10, padx=10)
    button3 = Button(root, text="Heat Map",command=sel_heatmap).grid(row=9, column=3,pady=10, padx=10)
    Label(root, text="PadPlot authored by SimonF92, contact me at s.fisher.1@research.gla.ac.uk").grid(row=15, column=0, padx=20, pady=20,columnspan=5)
    button5= Button(root, text='Help',command=debug_options).grid(row=34, column=1, padx=10, pady=10, sticky='w')
    button4= Button(root, text='Cancel',command=exitout).grid(row=35, column=1, padx=10, pady=10, sticky='w')
    
    root.mainloop()


    if sel == 1:
        pca()
    elif sel == 2:
        volcano()
    else:
        heatmap()
        

        
main_gui()
    