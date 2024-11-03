from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import pandas as pd

# Carrega a tabela do Excel
tabela = pd.read_excel("EnadeEngControleAutomação.xlsx")

# Exibe as estatísticas descritivas da coluna especificada
with pd.option_context("float_format","{:.2f}".format):
    display(tabela['Nº de Concluintes Inscritos'].describe())

# Cria o boxplot da coluna 'Nº de Concluintes Inscritos'




fig, (ax1, ax2) = plt.subplots(
    nrows=2,
    ncols=1,
    sharex=True,
    gridspec_kw={"height_ratios": (0.15, 0.85), "hspace": 0.02},
)



sns.boxplot(x=tabela['Nº de Concluintes Inscritos'], ax=ax1, showmeans=True, meanline=True, meanprops= {"color": "C1", "linestyle": "--", "linewidth": 1})
sns.histplot(x=tabela['Nº de Concluintes Inscritos'], bins=13, kde = True, ax=ax2)

plt.xlabel('N° de Concluintes inscritos')
plt.ylabel('Quantidade de faculdades')

ax2.xaxis.set_major_locator(mtick.MultipleLocator (base=10.0)) 
ax2.tick_params(axis="x", rotation=90)

for ax in (ax1, ax2): 
    ax.grid(True, linestyle="--", color="gray", alpha=0.5) 
    ax.set_axisbelow (True)

ax2.axvline(tabela['Nº de Concluintes Inscritos'].mean(), color="C1", linestyle="--", label="Média")
ax2.axvline(tabela['Nº de Concluintes Inscritos'].median(), color="C2", linestyle="--", label="Mediana") 
ax2.axvline(tabela['Nº de Concluintes Inscritos'].mode()[0], color="C3", linestyle="--", label="Moda")
ax2.legend()

plt.show()
