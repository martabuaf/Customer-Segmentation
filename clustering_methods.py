## Clustering

## Método del codo

inercias = list() 

numero_k = range(1, 15)
  
for k in numero_k: 
    
    kmeans = KMeans(n_clusters = k, n_init = "auto")
    
    kmeans.fit(x_norm)  
    
    inercias.append(kmeans.inertia_)
    
# Creo el gráfico

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(x = numero_k, y = inercias, s = 80, ax = ax)

sns.lineplot(x = numero_k, y = inercias, alpha = 0.5, ax = ax)

sns.scatterplot(x = [numero_k[3]], y = [inercias[3]], color = palette[4], s = 150, ax = ax)

ax.set(title='Inercia K-Means', ylabel='Inercia', xlabel = 'Número de clusters')

plt.savefig('elbow_method.png')

## Algoritmos de agrupación

# K-Means

# Defino el modelo

model = KMeans(n_clusters = 4, n_init = 10)

model.fit(x_norm)

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())


# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Diferentes n_init:

fig, axes = plt.subplots(5, 2, figsize=(20, 20))

for ax, n in zip(axes.flat, range(1,20,2)):

    # Defino el modelo

    model = KMeans(n_clusters = 4, n_init = n)

    model.fit(x_norm)

    # Gráfico

    fig = sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap, ax = ax)
    
    ax.title.set_text(f"n_init:{n}")
    
    plt.tight_layout()
    
# K-means Mini Batch

# Defino el modelo

model = MiniBatchKMeans(n_clusters = 4, n_init = 10)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Diferentes n_init:

fig, axes = plt.subplots(5, 2, figsize=(20, 20))

for ax, n in zip(axes.flat, range(1,20,2)):

    # Defino el modelo

    model = MiniBatchKMeans(n_clusters = 4, n_init = n)

    model.fit(x_norm)

    # Gráfico

    fig = sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap, ax = ax)
    
    ax.title.set_text(f"n_init:{n}")
    
    plt.tight_layout()
    
# Bisecting K-means

# Defino el modelo

model = BisectingKMeans(n_clusters = 4, n_init = 10)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Diferentes n_init:

fig, axes = plt.subplots(5, 2, figsize=(20, 20))

for ax, n in zip(axes.flat, range(1,20,2)):

    # Defino el modelo

    model = BisectingKMeans(n_clusters = 4, n_init = n)

    model.fit(x_norm)

    # Gráfico

    fig = sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap, ax = ax)
    
    ax.title.set_text(f"n_init:{n}")
    
    plt.tight_layout()
    
# Affinity Propagation

# Defino el modelo

model = AffinityPropagation(preference =-50)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Mean Shift

# Defino el modelo

model = MeanShift(bandwidth = 0.65, bin_seeding = True)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Spectral Clustering

# Defino el modelo

model = SpectralClustering(n_clusters = 4, affinity ='nearest_neighbors')

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

#plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Agglomerative Clustering

# Defino el modelo

model = AgglomerativeClustering(n_clusters = 4)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

#plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Feature Agglomeration

# Defino el modelo

model = FeatureAgglomeration(n_clusters = 4)

model.fit(np.transpose(x_norm))

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

#plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# DBSCAN

# Defino el modelo

model = DBSCAN()

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

#plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# OPTICS

# Defino el modelo

model = OPTICS(max_eps = 10)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

#plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Birch

# Defino el modelo

model = Birch(n_clusters = 4) ## Funciona bien con 3 clusters

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

#plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

## Elección del método de clustering

# Defino el modelo

model = BisectingKMeans(n_clusters = 4, n_init = 10)

model.fit(x_norm)

# Detalles de los clusters

df_model = pd.DataFrame.copy(df)

pd.options.display.max_columns = 250 # Cambio el numero de columnas que se visualizan

df_model["Cluster"] = model.labels_

display(df_model.groupby(by = ["Cluster"]).describe())

# Gráfico

plt.figure(figsize = (10, 6))

sns.scatterplot(x = x_norm[:, 7], y = x_norm[:, 1], hue = model.labels_, palette = colormap)

plt.scatter(model.cluster_centers_[:, 2], model.cluster_centers_[:, 3], color = palette[2], marker = "x", )

plt.title("Clustering")

plt.show()

# Muestro los datos de los centroides

df_centroides  = pd.DataFrame(data = model.cluster_centers_, columns = df.columns)

scaler = MinMaxScaler()

scaler = scaler.fit(df_centroides)

df_centroides = scaler.inverse_transform(df_centroides)

df_centroides =  pd.DataFrame(data = df_centroides, columns = [df.columns])

df_centroides

# Muestro las relaciones entre variables

sns.pairplot(df_model, hue = "Cluster", palette = colormap, corner = True)

plt.savefig('atributos_clusters.png')
