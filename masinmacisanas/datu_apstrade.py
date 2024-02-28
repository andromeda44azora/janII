import pandas as pd #Failu apstrāde
import matplotlib.pyplot as plt #Grafiki
import seaborn as sb #Vizualizācija
sb.set_style('whitegrid')
plt.rcParams['figure.figsize']=(15,10) # plot size

def karstuma_karte(datne):
    datu_fails = pd.read_csv(datne).select_dtypes('number')
    sb.heatmap(datu_fails.corr(), annot=True, cmap='magma')
    plt.show()


def datu_biezums(datne, kolonna):
    datu_fails = pd.read_csv(datne)
    sb.distplot(datu_fails[kolonna], color='r')
    plt.title(kolonna.capitalize() + ' biežums', fontsize = 16)
    plt.xlabel(kolonna.capitalize(), fontsize = 14)
    plt.ylabel("Biežums", fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.show()
    return

datne1 = "masinmacisanas/dati/auto_simple.csv"
datne2 = "masinmacisanas/dati/auto_imports.csv"

# karstuma_karte(datne2)

datu_biezums(datne1, "Volume")

