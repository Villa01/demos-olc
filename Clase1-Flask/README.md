# Ejemplo en Clase
Laboratorio Organización de Lenguajes y Compiladores 2<br>
Sección A

A continuación se encuentra un ejemplo de un servidor backend con Flask, que es consumido a través de una interfaz web simple, a través de JavaScript. El servidor realiza la tarea de procesar procesar una entrada, en este caso operaciones matemáticas. 

## Prerequisitos

### Python 
Para la instalación de python y pip se recomienda visitar la [documentación oficial.](https://www.python.org/downloads/)

### Ply
Para la utilización de Ply se recomienda la lectura de la [documentación de Ply.](https://github.com/dabeaz/ply).

### Flask
Para instalar Flask se recomienda leer la [documentación.](https://flask.palletsprojects.com/en/2.1.x/)

## Utilización del proyecto
Una vez cumplidos los prerequisitos, lo primero que se debe realizar es un entorno virtual de python y activarlo. Para ello se deben correr los siguientes comandos: 

```
mkdir myproject
cd myproject
py -3 -m venv venv
venv\Scripts\activate
```

Una vez iniciado el proyecto se debe instalar Flask con el siguiente comando: 
```
pip install Flask
```
Y posteriormente se puede correr en un ambiente de desarrollo la aplicación con el comando
```
flask run
```
Para utilizar Ply se debe descargar la versión compatible del repositorio oficial y descomprimir la carpeta `Ply` dentro del proyecto. 