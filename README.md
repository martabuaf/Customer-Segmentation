# Segmentación de bases de clientes

![Captura de pantalla 2023-02-22 a las 21 13 00](https://user-images.githubusercontent.com/122131317/220748769-d78ab969-5fbc-4e8b-be2d-d39dee93bcc5.png)

<h3>Resumen:</h3>
<p>En este proyecto, llevaremos a cabo la agrupación no supervisada de datos sobre los registros de clientes de la base de datos de una empresa de comestibles.</p>
<p>La segmentación de clientes es la práctica de separar a los clientes en grupos según sus similitudes y diferencias. Dividiremos a los clientes en grupos para resaltar las características más importantes de cada segmento y modificar los productos en función de las distintas necesidades y comportamientos de los clientes.</p>
<p>Los datos los encontramos <a href = "https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis">aquí</a>.</p>

<h3>Paso 1: Carga de los datos y EDA</h3> 
<p>El análisis exploratorio de datos se refiere al proceso de realizar investigaciones iniciales sobre los datos para descubrir patrones, detectar anomalías, probar hipótesis y comprobar suposiciones con la ayuda de estadísticas resumidas y representaciones gráficas. Sacaremos una serie de conclusiones sobre los siguientes pasos para tratar los datos, dividiéndolos en datos numéricos y categóricos.</p>
<h3>Paso 2: Procesamiento de los datos</h3> 
<p>Procesaremos los datos de manera que nos resulte más fácil su interpretación y, al mismo tiempo, reduciremos la cantidad de variables del modelo.</p>
<h3>Paso 3: Ingeniería de datos</h3> 
<p>Compactaremos los datos de forma que los datos de las nuevas columnas resulten más representativos.</p>
<h3>Paso 4: Agrupación</h3> 
<p>Llevaremos a cabo la agrupación no supervisada de los datos. Para ello utilizamos previamente el método del codo para determinar el número de clusters necesarios. Estudiaremos diferentes métodos de agrupación y buscaremos los valores óptimos de los parámetros.</p><p>La información sobre los distintos algoritmos de clustering la encontramos <a href = "https://scikit-learn.org/stable/modules/clustering.html">aquí</a>.</p>
<h3>Paso 5: Evaluación de los resultados</h3> 
<p>Tras la evaluación de los distintos métodos, nos centraremos en el que mejor resultados nos aporta para nuestro fin. Representaremos los datos resultantes de la agrupación para cada una de las variables que componen el DataFrame original.</p>
<h3>Paso 6: Conclusiones</h3> 
<p>Una vez interpretados los resultados, definiremos las características más relevantes que componen cada uno de los grupos.</p>

<div>
<h4 style = "text-align: center;">Información sobre el contenido del dataset</h4>

<h4>Personas</h4>
<ul>
<li>ID: Identificador único del cliente</li>
<li>Year_Birth: Año de nacimiento del cliente</li>
<li>Education: Nivel educativo del cliente</li>
<li>Marital_Status: Estado civil del cliente</li>
<li>Income: Ingresos anuales del hogar del cliente</li>
<li>Kidhome: Número de hijos en el hogar del cliente</li>
<li>Teenhome: Número de adolescentes en el hogar del cliente</li>
<li>Dt_Customer: Fecha de inscripción del cliente en la empresa</li>
<li>Recency: Número de días transcurridos desde la última compra del cliente</li>
<li>Complain: 1 si el cliente se ha quejado en los últimos 2 años, 0 en caso contrario</li>
</ul>   
<h4>Productos</h4>
<ul>
<li>MntWines: Importe gastado en vino en los últimos 2 años</li>
<li>MntFruits: Importe gastado en frutas en los últimos 2 años</li>
<li>MntMeatProducts: Cantidad gastada en carne en los últimos 2 años</li>
<li>MntFishProducts: Cantidad gastada en pescado en los últimos 2 años</li>
<li>MntSweetProducts: Cantidad gastada en dulces en los últimos 2 años</li>
<li>MntGoldProds: Importe gastado en oro en los últimos 2 años</li>
</ul>      
<h4>Promociones</h4>
<ul>
<li>NumDealsPurchases: Número de compras realizadas con descuento</li>
<li>AcceptedCmp1: 1 si el cliente aceptó la oferta en la 1ª campaña, 0 en caso contrario</li>
<li>AcceptedCmp2: 1 si el cliente aceptó la oferta en la 2ª campaña, 0 en caso contrario</li>
<li>AcceptedCmp3: 1 si el cliente aceptó la oferta en la 3ª campaña, 0 en caso contrario</li>
<li>AcceptedCmp4: 1 si el cliente aceptó la oferta en la 4ª campaña, 0 en caso contrario</li>
<li>AcceptedCmp5: 1 si el cliente aceptó la oferta en la 5ª campaña, 0 en caso contrario</li>
<li>Response: 1 si el cliente aceptó la oferta en la última campaña, 0 en caso contrario</li>
</ul>     
<h4>Lugar</h4>
<ul>
<li>NumWebPurchases: Número de compras realizadas a través de la página web de la empresa</li>
<li>NumCatalogPurchases: Número de compras realizadas a través de un catálogo</li>
<li>NumStorePurchases: Número de compras realizadas directamente en tiendas</li>
<li>NumWebVisitsMonth: Número de visitas a la página web de la empresa en el último mes</li>
</ul>   
</div>

<h2> Perfiles de los clientes:</h2>

![atributos_clusters](https://user-images.githubusercontent.com/122131317/220757311-c979a69c-560d-40f6-b7da-f7c33edcae30.png)

![Captura de pantalla 2023-02-22 a las 21 14 38](https://user-images.githubusercontent.com/122131317/220748786-730cd522-dbbc-4c78-b98c-bc5b221028c6.png)

<h2 style="text-align:center;">Esperamos que te haya gustado!! 😄</h2>

## Autores: 
<p>Marta Búa Fernández ➡️ Ir al perfil de<a href="https://www.linkedin.com/in/martabuaf" target = "_blank"> LinkedIn </a></p> 
<p>Laura Arufe Jorge ➡️ Ir al perfil de<a href="https://www.linkedin.com/in/laura-arufe-aab862247" target = "_blank"> LinkedIn </a></p>
