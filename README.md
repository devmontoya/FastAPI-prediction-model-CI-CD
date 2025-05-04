# FastAPI-prediction-model-CI/CD

En este proyecto se despliega en GCP una API usando FastAPI donde el proceso CI/CD es llevado por dos pipelines en Github actions.
Esta API sirve un modelo sencillo de predicción de precios de celulares con base en sus características, el desarrollo de este es ampliamente explorado en este repositorio [project-mobile-phone-classification_deploy](https://github.com/devmontoya/project-mobile-phone-classification_deploy)

Una vez desplegado localmente o usando la URL: [fastapi-prediction-model-cicd](https://fastapi-prediction-model-cicd-51073707783.us-central1.run.app/) puede realizarse una prueba sencilla de predicción usando el archivo `xtest.json`


## Pasos para realizar un despliegue localmente

- `python -m venv venv`
- `pip install -r requirements.txt`
- `uvicorn app:app --reload`

## Pasos para realizar un despliegue local usando docker

- `docker build -t fastapi-pm .`
- `podman run --rm -p 4030:4030 fastapi-pm`
