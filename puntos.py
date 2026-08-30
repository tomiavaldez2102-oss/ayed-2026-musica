#APLIQUE PCA SOBRE 13 VARIABLES FISICO QUIMICAS DE DATASET DE VINOS, DIRECTAMENTE
#SOLO CENTRANDO LOS DATOS, LUEGO REPITO EL PROCEDIMIENTO
# YA HABIENDO ESTANDARIZADO LAS VARIABLES PREVIAMENTE
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

#IMPORTO LOS DATOS
df = pd.read_csv("Wine.csv")
#creo variables para separar clase del resto
X = df[['Alcohol','Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
        'Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue',
        'OD280/OD315 of diluted wines','Proline']]
y = df[['Class']]
#Creo la estructura natematica que contiene centrado por defecto
pca = PCA()
#meto los valores de X a la caja y hace los calculos
#de la matriz de covarianza y teorema espectral
# y guarda la matriz de coeficientes o rotacion P
pca.fit(X)
#print(pca.components_)
#calculo la varianza explicativa
var = pca.explained_variance_
#print(var)
#YA APLIQUE PCA SOBRE LAS 13 VARIABLES SIN ESTANDARIZAR
# REPITO EL PROCEDIMIENTO
# YA HABIENDO ESTANDARIZADO LAS VARIABLES PREVIAMENTE
#ESTANDARIZO ANTES DE APLICAR EL MODELO
#PARA QUE LAS VARIABLES ESTEN EN IGUALDAD DE CONDICIONES
#creo la estructura matematica de estandarizacion
x_escalado = StandardScaler()
#meto los valores de x y fit calula media 0 y desv 1 estandarizo con transform
x_estand = x_escalado.fit_transform(X)
#ahora aplico el PCA
pca_est = PCA()
pca_est.fit(x_estand)
print(pca_est.components_)
var_est = pca_est.explained_variance_
print(var_est)
#APLICO CRITERIO DE KAISER ME QUEDO CON LAS COMPONENTES >1
criterio_k = var_est[var_est>1]
print(criterio_k)
#AHORA DETERMINO CUANTAS  COMPONENTES SE NECESITAN PARA CAPTURAR
#AL MENOS 70% DE LA VARIANZA TOTAL Y HAGO EL GRAFICO
#APLICO SUMA ACUMULATIVA QUE SERA LA SUMA PARCIAL DE CADA COMPONENTE
acumulativa = np.cumsum(pca_est.explained_variance_ratio_)
print(acumulativa)
#NECESITO 4 COMPONENTES PARA CAPTURAR EL 70% DE LA VARIABILIDAD
#AHORA GRAFICO LA CURVA ACUMULADA CON MATPLOTLIB
#convierto los valores acumulados a porcentaje
var_acum = acumulativa *100
#aplico la condicion del 70%
plt.figure(figsize=(6,4))
plt.plot(range(1,14), var_acum, marker ='o', color ='red', label='Varianza acumulada')
plt.axhline(y=70, linestyle='--', c='red', label='COMPONENTES')
plt.axvline(x=4, linestyle='--', c='blue', label = 'variabilidad >= 70')
plt.xticks(range(1,14))
plt.ylabel('porcentaje')
plt.xlabel('Componentes principales')
plt.legend()
plt.show()