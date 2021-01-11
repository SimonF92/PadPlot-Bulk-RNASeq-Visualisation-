import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style("white")
import adjustText
from adjustText import adjust_text
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import gseapy as gp
from gseapy.plot import gseaplot, heatmap
import matplotlib.gridspec as gridspec

st.beta_set_page_config(layout="centered")
initial_sidebar_state="expanded"

def _max_width_():
    max_width_str = f"max-width: 1300px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )




def loaddata():
    global df
    global headers
    global log2s
    global paddys
    global genenames
    global temp
    global gene
    global controlg
    global expg
    global title
    global pim

    st.header("Next point PadPlot to the Relevant Columns")
    
        
    df=pd.read_csv(data)
    #st.dataframe(df)
    
    headers= list(df.columns.values)
    title=data.name
       
def loaddata():
    global df
    global headers
    global log2s
    global paddys
    global genenames
    global temp
    global gene
    global controlg
    global expg
    global group1_title
    global group2_title
    global schema
    global statmethod
    global gene_set
    global permtype
    #st.dataframe(df.head(20))

    st.header("Next select a Global Style for Plots")

    STYLES = {
        "White":"white",
        "Dark grid": "darkgrid",
        "Dark": "dark",
        "White Grid":"whitegrid",
        "Ticks":"ticks",
        
        
    }

    schemes= list(STYLES.keys())

    sch = st.selectbox("Define a plot schema", schemes)
    schema= STYLES.get(sch)

    st.text("")
    st.text("")
    st.text("")

    st.header("Finally point PadPlot to the Relevant Columns")
    
    data.seek(0)  
    df=pd.read_csv(data)

    #dfprocesses=pd.read_csv('mart_export.txt')

    headers= list(df.columns.values)

    stat_methods=['signal_to_noise','t_test','ratio_of_classes','diff_of_classes','log2_ratio_of_classes']

    gene_sets=['GO_Molecular_Function_2018','GO_Biological_Process_2018','KEGG_2019_Human','MGI_Mammalian_Phenotype_Level_4_2019']
    
    
    col1, col2, col3= st.beta_columns(3)

    genenames = col1.selectbox("Select Gene Names", headers)
    paddys = col2.selectbox("Select Adjusted p-values", headers)
    log2s = col3.selectbox("Select Log2 Fold Changes", headers)
    
    controlg = st.multiselect("Select Control Group", headers)
    expg = st.multiselect("Select Experimental Group", headers)

    col4, col5= st.beta_columns(2)

    group1_title = col4.text_input("Define Group 1 Title Here", 'ie "Control"')
    group2_title = col5.text_input("Define Group 2 Title Here", 'ie "Experimental"')

    st.text("")
    st.text("")

    st.header("Customise Gene Set Enrichment Parameters (Human Data Only)")

    col6, col7, col8=st.beta_columns(3)

    statmethod = col6.selectbox("Gene Set Enrichment Method", stat_methods)

    gene_set= col7.selectbox("Gene Set Enrichment Reference Database", gene_sets)

    permtype= col8.selectbox("Gene Set Enrichment Permutation Type (Phenotype only if samples > 15", ['gene_set','phenotype'])

    


def selectplot():

    st.text("")
    st.text("")
    st.text("")

    options = [
        "PadPlot Volcano",
        "PadPlot Heatmap",
        "PadPlot PCA",
        "PadPlot Violin",
        "PadPlot Gene Set Enchrichment (Human Only)",
        
        
    ]

    #padplots= list(OPTIONS.keys())

    st.header("Choose a plot:")

    plot = st.selectbox("Define a plot schema", options)
   



    if plot== "PadPlot Volcano":
        volcanoplot()
        

    elif plot== "PadPlot Heatmap":
        heatmapplot()

    elif plot== "PadPlot PCA":
        pcaplot()

    elif plot== "PadPlot Violin":
        violinplot()

    elif plot== "PadPlot Gene Set Enchrichment (Human Only)":
        geneset_enrichment()

    else:
        st.header("No Plot Currently Selected")



def pcaplot():

    st.sidebar.header("Change PCA-plot Parameters")

    
    

    pca_df=df[controlg+expg]
    genes=len(pca_df)
    pca_df=pca_df.transpose()




    logdata = st.sidebar.checkbox('Log PCA Input Values')

    if logdata:
        pca_df=np.log((pca_df+1))
        title='Logged Values'
    else:
        pca_df=pca_df
        title='Raw Values'



    pca_df['Sample']=pca_df.index
    #st.dataframe(pca_df)

    labelsize=st.sidebar.slider('Size of text labels', 2, 20, 8)

    





    g1= [group1_title]
    g1=g1* len(controlg)
    
    g2= [group2_title]
    g2=g2*len(expg)

    grouping=g1+g2

    pca_df['Group']= grouping





    

    

    #st.dataframe(pca_df)

    features = range(0,genes,1)
    x=pca_df.loc[:,features].values
    y=pca_df.loc[:,['Sample']].values
    #x=StandardScaler().fit_transform(x)

    pca=PCA()
    principalComponents=pca.fit_transform(x)
    ex_variance=np.var(principalComponents,axis=0)
    ex_variance_ratio=ex_variance/np.sum(ex_variance)
    pc1=round((ex_variance_ratio[0] * 100), 1)
    pc2=round((ex_variance_ratio[1] * 100), 1)


    pcx= [i[0] for i in principalComponents]
    pcy= [i[1] for i in principalComponents]
    #pc2

    principaldf=pd.DataFrame(data=zip(pcx,pcy),columns=['PC1 ' + '(' + str(pc1) + '% of variance' + ' )','PC2 ' + '(' + str(pc2) + '% of variance' + ' )'])#,raise_missing=False)
    principaldf['Sample']=pca_df.index
    principaldf['Group']= grouping
    principaldf['x']=principaldf['PC1 ' + '(' + str(pc1) + '% of variance' + ' )']
    principaldf['y']=principaldf['PC2 ' + '(' + str(pc2) + '% of variance' + ' )']

    #st.dataframe(principaldf)

    

    with sns.axes_style(schema):
        fig = plt.figure(figsize=(8,8))        
        ax = fig.add_subplot(1, 1, 1)
        sns.scatterplot(data= principaldf,x= 'PC1 ' + '(' + str(pc1) + '% of variance' + ' )',
                        y= 'PC2 ' + '(' + str(pc2) + '% of variance' + ' )', 
                        ax=ax,s=400, hue=principaldf.Group.tolist())

        plt.title(title,loc='left')

        texts= []

        for x,y,s in zip(principaldf.x,(principaldf.y),principaldf.Sample):
            texts.append(ax.text(x,y,s,size=labelsize))

        adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1))

    st.pyplot(fig)




def violinplot():

    st.sidebar.header("Change Violin-plot Parameters")

    


    df2=df

    samples=controlg+expg

    

    


    cols = [x for x in headers if x not in samples]
    gp1=group1_title
    gp2=group2_title
    g1= [gp1]
    g2= [gp2]
    grouping= (g1 * len(controlg)) + (g2 * len(expg))
    temp = (df2[headers].melt(id_vars = cols, var_name = 'Sample',value_name = 'Expression'))

    temp=temp.dropna()



    logviolin = st.sidebar.checkbox('Log Expression Input Values')

    

    if logviolin:
        temp['Expression']=np.log((temp['Expression']+1))
        title='       Logged Values'
    else:
        temp['Expression']=temp['Expression']
        title='       Raw Values'

    

    #st.markdown(controlg)
    low_samples = controlg
    temp['Group'] = temp['Sample'].apply(lambda x : gp1 if x in low_samples else gp2)

    

    with sns.axes_style(schema):

        fig = plt.figure(figsize=(8,8))        
        ax = fig.add_subplot(1, 1, 1)

        grouped = st.sidebar.checkbox('Sample Grouping')

        if grouped:
            sns.violinplot(data= temp,x='Sample',y='Expression',hue='Group',dodge=False)

        else:
            sns.violinplot(data= temp,x='Sample',y='Expression')

        jitter = st.sidebar.checkbox('Add Jitter')

    

        if jitter:
            jittersize=st.sidebar.slider('Size of points', 0, 10, 1)
            jitteralpha=st.sidebar.slider('Opacity of points', float(0), float(1), float(0.2))
            sns.stripplot(data= temp,x='Sample',y='Expression',alpha=jitteralpha,s=jittersize,color='black',jitter=0.4)
        
        else:
            pass
        
        locs, labels = plt.xticks()
        plt.setp(labels, rotation=45)
        plt.title(title,loc='left')

        

    st.pyplot(fig)






def prepdata():
    global l2fc
    global logp
    global df
    global ps

    df= df.sort_values(by=[paddys])

    Fold_changes = log2s
    padjs = paddys
    gene_names = genenames

    fc_df = df.filter([Fold_changes])
    fc_df.columns= ['L2FC']

    p_df = df.filter([padjs])
    p_df.columns= ['p-value (Adjusted)']

    gene_df = df.filter([gene_names])
    gene_df.columns= ['Gene']

    df['L2FC'] = fc_df
    df['padj'] = p_df
    df['Gene'] = gene_df
    df['neglogp'] = - np.log(df['padj'])
    df['p(-log10)'] = - np.log10(df['padj'])  
    ps=df["padj"].tolist()     
    l2fc=df["L2FC"].tolist()
    logp=df["neglogp"].tolist()

    #st.dataframe(df)

def volcanoplot():
    

    
    
    st.sidebar.header("Change Volcano-plot Parameters")

    option = st.sidebar.selectbox('Choose Volcano Type',('Standard', 'Gene Ontology (Human Only)'))
    
    p=st.sidebar.slider('p-value threshold', float(min(ps)), float(max(ps)), 0.05)
    top_genes=st.sidebar.slider('Label top genes', 0, 30, 5)
    textsize=st.sidebar.slider('Size of labels', 0, 20, 8)
    x=st.sidebar.slider('Adjust x-axis', float(0), float(max(l2fc)+2), float(max(l2fc)+2))
    y=st.sidebar.slider('Adjust y-axis', float(0), max(logp)+10, (max(logp)+10))
    size=st.sidebar.slider('Point Size', float(1), float(50), float(25))

   

    if option=='Gene Ontology (Human Only)':

        st.error('Currently In Development')

        '''

        st.sidebar.header("Biological Process Labelling Input (Human Only)")

        user_input = st.sidebar.text_input("Enter GO Processes here separated by commas, ie 'Sodium, Receptor, Membrane, Pregnancy'")
        user_list=user_input.split(',')
        st.text(user_list)
      
        
        
        @st.cache(suppress_st_warning=True)
        def prepmartdata():
  
            st.write("Cache miss: expensive_computation ran")
            
            dfprocesses=pd.read_csv('mart_export.txt')
            df2=dfprocesses.merge(df, right_on='Row.names', left_on='Gene stable ID', how='outer')
            df2=df2.dropna(subset=['Unnamed: 0', 'Row.names','padj','GO term name'])
            return df2
            
            
           
        df2=prepmartdata()

        
       

        remove_list = user_list
        df2['flagCol'] = np.where(df2['GO term name'].str.contains('|'.join(remove_list)),1,0)
        df2['flagCol'] = df2['flagCol'].replace(0, np.nan)
        dfflagged=df2.dropna(subset=['flagCol'])
        genes=dfflagged['external_gene_name'].values.tolist()
        genes = set(genes)
        genes = list(genes)

        df2['Flagged by keywords ' + str(remove_list)]= df2['external_gene_name'].isin(genes)
        df3= df2[df2['Flagged by keywords ' + str(remove_list)].astype(str).str.contains('True')]
        df3=df3.drop_duplicates(subset=['external_gene_name'])

        

        df3=df3.sort_values(by=['padj'])

        df3['x']= df3.log2FoldChange
        df3['y']= df3.neglogp
        df3['Gene2']= df3.external_gene_name
        
        dfgolabels=df3.iloc[0:top_genes]

        
        
        df['Flagged by keywords ' + str(remove_list)]= df['external_gene_name'].isin(genes)
        coly=df['Flagged by keywords ' + str(remove_list)].values.tolist()

        with sns.axes_style(schema):
            fig = plt.figure(figsize=(8,8))        
            ax = fig.add_subplot(1, 1, 1)
            sns.scatterplot(l2fc,logp,hue=coly,s=size,ax=ax)
            ax.set_ylabel("-log p-value",fontsize=15)
            ax.set_xlabel("log2 Fold Change",fontsize=15)
            plt.ylim(0, y)
            plt.xlim((-x), x)
            plt.title(title)


            legendlabel='Flagged by keywords ' + str(remove_list)
            ax.legend([legendlabel],loc="upper right")

            texts=[]
            props= dict(boxstyle='round', facecolor='wheat', alpha=0.9)

            for x,y,s in zip(dfgolabels.x,dfgolabels.y,dfgolabels.Gene2):
                        texts.append(ax.text(x,y,s,size=textsize,bbox=props))

            adjust_text(texts)

            

            
        
            

            st.pyplot(fig)

            '''

        

    else:

        

        df['x']= df.L2FC[0:top_genes]
        df['y']= df.neglogp[0:top_genes]
        df['Gene2']= df.Gene[0:top_genes]
        dfmod=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        dfmod20=dfmod.iloc[0:top_genes]

        df['coly']=df["padj"]<p
        coly=df['coly'].values.tolist()
        
        with sns.axes_style(schema):
            fig = plt.figure(figsize=(8,8))        
            ax = fig.add_subplot(1, 1, 1)
            sns.scatterplot(l2fc,logp,hue=coly,s=size,ax=ax)
            ax.set_ylabel("-log p-value",fontsize=15)
            ax.set_xlabel("log2 Fold Change",fontsize=15)
            plt.ylim(0, y)
            plt.xlim((-x), x)
            plt.title(title)


            legendlabel="FDR < " + str(p)
            ax.legend([legendlabel],loc="upper right")

            texts=[]

            for x,y,s in zip(dfmod20.x,dfmod20.y,dfmod20.Gene2):
                        texts.append(ax.text(x,y,s,size=textsize))

            adjust_text(texts)

            

            
        
            

            st.pyplot(fig)




def heatmapplot():
    #p2=0.05
    #delta= st.sidebar.number_input("Adjust p-value:", min_value=float(0.0001), max_value=float(1),value=float(0.05),step=0.005)
    #st.write(delta)
    #p2=st.slider('p-value threshold', min(ps), 0.05, 0.0005)
    st.sidebar.header("Change Heatmap Parameters")
    user_input = st.sidebar.text_input("Threshold adjusted p-value at (enter a value)", 0.05)
    delta=float(user_input)
    fontsize=st.sidebar.slider('Set gene names font size', 0.01, float(1.5), float(1))
    xfont=st.sidebar.slider('Set sample names font size', 2, 20, 10)
    sns.set(font_scale=fontsize)
    
    MODES = {"Standard": "magma",
        "Yellow, Orange and Red":"YlOrRd",
        "Orange and Red":"OrRd",
        "Blue and Red":"bwr",
        "Red and Purple":"RdPu",
        "Hot":"hot"
        
        
    }
    x= list(MODES.keys())
    c = st.sidebar.selectbox("Define a colour-scheme", x)
    colour= MODES.get(c)
    
    
    df2=df.where(df[paddys]<delta)
    samples=controlg+expg
    cols = [x for x in headers if x not in samples]
    gp1="placehld"
    gp2="placehld_2"
    g1= [gp1]
    g2= [gp2]
    grouping= (g1 * len(controlg)) + (g2 * len(expg))
    temp = (df2[headers].melt(id_vars = cols, var_name = 'Sample',value_name = 'Expression'))
    #st.markdown(controlg)
    low_samples = controlg
    temp['Group'] = temp['Sample'].apply(lambda x : gp1 if x in low_samples else gp2)
    gene=genenames

    global temp_adj




    def plot():
        g= sns.clustermap(temp.groupby([gene, 'Sample'])['Expression'].mean().unstack(),cmap=colour,metric = 'correlation',z_score=0)
        g.ax_heatmap.set_xticklabels(g.ax_heatmap.get_xmajorticklabels(), fontsize = xfont)
        return g.fig

    #st.table(temp_adj)
    figure= plot()
    st.pyplot(figure)


def geneset_enrichment():
    
    gseaselect=[genenames]+controlg+expg
    gene_exp=df[gseaselect]



    gene_exp=gene_exp.sort_values(by=gene_exp.columns[2])
    gene_exp=gene_exp.tail(7000)

    #st.dataframe(gene_exp.head(5))

    # gene_sets='GO_Biological_Process_2018','GO_Molecular_Function_2018','KEGG_2019_Human'
    # gene_sets='MGI_Mammalian_Phenotype_Level_4_2019'
    # gene_sets='GO_Molecular_Function_2018'

    gp1="placehld"
    gp2="placehld_2"
    g1= [gp1]
    g2= [gp2]
    grouping= (g1 * len(controlg)) + (g2 * len(expg))

    @st.cache(suppress_st_warning=True,allow_output_mutation=True)
    def calculate_genesets():
        gs_res = gp.gsea(data=gene_exp, # or data='./P53_resampling_data.txt'
                        gene_sets=gene_set, # enrichr library names
                        cls= grouping, # cls=class_vector
                        # set permutation_type to phenotype if samples >=15
                        permutation_type=permtype,
                        permutation_num=100, # reduce number to speed up test
                        outdir=None,  # do not write output to disk
                        no_plot=True, # Skip plotting
                        method=statmethod, # or t_test
                         seed= 7,
                        format='png')

        return(gs_res)

    

    
    gs_res=calculate_genesets()
    st.success('Gene Set Enrichment Successful')



    terms = gs_res.res2d.index
    fdrs= gs_res.res2d['fdr']

    reindexed=gs_res.res2d.reset_index()
    st.dataframe(reindexed)

    processes = st.selectbox("Enriched Processes in Your Dataset (Choose one to visualise)", terms)
    keepGO= str(processes[-len(processes):])
    #st.text(keepGO)

    

    #ids = np.unique(reindexed.stack()[reindexed.astype('str').str.contains(keepGO)].index.get_level_values(0))
    ids= reindexed.index[reindexed['Term'] ==keepGO].tolist()
    #st.text(ids)
    





    def plot(n):
        #st.text(n)
        genes = gs_res.res2d.genes[n].split(";")
        #st.dataframe(genes)

        dfprocess= gs_res.heatmat.loc[genes]

        control_mean= dfprocess.iloc[:,:3].mean(axis=1)
        exp_mean= dfprocess.iloc[:,3:].mean(axis=1)
        dfprocess_mean=pd.DataFrame()
        dfprocess_mean['Control_mean']=control_mean
        dfprocess_mean['Experimental_mean']=exp_mean
        dfprocess_mean['Divided']=(dfprocess_mean['Control_mean']/dfprocess_mean['Experimental_mean'])
        dfprocess_mean=np.log(dfprocess_mean[['Divided']])
        dfprocess_mean=dfprocess_mean.sort_values(by='Divided',ascending='False')
        
        
        grid=sns.clustermap(data=dfprocess_mean.T ,z_score=0, col_cluster=False,row_cluster=False, figsize=(18,4),cmap='RdBu_r', dendrogram_ratio=0.0,cbar_pos=None)
        labels=grid.ax_heatmap.get_xticklabels()
        grid.ax_heatmap.set_xticklabels(labels=labels, rotation=60, fontsize = 16)
        labels=grid.ax_heatmap.get_yticklabels()
        grid.ax_heatmap.set_yticklabels(labels=labels, fontsize = 16)

        grid.ax_heatmap.set_title(terms[n] + ',  FDR: ' + str(round(fdrs[n],3)),size=17)
        
        return grid


    indexes=ids

    for value in indexes:
        figure=plot(value)
        st.pyplot(figure)

    
    
    

    
    def fullgenesets():
        fig, ax = plt.subplots(figsize=(3,len(fullset_head)/4)) 
        scatterplot=ax.scatter(y=fullset_head.index,x=fullset_head['neglogp'],c=fullset_head['nes'],cmap='seismic',edgecolors='black',s=60)



        cbar= plt.colorbar(scatterplot, orientation="horizontal", pad=2.8/len(fullset_head))

        cbar.set_label("Normalised\nEnrichment Score")


        plt.title('Enriched Pathways and Functions',size=12)
        plt.xlabel('FDR (-log)')
        

        st.pyplot(fig)


    

    gseaplot = st.sidebar.checkbox('Display GSEA Bubble Plot')

    if gseaplot:

        fullset=gs_res.res2d
        
        fullset['neglogp']= -np.log(fullset['fdr'])
        fullset=fullset.sort_values(by='neglogp',ascending=False)

        head=st.sidebar.slider('Number of Pathways', 0, 50, 20)

        fullset_head=fullset.head(head)
        fullset_head=fullset_head.sort_values(by='neglogp')

        fullgenesets()
                

_max_width_()  	

#load=st.checkbox("Load Data")
st.title("Welcome to PadPlot")

st.header("Start by Providing your Dataset")


data = st.file_uploader("Upload a Dataset", type=["csv", "txt","tsv"])

if not data:
    st.warning('Please input a file.')
    st.stop()
st.success('Dataset loaded.')
#st.success('Dataframe loaded')
title=data.name



st.text("")
st.text("")
st.text("")



loaddata()


prepdata()


selectplot()

#if load:
#    loaddata()
#    prepdata()

# if data not in globals():
#     st.error('No File Loaded')

st.text("")
st.text("")
st.text("")
st.text("")



st.text("")


st.text("")
st.text("")




c1, c2 = st.beta_columns((2))
c3, c4 = st.beta_columns((2))



