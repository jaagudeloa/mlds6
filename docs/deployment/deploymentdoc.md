# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** petdies_clasification, clasificacion de petidos mediante red convolucional !d0
- **Plataforma de despliegue:** FastApi / railway
- **Requisitos técnicos:** 
    - pandas 2.2
    - numpy  1.26
    - tensorflow 2.16
    - nltk 3.8
    - keras
    - sklearn
    - matplotlib
    - python 3.11.5
    - GPU con las siguientes caracteristicas RAM de sistema  12.7 GB RAM de GPU 15.0 GB Disco 78.2 GB

- **Diagrama de arquitectura:** Diagrama de arquitectura esta en imagen adjunta

## Código de despliegue

- **Archivo principal:** main.py
- **Rutas de acceso a los archivos:** los archivos se encuentran en
    - scripts/deployment/labels.json
    - scripts/deployment/main.py
    - scripts/deployment/model_conv1d.h5
    - scripts/deployment/railway.json
    - scripts/deployment/requirements.txt
    - scripts/deployment/tokenizer.pickle
- **Variables de entorno:** 
    - GITHUB: Repositorio donde esta desplegada el API

## Documentación del despliegue

- **Instrucciones de instalación:** El modelo esta desplegado en railway mediante una API construida en FAST API
- **Instrucciones de configuración:** Para acceder al modelo se consume el metodo POST llamado predict de la URL https://peptides-production-ce80.up.railway.app/
- **Instrucciones de uso:** Para el consumo de la API se debe enviar como parametro un json con la siguiente estructura {feature:""} y retorna un JSON con la siguiente estructura {forecast:""} en donde retorna alguno de los siguentes valores "Anti_Cancer", "Anti_Fungi", "Anti_MRSA", "Anti_Viral"
- **Instrucciones de mantenimiento:** Al estar desplegado en railway se refresca automaticamente al momento de realizar un commit en el repositorio
