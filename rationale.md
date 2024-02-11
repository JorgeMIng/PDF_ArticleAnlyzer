## Funcionalidades

## Para validar cada una de las funcionalidades existen tres notebooks en la carpeta examples del uso de las 3 funcionalidades


# NOTA esta libraria realiza operaciones de cache guardando los xml generados en carpetas, estas carpetas son relativas a la ubicacion de ejecucion de los notbooks y pueden ser configuradas

# Tambien se puede deshabilitar las funcionalidades de cache desde los ficheros de conf 


### 1. Draw a keyword cloud based on the abstract information

Se extraen todos los elementos <p> de los bloques abstract que existan en el xml y se usa la libraria word_cloud para mostar las imagenes y descargarlas




### 2. Bar Chart with the Number of Figures per Article

Se cuentan todos los elementos <atributo> que esten definidos en la configuracion en nuestor caso <figure>, en la configuracion se puede cambiar el valor a una lista de ["figure","abstract"] y mostrata tablas de barras por cada atributo



### 3. List Article Links

Se buscan todos los elements <ref> y todos los enlaces <https> en texto plano usando un regex, y se muestran en tablas por cada articulo, las tablas
se crean usando rich, y se componen de un indice y dos columnas una para los ref y otra para los https