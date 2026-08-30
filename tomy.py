import numpy  as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#IMPORTO LOS DATOS
df = pd.read_csv("Wine.csv")