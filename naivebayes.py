# Importo las librer´ıas
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
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
#Creare las 4 variables necesarias 
#para separar el bloque de entrenamiento y evaluacion
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#creo la caja vacia
gnb = GaussianNB()
# con .fit meto los valores de X_train e y_train para el entrenamiento
gnb.fit(X_train, y_train)
#aplico ecuacion de prob. bayes aplicada a este contexto
y_pred = gnb.predict(X_test)
#ya se aplico la multiplicacion de de probabilidades individuales

#AHORA, que tan bueno es el modelo?
#necesito una metrica que mida la tasa de acierto frente a la realidad,
#osea acuraccy
#tomo la variable y_test e y_pred
acuraccy = accuracy_score(y_test, y_pred)
print(f'El acuraccy en test es:{acuraccy}')

#Ademas, puedo imprimir los parametros calculados y las posibilidades del modelo
#veamos que los prior se calculan como la frecuencia de cada rato
print(gnb.theta_)
#y tambien la varianza de cada clase
print(gnb.var_)
#podemos imprimit la proba de cada dato
print(gnb.predict_proba(X_test[:10]))


#Uso solo 2 variables
X = df[['Alcohol', 'Color intensity']]
y = df['Class']
#train test
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.3, random_state=42)
#Naive bayes gaussiano
gnb = GaussianNB()
gnb.fit(X_train, y_train)
#prediccion

y_pred = gnb.predict(X_test)
#Acuraccy en test
accuracy =accuracy_score(y_test, y_pred)
print(f'El acuraccy en test es: {accuracy}')
#visualizo la clasificacion 
#creo una malla de puntos para graficar los bordes de decision
x_min, x_max = X['Alcohol'].min() -1, X['Alcohol'].max() +1 
y_min, y_max = X['Color intensity'].min() -1, X['Color intensity'].max() +1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
#predice en toda la malla de puntos
Z = gnb.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy,Z, alpha = 0.4, cmap=plt.cm.RdYlBu)
clase_1 = plt.scatter(df[df['Class']==1]['Alcohol'],
                      df[df['Class']==1]['Color intensity'],c='red')
clase_2 = plt.scatter(df[df['Class']==2]['Alcohol'],
                      df[df['Class']==2]['Color intensity'], c='blue')
clase_3 = plt.scatter(df[df['Class']==3]['Alcohol'],
                      df[df['Class']==3]['Color intensity'], c='green')
plt.legend((clase_1,clase_2,clase_3),
(1,2,3),
scatterpoints=1,
ncol=3,
fontsize=8)
plt.xlabel("Alcohol")
plt.ylabel("Color intensity")
plt.show()