# Definición de los datos

## Origen de los datos

<<<<<<< HEAD
- Con cerca de 3700 nombres asociados con los péptidos se procederá a  realizar búsquedas en la base de datos de PUBMED y se traerá un número de resúmenes de artículos en formato tipo json susceptible de ser analizados por medio de notebooks de python 

## Especificación de los scripts para la carga de datos

- data_acquisition/main.ipynb 

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos
- https://www.ncbi.nlm.nih.gov/research/pubtator3/ 
- https://drive.google.com/drive/folders/1Ok4om1YBNHw9-DpfXZKLET-cK__ZTWSq?usp=drive_link
=======
- Los datos provienen de los resumens de articulos de PUBMED (https://pubmed.ncbi.nlm.nih.gov/). Para la obtención masiva de articulos cientificos desde PubMed se utilizo la API E-utilities que permite a partir de palabras clave realizar la busqueda y descarga de abstrac de manera masiva.Para el proceso de descarga se obtuvo un listado de 430 peptidos Antimicrobianos, estos terminos se utilizan como criterios de busqueda para encontrar los abstracts

## Especificación de los scripts para la carga de datos

- Con ayuda de la api PubTator 3 https://www.ncbi.nlm.nih.gov/research/pubtator3/ se puede extraer una colección de textos en formato tipo Json. La colección de textos hacen parte de los resumenes (abstracts) de interés. En esta etapa se incluye la extracción de ciertas características de los textos. En nuestro caso, nos interesaba extraer segmentos de palabras que correspondieran a las categorías: Disease, Specie y gracias a una lista (bolsa de palabras) elaborada previamente se pudo extraer los términos relacionados a (lípidos) para cada texto (abstract) de interés. De los archivos tipo .json se puede extraer la siguiente información relevante


### Rutas de origen de datos

- https://www.ncbi.nlm.nih.gov/research/pubtator3/
- https://www.ncbi.nlm.nih.gov/research/pubtator3/
>>>>>>> 04d079ebea16c87e1ce791cf9abaf75d8a83cb5d


