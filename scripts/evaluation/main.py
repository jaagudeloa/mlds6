# Graficamos la función de pérdida para las
# particiones de entrenamiento y validación
plt.figure(figsize=(8, 8))
plt.plot(hist_2d.history["loss"], "r", label="Entrenamiento")
plt.plot(hist_2d.history["val_loss"], "r--", label="Validación")
plt.legend(); plt.xlabel("Épocas"); plt.ylabel("Pérdida")

"""### **4.1.2. Evaluación del modelo**
---
"""

# Generamos el reporte de clasificación
# Este classification report es mañoso, y_test debe ser el original y no el Hot Encoded
print(classification_report(y2d_test, np.argmax(model_2d.predict(X2d_test),axis=1)))
