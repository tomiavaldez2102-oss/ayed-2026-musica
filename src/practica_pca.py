## ==============================================================================
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib import style

# Preprocesado y modelado
# ==============================================================================
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')
#cargo el data set
df = pd.read_csv("Wine.csv")
#necesito separar la class del resto de variables
X = df[['Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids',
     'Nonflavanoid phenols', 'Proanthocyanins','Color intensity','Hue',
     'OD280/OD315 of diluted wines', 'Proline']]

y = df['Class']

#antes de iniciar el pca puedo estandarizar
x_esc = StandardScaler()
x_estan = x_esc.fit_transform(X)
#una vez que estandarize puedo aplicar el modelo pca
#creo la caja vacia
pca = PCA()
pca_est = pca.fit(x_estan)
print(pca_est.components_)
#muestro varianza explicativa
print('--QUE PORCENTAJE DE INFORMACION CAPTURA CADA COMPONENTE?:')
var = pca_est.explained_variance_ratio_
print(var)
#Aplico criterio de kaiser que 
#retiene solo las componentes cuyo
#autovalor sea >1 osea 
autovalor = pca.explained_variance_
criterio_k = autovalor[autovalor > 1]
print(criterio_k)
#AHORA DETERMINO CUANTAS COMPONENTES SE NECESITAN PARA 
#CAPTURAR EL 70% DE LA VARIANZA
#APLICO SUMA ACUMULATIVA DEL PORCENTAJE DE VARIANZA EXPLICADA
print('CUANTOS COMPONENTES NECESITO PARA TENER VARIANZA EXPLICADA MAYOR A 70')
var_exp = np.cumsum(pca.explained_variance_ratio_)
print(var_exp)
#grafico en base a que necesito 4 componentes
#busco indices donde componentes son true
var_70 = np.argmax(var_exp >= 70) +1
var_acum = var_exp*100
#grafico cada componente principal
# eje y altura
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))
ax.plot(range(1,14), var_acum, marker ='o', color='red', label = 'varianza acumulada')

plt.axhline(y=70, color='red',linestyle='--', label ="condicion >70%")
plt.axvline(x=4, color='blue', linestyle='--', label='Componentes')

for x,y in zip(range(1,14), var_acum):
    label=round(y,2)
    ax.annotate(
        label,
        (x,y),
        textcoords='offset points',
        xytext=(0,10),
        ha='center'
    )

plt.xlabel("COMPONENTES PRINCIPALES")
plt.ylabel('Porcentaje acumulado')
plt.xticks(range(1,14))
plt.grid(True)
ax.legend()
plt.show()






























