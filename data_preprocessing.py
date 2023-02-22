## Librerías

# Procesamiento de datos
import numpy as np
import pandas as pd
import datetime

# Gráficos
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle

# Normalización
from sklearn.preprocessing import MinMaxScaler

## Paleta de colores

colormap = "coolwarm"

cmap = matplotlib.cm.get_cmap(colormap)

palette = cmap(np.linspace(start = 0, stop = 1, num = 5))

## Carga de los datos

df = pd.read_csv("marketing_campaign.csv", delimiter = "\t")

print(f"Este dataset contiene {df.shape[0]} registros y {df.shape[1]-1} atributos.")

## EDA

df.describe() # Resumen de estadísticas de las características numéricas

df.info() # Información sobre las categorías

# Matriz de correlaciones

plt.figure(figsize=(20,20))  

sns.heatmap(df.corr(),annot = True, cmap = colormap, center = 0)

plt.title(label = "Matriz de correlaciones")

plt.savefig('heatmap.png')

# Analizamos las columnas categóricas y las numéricas

cols = df.columns

num_cols = df._get_numeric_data().columns.values

cat_cols = list(set(cols) - set(num_cols))

print(f"Estas son las columnas categóricas:\n\n{cat_cols}\n\n")

print(f"Estas son las columnas numéricas:\n\n{num_cols}\n\n")

# Representamos los histogramas de las columnas numéricas

fig, axes = plt.subplots(5, 5, figsize=(20, 20))

for ax, column, color in zip(axes.flat, num_cols[1:], cycle(palette)):

    fig = sns.histplot(df[column], ax = ax, color = color)
    
    fig.grid()
    
plt.savefig('numeric_data.png')

## De la exploración de datos numéricos sacamos las siguientes conclusiones:
# Se pueden eliminar los outliers de los atributos de Year_Birth y Income
# Se pueden unir los datos proporcionados por Kidhome y Teenhome
# Los atributos Z_CostContact y Z_Revenue no proporcionan información relevante

# Representamos la frecuencia de las columnas categoricas

fig, axes = plt.subplots(1, 2, figsize=(20, 8))

for ax, column, color in zip(axes.flat, ['Marital_Status', 'Education'], palette):
    
    sns.barplot(x= df[column].value_counts().index, y = df[column].value_counts().values, ax = ax, color = color)
    
plt.savefig('categorical_data.png')

## De la exploración de datos categóricos sacamos las siguientes conclusiones:
# Se pueden eliminar los outliers del atributo de Marital_Status
# La columna Dt_Customer contiene valores temporales, que se transformarán posteriormente a número de días discurridos

## Procesamiento de datos

# Porcentaje de valores nulos en cada una de las características

df.isnull().sum()/len(df)*100

# Como los valores nulos tan solo representan el 1% de los valores, procedemos a eliminarlos.

df = df.dropna()

print(f"El número total de registros después de eliminar las filas con valores nulos es: {len(df)}")

# Columnas numéricas

fig, axes = plt.subplots(1, 2, figsize=(6, 6))

for ax, column, color in zip(axes.flat, ["Year_Birth", "Income"], palette):

    fig = sns.boxplot(data = df[f"{column}"], ax = ax, color = color)
    
    fig.grid()

plt.tight_layout()

plt.savefig('numeric_boxplot.png')

# Year_Birth: Eliminamos los outliers

df = df[df["Year_Birth"] > 1920]

# Income: Eliminamos los outliers

df = df[df["Income"] < 200_000]

print(f"El número total de registros después de eliminar los outliers de las columnas numéricas es: {len(df)}")

# Columnas categóricas

# Marital_Status: Eliminamos los outliers y convertimos los valores

df = df[df["Marital_Status"].isin(['Single', 'Together', 'Married', 'Divorced', 'Widow', 'Alone'])]

df["Marital_Status"] = df["Marital_Status"].replace({'Single' : 1, 'Together' : 2, 'Married' : 2, 'Divorced' : 1, 'Widow' : 1, 'Alone' : 1})

# Education: Sustituimos cada nivel educativo por un numero

df["Education"] = df['Education'].replace({"Basic": 0, "2n Cycle": 1, "Graduation": 2, "Master": 3, "PhD": 4})

# Dt_Customer: Convertimos la fecha en la que se hicieron clientes en el numero de dias discurridos desde entonces

df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], format='%d-%m-%Y')

df["Time_Customer"] = (datetime.datetime.now() - df["Dt_Customer"]).dt.days

print(f"El número total de registros después de eliminar los outliers de las columnas categóricas es: {len(df)}")

## Feature Engineering

# Age: calculamos la edad del cliente según el año de nacimiento

df["Age"] = datetime.datetime.now().year - df["Year_Birth"]

# Family_members: unimos los datos de Marital_Status  y de Children

df["Family Members"] = df["Marital_Status"] + df["Kidhome"] + df["Teenhome"]

# Total_Spent: Total de gasto en productos

df["Total_Spent"] = df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] + df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]

# Total_Purchases: Total de compras realizadas

df["Total_Purchases"] = df["NumDealsPurchases"] + df["NumWebPurchases"] + df["NumCatalogPurchases"] + df["NumStorePurchases"]

# Accepted_Promos: Total de promociones aceptadas

df["Accepted_Promos"] = df["AcceptedCmp1"] + df["AcceptedCmp2"] + df["AcceptedCmp3"] + df["AcceptedCmp4"] + df["AcceptedCmp5"]

# Pct_Promos: Porcentage de compras realizadas con promoción frente al total de compras

df["Prctg_Promos"] = np.where(df["Total_Purchases"] != 0, round(df["NumDealsPurchases"] / df["Total_Purchases"], 2), 0)

## Feature Selection

# Eliminamos las columnas que no nos aportan información

drop_columns = ["ID", "Year_Birth", "Marital_Status", "Kidhome", "Teenhome", "Dt_Customer", "Z_CostContact", "Z_Revenue", "MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds", 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4','AcceptedCmp5', 'Complain', 'Response']

df = df.drop(drop_columns, axis = 1)

# Matriz de correlaciones

plt.figure(figsize = (12, 12))  

sns.heatmap(df.corr(),annot = True, cmap = colormap, center = 0)

plt.title(label = "Matriz de correlaciones")

plt.show()

plt.savefig('engineered_heatmap.png')

## Normalización de Datos

scaler = MinMaxScaler()

x = np.asarray(df)

x_norm = scaler.fit_transform(x)
