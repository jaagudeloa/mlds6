# Librerías que se utilizarán en el notebook
import pubmed_parser as pp
import numpy as np
np.random.seed(0)
import pandas as pd
import json, nltk, re
import requests
import xml.etree.ElementTree as ET
import time
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from unidecode import unidecode


def descarga_articulos():
  # listado de peptidos
  peptidos = ['abaecin', 'acaloleptin', 'acanthaporin', 'acanthoscurrin', 'acidocin', 'acipensin', 'actagardine', 'adepantin', 'adrenomedullin', 'afusinc', 'agelaia', 'alamethicin', 'alarin', 'alloferon', 'allomyrinasin', 'alvinellacin', 'alyteserin', 'amoebapore', 'amolopin', 'amurin', 'amylin', 'amylocyclicin', 'andersonin', 'andricin', 'androctonin', 'androctonus', 'andropin', 'anoplin', 'antapin', 'apidaecin', 'arasin', 'arenicin', 'ascaphin', 'astacidin', 'aurein', 'aureocin', 'baceridin', 'bactenecin', 'bactericidin', 'bacteriocin', 'bactofencin', 'bactridine', 'bactrocerin', 'balteatide', 'batroxicidin', 'beta', 'bldesin', 'bombinin', 'bombolitin', 'bovine', 'bradykinin', 'brazzein', 'brevifactin', 'brevinin', 'buforin', 'buthinin', 'butyrivibriocin', 'buwchitin', 'caenacin', 'caerin', 'caerulein', 'callinectin', 'capidermicin', 'capistruin', 'carnobacteriocin', 'carnocin', 'carnocyclin', 'casecidin', 'cathelicidin', 'cecropin', 'centrocin', 'ceratotoxin', 'cerecidin', 'chemerin', 'chensinin', 'chromacin', 'chrombacin', 'chrysophsin', 'cinnamycin', 'circularin', 'circulin', 'citrocin', 'citropin', 'clavanin', 'clavaspirin', 'cliotide', 'coleoptericin', 'colistin', 'coprisin', 'copsin', 'corticostatin', 'crabrolin', 'cremycin', 'crinicepsin', 'crotalicidin', 'crotamine', 'cryptdin', 'cryptonin', 'ctenidin', 'ctriporin', 'cupiennin', 'curvacin', 'curvaticin', 'cyanophlyctin', 'cyanovirin', 'cyclopsychotride', 'cyclosaplin', 'cycloviolacin', 'cycloviolin', 'cypemycin', 'cytolysin', 'dahlein', 'datucin', 'defensin', 'delftibactin', 'dendropsophin', 'dermaseptin', 'dermatoxin', 'dermcidin', 'deserticolin', 'desotamide', 'diapausin', 'diptericin', 'distinctin', 'divercin', 'divergicin', 'dolabellanin', 'dominulin', 'dosotamide', 'drosocin', 'drosomycin', 'duramycin', 'durancin', 'dybowskin', 'enbocin', 'enterocin', 'esculentin', 'fabatin', 'feleucin', 'fengycin', 'formaecin', 'formicin', 'frenatin', 'fusaricidin', 'gaegurin', 'gageostatin', 'gageotetrin', 'galensin', 'gallerimycin', 'gallidermin', 'gallin', 'gallinacin', 'gambicin', 'garvicin', 'geobacillin', 'ginkbilobin', 'gramicidin', 'griffithsin', 'griselimycin', 'guentherin', 'hadrurin', 'hainanenin', 'halictine', 'haliotisin', 'halocidin', 'halocin', 'hdmolluscidin', 'heliocin', 'heliomicin', 'hepcidin', 'heterin', 'heteroscorpine', 'hinnavin', 'hipposin', 'hiracin', 'hispidalin', 'holosin', 'holothuroidin', 'holotricin', 'hominicin', 'hymenochirin', 'hymo', 'hyphancin', 'hyposin', 'imcroporin', 'indolicidin', 'isracidin', 'ixodidin', 'ixosin', 'jaburetox', 'japonicin', 'jelleine', 'jindongenin', 'jingdongin', 'kalata', 'kaliocin', 'kassinatuerin', 'kassorin', 'kenojeinin', 'labaditin', 'labyrinthopeptin', 'lacrain', 'lactacin', 'lacticin', 'lactocin', 'lactococcin', 'lactococcin', 'lactocyclicin', 'lactoferricin', 'lactolisterin', 'lariatin', 'lasiocepsin', 'lasioglossin', 'lassomycin', 'laterosporulin', 'laticeptin', 'lebocin', 'leucocin', 'leucrocin', 'lichenicidin', 'lichenin', 'lividin', 'locustin', 'longicin', 'longicornsin', 'longipin', 'lucifensin', 'lucilin', 'lugensin', 'lumbricin', 'lunasin', 'lunatusin', 'lycocitin', 'lycotoxin', 'lynronne', 'lysozyme', 'macropin', 'maculatin', 'maeucath', 'magainin', 'marmelittin', 'mastoparan', 'maximin', 'medusin', 'megin', 'melectin', 'melimine', 'melittin', 'mersacidin', 'mesentericin', 'metalnikowin', 'metchnikowin', 'meucin', 'micasin', 'microbisporicin', 'microcin', 'micrococcin', 'microplusin', 'moronecidin', 'mucroporin', 'mundticin', 'muscin', 'mutacin', 'myticalin', 'mytichitin', 'myticin', 'mytilin', 'mytilus', 'mytimacin', 'myxinidin', 'nabaecin', 'naegleriapore', 'neuromacin', 'neurotensin', 'nicomicin', 'nigroain', 'nigrocin', 'nisin', 'nukacin', 'ocellatin', 'odoranain', 'odorranain', 'omwaprin', 'oncorhyncin', 'opiscorpine', 'opistoporin', 'oreoch', 'ovispirin', 'oxyopinin', 'oxysterlin', 'paenibacillin', 'paenibacterin', 'paenicidin', 'palicourein', 'palustrin', 'pandinin', 'panitide', 'pantocin', 'panurgine', 'panusin', 'papiliocin', 'papilosin', 'parabutoporin', 'paracentrin', 'paralithocin', 'parasin', 'pardaxin', 'parigidin', 'parkerin', 'patellamide', 'pediocin', 'pelophylaxin', 'pelovaterin', 'penaeidin', 'penisin', 'penocin', 'perfrin', 'perinerin', 'persulcatusin', 'phoratoxin', 'phormicin', 'phylloseptin', 'phylloxin', 'piceain', 'pilosulin', 'piscicolin', 'piscidin', 'planosporicin', 'plantaricin', 'plantaricyclin', 'plantazolicin', 'plasticin', 'plectasin', 'pleskein', 'pleurain', 'pleurocidin', 'plicatamide', 'polymyxin', 'ponericin', 'potamin', 'procambarin', 'prolixicin', 'prophenin', 'protegrin', 'protonectin', 'psacotheasin', 'psalmopeotoxin', 'psdefensin', 'pseudhymenochirin', 'pseudin', 'psyle', 'pyrrhocoricin', 'ranacyclin', 'ranalexin', 'ranatuerin', 'raniseptin', 'rattusin', 'regiiialpha', 'retrocyclin', 'rondonin', 'roseocin', 'rugosin', 'ruminococcin', 'sakacin', 'salivaricin', 'salmocidin', 'sapecin', 'sarconesin', 'sarcotoxin', 'scapularisin', 'scarabaecin', 'schmackerin', 'sclerosin', 'scolopendin', 'scolopendrasin', 'scolopin', 'scygonadin', 'secretolytin', 'seminalplasmin', 'senegalin', 'serrulin', 'sesquin', 'shepherin', 'shuchin', 'siamycin', 'signiferin', 'spiderine', 'spiniferin', 'spinigerin', 'staphylococcin', 'stigmurin', 'stomoxyn', 'streptococcin', 'strongylocin', 'styelin', 'sublancin', 'subtilin', 'subtilomycin', 'subtilosin', 'tachycitin', 'tachyplesin', 'tachystatin', 'teixobactin', 'temporin', 'tenecin', 'termicin', 'thermophilin', 'theromacin', 'thrombocidin', 'thuricin', 'tigerinin', 'tolworthcin', 'trichamide', 'tricholongin', 'tridecaptin', 'triintsin', 'tritrpticin', 'turgencin', 'uberolysin', 'ubiquicidin', 'ubonodin', 'uperin', 'urechistachykinin', 'urumin', 'variacin', 'vasostatin', 'vejovine', 'virescein', 'viscotoxin', 'wollamide']

  # variables fijas request
  base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
  db = "pubmed"
  retmax = 200

  # inicializamos lista de articulos
  list_articulos = []
  for peptide in peptidos:
    term = peptide
    url = f"{base}?db={db}&term={term}&usehistory=y&retmax={retmax}"

    # realizo el consumo
    response = requests.get(url)

    # espera de 1 s para no saturar el servidor
    time.sleep(1)

    if response.status_code == 200:
      # Leer la respuesta como texto
      data = response.text

      #convierto el archivo a un element tree
      root = ET.fromstring(data)
      id_elements = root.findall(".//Id")
      # Obtener los textos de las etiquetas <Id>
      id_list = [id_element.text for id_element in id_elements]

      # itero sobre el listado de id para obtener la info de los articulos
      for id in id_list:
        # obtengo la información del articulo a partir del id
        try:
          article = pp.parse_xml_web(id, sleep=1, save_xml=False)
          article['peptido'] = peptide
          # Agrego el articulo al listado de articulos
          list_articulos.append(article)
        except Exception as e:
          print(f"Error: {e} id {id}")

  # Convertir a DataFrame
  df_articles = pd.DataFrame(list_articulos)

  # Guardar como CSV
  df_articles.to_csv('data.csv', index=False, sep=';')

"""La  función implementada recorre el listado de péptidos y mediante el API de e-utilities obtiene el identificador único del artículo y lo almacena en una lista. Posteriormente para cada ID obtenido se descarga el artículo el cual retorna un diccionario de python con la siguiente información:


*   title
*   abstract
*   journal
*   affiliation
*   autors
*   keywords
*   doi
*   year
*   pmid

---

Se realiza la descarga del archivo obtenido al ejecutar la función descrita en la sección anterior y se lee en un data frame de pandas el cual se encuentra en la siguiente enlace https://drive.google.com/file/d/1EHQDqAWHlIvJrAJ33Ikbo9kNSjNR9Y_s/view?usp=sharing
"""

articles = pd.read_csv('/content/articles.csv',sep=';')

print(f"El corpus contiene {articles.shape[0]} articulos")

size_bytes = articles.memory_usage(deep=True).sum()

# Convertir a megabytes
size_mb = size_bytes / (1024*1024)

print(f"El corpus tiene un tamaño de {size_mb} MB")

"""
Al obtenerse los datos de una fuente confiable no se presentan errores de codificación

Para verificar si existen datos nulos se realiza la busqueda en el dataFrame en donde se evidencia que existen algunos registros que ni tienen abstract los cuales se proceden a eliminar
"""

missing_data = articles.isnull().any()
print(missing_data)

articles_clean = articles.dropna(subset=['abstract'])

"""
---

Los tipos de datos del dataset son los siguientes
"""

articles_clean.info()

articles_clean.describe()

"""Realizamos la grfica para visualizar la frecuencia de aparicion de cada uno de los peptidos en el dataset"""

# Contar la frecuencia de cada péptido
peptidos_freq = articles_clean['peptido'].value_counts()

# Graficar
plt.figure(figsize=(12, 6))
peptidos_freq.plot(kind='bar')
plt.title('Frecuencia de Péptidos')
plt.xlabel('Péptido')
plt.ylabel('Frecuencia')
plt.show()

"""Visualizamos los peptidos con mayor frecuencia"""

# Obtener los 15 primeros con mayor frecuencia
top_peptidos = peptidos_freq.head(15)

# Graficar
plt.figure(figsize=(12, 6))
top_peptidos.plot(kind='bar')
plt.title('15 Péptidos con Mayor Frecuencia')
plt.xlabel('Péptido')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')
plt.show()

"""Visualizamos los peptidos con menor frecuencia"""

# Obtener los 15 últimos con menor frecuencia
bottom_peptidos = peptidos_freq.tail(15)

# Graficar
plt.figure(figsize=(12, 6))
bottom_peptidos.plot(kind='bar')
plt.title('15 Péptidos con Menor Frecuencia')
plt.xlabel('Péptido')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')
plt.show()

"""Se crea el histograma por año para visualizar la distribuvión temporal de los artículos"""

# Filtrar por años
articles_year = articles_clean[articles_clean['year'] >= 1990]

# Ordenar el DataFrame por el año
articles_year_sorted = articles_year.sort_values('year')

# Conteo de registros por año
registros_por_año = articles_year_sorted['year'].value_counts()

# Crear el histograma
plt.figure(figsize=(12, 6))
plt.bar(registros_por_año.index, registros_por_año.values, color='skyblue')
plt.xlabel('Año')
plt.ylabel('Cantidad de Péptidos')
plt.title('Cantidad de Péptidos por Año (Ordenados)')
plt.xticks(registros_por_año.index)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

"""Observamos la distribución por revista y graficamos las 15 revistas con mayor cantidad de articulos"""

#frecuencia de aparición de los articulos
registros_por_revista = articles_year_sorted['journal'].value_counts()

# Obtener los 15 primeros con mayor frecuencia
top_journal = registros_por_revista.head(15)

# Graficar
plt.figure(figsize=(12, 6))
top_journal.plot(kind='bar')
plt.title('15 Revistas con Mayor Frecuencia')
plt.xlabel('Revista')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')
plt.show()

"""Debido a aque el objetivo del proyecto es analizar los abstract se obtiene la longitud de cada abstract"""

articles_clean['abstract_length'] = articles_clean['abstract'].apply(len)

sns.set(style="whitegrid")

# Crear el histograma
plt.figure(figsize=(10, 6))
sns.histplot(articles_clean['abstract_length'], bins=30, kde=True, color='skyblue')
plt.title('Histograma de Longitud de Abstracts')
plt.xlabel('Longitud del Abstract')
plt.ylabel('Frecuencia')
plt.show()

"""## **2. Limpieza de los Textos**
---

Se aplico el siguiente preprocesamiento:

1. Filtrar stopwords.
3. Normalizar el texto con `unidecode`.
4. Convertir a minúsculas.
"""

# FUNCIÓN CALIFICADA preprocess:
def preprocess(doc):
    filtered_tokens = filter(
            lambda token: not token.is_stop,
            doc
            )
    # Obtenemos los textos de cada token
    textos = map(
            lambda token: token.text ,
            filtered_tokens
    )
    text = " ".join(textos)
    # Normalizamos el texto
    norm_text = unidecode(text)
    # Quitamos grafía
    lower_text = norm_text.lower()
    preprocess_text = lower_text
    return preprocess_text

"""Utilizamos la función para preprocesar los abstract, para esto se descargo un modelo de spacy para terminos biomedicos en íngles el cual se encuentra en el siguiente enlace [scispacy](https://allenai.github.io/scispacy/)"""

nlp = spacy.load("en_core_sci_sm")

"""Realizamos el preprocesamiento para el abstract de los articulos"""

articles_preprocess = articles_clean.head(10)
texts = list(articles_preprocess["abstract"])
corpus = list(nlp.pipe(texts, n_process=4))
preprocess_text = preprocess(corpus[0])
display(preprocess_text)
