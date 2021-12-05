import seaborn as sns
import numpy as np

def heatmap(x):
    """
    This function creates a heatmap from a dataframe given
    """
    corr = x.corr()
    mascara = np.triu(np.ones_like(corr, dtype=bool)) # generamos la máscara para la triangular superior
    color_map = sns.diverging_palette(0, 10, as_cmap=True) # paleta de colores
    return sns.heatmap(corr,  
                mask = mascara,
                cmap='viridis',
                square=True, #que los datos se vean como cuadrados
                linewidth=0.5, #ancho de línea
                vmax=1,
                cbar_kws={"shrink": .5}, #barra lateral,
                annot=True
            )

