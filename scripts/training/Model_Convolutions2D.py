"""## **Entrenamiento y validación de modelo con convoluciones 2D**
---

### **Implementación del modelo**
"""

# Iniciamos con la representación vectorizada de los péptidos
X_vect.shape

# Las matrices de los modelos convolucionales 2d sólo reciben floats
# En vista de que los vectores son de enteros, hacemos el casting a float
X_float = X_vect.astype(float)

# Reshape para el corpus. 243412 observaciones.
# Los vectores eran de tamaño 100, ahora los convertiremos a matrices 2d de 10 X 10
# que representa el tamaño del embedding 2d
# Para eso hacemos un reshape
X_float_reshaped = X_float.reshape(243412, 10, 10)

# Verificamos el reshape
print(X_float_reshaped[0])

# Verificamos tamaño y forma del dataset
X_float_reshaped.shape

# Aumentamos una dimensión, que representa un canal. Gris por ejemplo
X_float_reshaped = np.expand_dims(X_float_reshaped, axis=-1)

# Verificamos que haya aumentado una dimension
X_float_reshaped.shape

# Creamos las particiones de datos con X_float_reshaped
X2d_temp, X2d_test, y2d_temp, y2d_test = train_test_split(X_float_reshaped, y, test_size=0.2, random_state = 5, stratify = y)
X2d_train, X2d_val, y2d_train, y2d_val = train_test_split(X2d_temp, y2d_temp, test_size=0.25, random_state = 5, stratify = y_temp)
print(f"Documentos de entrenamiento: {X2d_train.shape[0]}")
print(f"Documentos de validación: {X2d_val.shape[0]}")
print(f"Documentos de test: {X2d_test.shape[0]}")
print(f"Número de categorías: {np.unique(y2d_train).size}")

# Definimos el modelo con convoluciones 2D
# El problema es de cuatro clases, la capa softmax llevará 4 neuronas
model_2d = tf.keras.models.Sequential()
model_2d.add(tf.keras.layers.Conv2D(kernel_size=3, activation="relu", filters=32 ,kernel_regularizer=tf.keras.regularizers.l2(l=1e-4)))
model_2d.add(tf.keras.layers.AveragePooling2D(pool_size=(2,2)))
model_2d.add(tf.keras.layers.Conv2D(kernel_size=3, filters=3, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(l=1e-4)))
model_2d.add(tf.keras.layers.AveragePooling2D(pool_size=(2,2)))
model_2d.add(tf.keras.layers.Flatten())
model_2d.add(tf.keras.layers.Dense(32, activation="relu"))
model_2d.add(tf.keras.layers.Dropout(0.2))
model_2d.add(tf.keras.layers.Dense(4, activation="softmax"))

model.summary()

# Codificamos las etiquetas de "y" (que son enteros a one hot encoding) - cod after
yHot2d_train = tf.keras.utils.to_categorical(y2d_train)
yHot2d_val = tf.keras.utils.to_categorical(y2d_val)
yHot2d_test = tf.keras.utils.to_categorical(y2d_test)

# Compilamos el modelo 2d
model_2d.compile(loss="categorical_crossentropy", optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
                metrics=["accuracy"])

best_callback = tf.keras.callbacks.ModelCheckpoint(filepath="model_2d.h5", monitor="val_loss",
                                                   verbose=True, save_best_only=True,
                                                   save_weights_only=True, mode="min")

early_callback = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5,
                                                  min_delta=0.001, verbose=True)

hist_2d = model_2d.fit(X2d_train, yHot2d_train, epochs=50, batch_size =32,
                         validation_data=(X2d_val, yHot2d_val), callbacks=[best_callback,
                                                                    early_callback])

# Graficamos la función de pérdida para las
# particiones de entrenamiento y validación
plt.figure(figsize=(8, 8))
plt.plot(hist_2d.history["loss"], "r", label="Entrenamiento")
plt.plot(hist_2d.history["val_loss"], "r--", label="Validación")
plt.legend(); plt.xlabel("Épocas"); plt.ylabel("Pérdida")

"""### *Evaluación del modelo**
---
"""

# Generamos el reporte de clasificación
# Este classification report es mañoso, y_test debe ser el original y no el Hot Encoded
print(classification_report(y2d_test, np.argmax(model_2d.predict(X2d_test),axis=1)))
