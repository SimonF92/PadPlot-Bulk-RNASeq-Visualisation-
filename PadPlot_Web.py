import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style("white")
import adjustText
from adjustText import adjust_text

def _max_width_():
    max_width_str = f"max-width: 800px;"
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

st.title("Welcome to PadPlot")

st.header("Start by Providing your Dataset")

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])


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

    st.header("Next point PadPlot to the Relevant Columns")
    
        
    df=pd.read_csv(data)
    #st.dataframe(df)
    headers= list(df.columns.values)
    genenames = st.selectbox("Select Gene Names", headers)
    paddys = st.selectbox("Select Adjusted p-values", headers)
    log2s = st.selectbox("Select Log2 Fold Changes", headers)
    
    controlg = st.multiselect("Select Control Group", headers)
    expg = st.multiselect("Select Experimental Group", headers)
    
    
    


def prepdata():
    global l2fc
    global logp
    global df
    global ps

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


    STYLES = {"Dark grid": "darkgrid",
        "Dark": "dark",
        "White Grid":"whitegrid",
        "White":"white",
        "Ticks":"ticks",
        
  
        
        
    }
    

    st.sidebar.header("Change Volcano-plot Parameters")
    x= list(STYLES.keys())
    sch = st.sidebar.selectbox("Define a plot schema", x)
    schema= STYLES.get(sch)
    p=st.sidebar.slider('p-value threshold', float(min(ps)), float(max(ps)), 0.05)
    top_genes=st.sidebar.slider('Label top genes', 0, 30, 5)
    textsize=st.sidebar.slider('Size of labels', 0, 20, 8)
    x=st.sidebar.slider('Adjust x-axis', float(0), float(max(l2fc)+2), float(max(l2fc)+2))
    y=st.sidebar.slider('Adjust y-axis', float(0), max(logp)+10, (max(logp)+10))

    df['x']= df.L2FC[0:top_genes]
    df['y']= df.neglogp[0:top_genes]
    df['Gene2']= df.Gene[0:top_genes]
    dfmod=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    dfmod20=dfmod.iloc[0:top_genes]

    coly=df["padj"]<p
    
    with sns.axes_style(schema):
        fig = plt.figure(figsize=(8,8))        
        ax = fig.add_subplot(1, 1, 1)
        sns.scatterplot(l2fc,logp,hue=coly,s=16,ax=ax)
        ax.set_ylabel("-log p-value",fontsize=15)
        ax.set_xlabel("log2 Fold Change",fontsize=15)
        plt.ylim(0, y)
        plt.xlim((-x), x)


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

_max_width_()  	

#load=st.checkbox("Load Data")



loaddata()

prepdata()

#if load:
#    loaddata()
#    prepdata()

st.header("Choose a plot:")

volcano=st.checkbox("PadPlot Volcano")
heatmap=st.checkbox("PadPlot Heatmap")

if volcano:
    volcanoplot()
    

if heatmap:
    heatmapplot()







