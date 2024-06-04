# Reporte del Modelo Final


**5.1 Resultados con convoluciones 1D**
*   El resultado nos muestra un accuracy de aproximadamente 0.8. Esto también se puede evidenciar durante la fase de entrenamiento del modelo, donde el modelo alcanza un "plateau" de 0.8. El hecho de que el accuracy no suba de este punto se debe probablemente a que hay péptidos en más de una cartegoría. Es decir que no son mutuamente exclusivos. Esta es una posible razón de por qué el modelo llega sólo hasta ese punto.

**5.2 Resultados con convoluciones 2D**
*   En este caso el accuracy del modelo no subió de 0.63 y finalizó con early stopping en vista de que no mejoraba. Posibles razones del pobre desempeño del modelo pueden tener que ver con la matriz de 10 x 10 que representa cada péptido. La matriz es muy pequeña y las convoluciones que se aplican a esta matriz no son demasiadas, generando modelos con muy pocos datos. Segun esto, la representación de secuencias cortas con modelos convolucionales 2d es poco eficiente.

**5.3 Resultados con modelo pre entrenado EfficientNet y Transfer Learning**
*   En este caso tuvimos un accuracy un tanto peor que el el modelo de convoluciones 2d. Esto posiblemente esté relacionado con el hecho de que la representación de las secuencias resulta en matrices de pequeño tamaño, las cuales son mejor analizables por convoluciones 1D. En el caso de EfficientNet tenemos representaciones que necesariamente van en tres canales, resultando en matrices con muchos ceros, lo que no es eficiente al momento de representar secuencias biológicas. Se puede concluir que para clasificación es superior el concepto de convoluciones 1D, seguido por convoluciones 2D con un sólo canal, seguido por modelos con convoluciones 2D pero que utilizan más de un canal. También se demuestra que el concepto de transfer learning es utilizable con conceptos tan distantes como una imágen y una secuencia biológica, a pesar de que su eficiencia en este caso no fue la óptima. Con seguridad fuentes de información de secuencia de ADN con mayor información, como lo es el caso de genomas completos, den mejores resultados con estos modelos.
