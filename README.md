# **ETL basico mas uso de dockerfile y docker-compose**

## Despliegue del proyecto

- ### Clonar repositorio y un local
- ### Tener instalado docker y docker-compose sino lo tienes instalados ve [aqui](https://docs.docker.com/engine/install/)
- ### Levantando el proyecto :
    ```
    docker-compose up -d
    ```
## Explicación del proyecto
El proyecto es un etl básico que extrae un archivo csv de una ruta especifica, luego la carga en un dataframe de `pandas`, para aplicarle una serie de transformaciones y lo cargarlo en una base de datos postgres.<br>
El proyecto tiene un Dockerfile y un docker-compose, el Dockerfile construye la aplicación de pyhton que realiza el etl, y con el docker-compose unimos la aplicación de python con la base de datos postgres.

## Entrar al contenedor de la base de datos
```
docker exec -it postgresdb psql -U postgres -d postgres
```
