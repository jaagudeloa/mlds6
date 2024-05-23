# Reporte del Modelo Baseline
Este documento contiene los resultados del modelo baseline de convoluciones 1D para la clasificación de secuencias de péptidos antimicrobianos

## Descripción del modelo
Se contruyó un modelo basado en convoluciones 1D, utilizando como vectorización un modelo word2vec

## Variables de entrada
Las variables de entrada fueron los péptidos transformados en secuencias de ADN como medida de aumentación de datos.
Esto permitió que cada secuencia de cada péptido fuese posible representarla en más de 100 diferentes secuencias.

## Variable objetivo
La variable objetivo es la etiqueta de función de cada uno de los péptidos antimicrobianos.
Se utilizaron secuencias con etiquetas en 4 categorías:
- AntiCancer     - Anticancerígenas
- AntiMRSA       - Anti Estafilococo dorado
- AntiFungal     - Anti hongo
- AntiBacterial  - Anti bacterianas
Estas categorías se encuentran en la variable 'Activity'

## Evaluación del modelo

### Métricas de evaluación
Se utilizó accuracy como principal métrica de evaluación, aunque también se evaluó precision, recall y f1-score

### Resultados de evaluación
              precision    recall  f1-score   support

           0       0.62      0.61      0.62      5866
           1       0.82      0.89      0.85     28616
           2       0.80      0.69      0.74      9321
           3       0.76      0.61      0.68      4880

    accuracy                           0.79     48683
   macro avg       0.75      0.70      0.72     48683
weighted avg       0.79      0.79      0.79     48683

## Análisis de los resultados
El resultado nos muestra un accuracy de aproximadamente 0.8. Esto también se puede evidenciar durante la fase de entrenamiento del modelo, donde el modelo alcanza un "plateau" de 0.8. El hecho de que el accuracy no suba de este punto se debe probablemente a que hay péptidos en más de una cartegoría. Es decir que no son mutuamente exclusivos. Esta es una posible razón de por qué el modelo llega sólo hasta ese punto.


## Conclusiones
Es posible que el modelo mejore con cominaciones de representaciones. Por ejemplo, en vez de representar las secuencias como ADN, realizar una representación en una combinación de secuencia de aminoácidos y "smiles" que es un modelo de representación de fármacos.

## Referencias
https://cezannec.github.io/CNN_Text_Classification/

