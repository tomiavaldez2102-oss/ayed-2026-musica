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
X = df[['Alcohol','Malic acid', 'Ash', 'Alcalinity of ash','Magnesium','Total phenols',
      'Flavanoids', 'Nonflavanoid phenols','Proanthocyanins','Color intensity',
      'Hue','OD280/OD315 of diluted wines','Proline']]

y = df['Class']

#estandarizo 
x_escal = StandardScaler()
x_est = x_escal.fit_transform(X)

#aplico pca
#creo estructura vacio
pca = PCA()
pca_est = pca.fit(x_est) 
print(pca_est.components_)

autovalores = pca_est.explained_variance_
print('muestro la varianza explicada')
print(autovalores)
print('CRITERIO DE KAISER')
criterio_k = autovalores[autovalores >1]
print(criterio_k)
#cuantos componentes necesito para capturar al menos el 70% de la
#variabilidad
#aplico suma acumulativa en varianza explicada
acumulativa = np.cumsum(pca.explained_variance_ratio_)
print(acumulativa)
#aplico condicion del 70% si es true en autovalores
var_acum = acumulativa*100
cond_70 = np.argmax(var_acum>=70)+1
print(f'necesito {cond_70} elementos para tener una variabilidad mayor a 70%')
#grafico la curva acumulada con matplotlib
eje_x = range(1,14)
eje_y = var_acum
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6,4))
plt.plot(eje_x, eje_y, marker='o',linestyle="-", color='red', label='PCA')
for x,y in zip(eje_x, eje_y):
    label= round(y,2)
    ax.annotate(
        label,
        (x, y),
        textcoords='offset points',
        xytext=(0,10),
        ha='center'
    )
plt.axhline(70, linestyle='--', color='blue')
plt.axvline(4, linestyle='--', color='red')
plt.xlabel('COMPONENTES PRINCIPALES')
plt.ylabel('PORCENTAJE DE VARIANZA EXPLICADA')
plt.xticks(range(1,14))
plt.grid(True)
plt.show()














