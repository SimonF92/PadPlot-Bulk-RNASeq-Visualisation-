import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style("white")
import adjustText
from adjustText import adjust_text
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

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

st.title("Welcome to PadPlot, by Simon Fisher @ McBride Group Glasgow University")

st.text("")

st.text("Remote Glasgow University Users Readme")
st.text("This remote version of PadPlot is running from an Amazon Machine. My personal debit card acts as a security against usage of this machine. \n You are being trusted with this IP address. Please do not attempt to store anything on this IP. \n Additionally, the machine has 1Gb Ram and 1CPU core, it will be slow. \n My advice would be to not toggle all of the graphs as you edit- and be patient!")

st.text("")

st.header("Start by Providing your Dataset")


data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
#st.success('Dataframe loaded')
title=data.name
st.text("")
st.text("")
st.text("")


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
    headers= list(df.columns.values)
    
    
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
    st.text("")



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
    x=StandardScaler().fit_transform(x)

    pca=PCA(n_components=2)
    principalComponents=pca.fit_transform(x)
    ex_variance=np.var(principalComponents,axis=0)
    ex_variance_ratio=ex_variance/np.sum(ex_variance)
    pc1=round((ex_variance_ratio[0] * 100), 1)
    pc2=round((ex_variance_ratio[1] * 100), 1)
    #pc2

    principaldf=pd.DataFrame(data=principalComponents,columns=['PC1 ' + '(' + str(pc1) + '% of variance' + ' )','PC2 ' + '(' + str(pc2) + '% of variance' + ' )'])#,raise_missing=False)
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
                        ax=ax,s=400, hue='Group',legend=False)

        plt.title(title,loc='left')

        texts= []

        for x,y,s in zip(principaldf.x,(principaldf.y),principaldf.Sample):
            texts.append(ax.text(x,y,s,size=labelsize))

        adjust_text(texts,force_points=0.1, force_text=0.2, expand_points=(1,1))

    c3.pyplot(fig)




def violinplot():

    st.sidebar.header("Change Violin-plot Parameters")

    


    df2=df

    samples=controlg+expg

    

    


    cols = [x for x in headers if x not in samples]
    gp1="placehld"
    gp2="placehld_2"
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
        

        plt.title(title,loc='left')

        

    c4.pyplot(fig)






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
    
    p=st.sidebar.slider('p-value threshold', float(min(ps)), float(max(ps)), 0.05)
    top_genes=st.sidebar.slider('Label top genes', 0, 30, 5)
    textsize=st.sidebar.slider('Size of labels', 0, 20, 8)
    x=st.sidebar.slider('Adjust x-axis', float(0), float(max(l2fc)+2), float(max(l2fc)+2))
    y=st.sidebar.slider('Adjust y-axis', float(0), max(logp)+10, (max(logp)+10))
    size=st.sidebar.slider('Point Size', float(1), float(50), float(25))

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

        c1.pyplot(fig)

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
    c2.pyplot(figure)

_max_width_()  	

#load=st.checkbox("Load Data")



loaddata()


prepdata()

#if load:
#    loaddata()
#    prepdata()

# if data not in globals():
#     st.error('No File Loaded')

st.text("")
st.text("")
st.text("")
st.text("")


st.header("Choose a plot:")
st.text("")
st.header("It is recommended that when editing fine detail of plots, you do not have them all loaded. Hit the top right side of the plot to enter fullscreen mode")

st.text("")
st.text("")

vol, heat, princ, viol = st.beta_columns(4)

volcano=vol.checkbox("PadPlot Volcano")
heatmap=heat.checkbox("PadPlot Heatmap")
pca=princ.checkbox("PadPlot PCA")
violin=viol.checkbox("PadPlot Violin")

st.text("")
st.text("")


c1, c2 = st.beta_columns((2))
c3, c4 = st.beta_columns((2))


if volcano:
    volcanoplot()
    

if heatmap:
    heatmapplot()

if pca:
    pcaplot()

if violin:
    violinplot()
