# Ejemplo en Clase
Laboratorio Organización de Lenguajes y Compiladores 2<br>
Sección A

A continuacion se encuentra la continuación del ejemplo visto en la clase anterior. Se realiza la misma interpretación, pero esta vez se genera la estructura de un AST, que puede ser recorrida y está basada en el patrón de diseño `interpreter`. Tambien se utiliza una interfaz gráfica, que fue hecha con React. 

## Prerequisitos

### Python 
Para la instalación de python y pip se recomienda visitar la [documentación oficial.](https://www.python.org/downloads/)

### Ply
Para la utilización de Ply se recomienda la lectura de la [documentación de Ply.](https://github.com/dabeaz/ply).

### Flask
Para instalar Flask se recomienda leer la [documentación.](https://flask.palletsprojects.com/en/2.1.x/)

### Node JS
Para instalar Flask se recomienda leer la [documentación.](https://nodejs.org/es/)

## Utilización del proyecto
Una vez cumplidos los prerequisitos, lo primero que se debe realizar es un entorno virtual de python y activarlo. Para ello se deben correr los siguientes comandos: 

```
mkdir myproject
cd myproject
py -3 -m venv venv
venv\Scripts\activate
```

Una vez iniciado el proyecto se debe instalar todos los paquetes que se utilizan y estan definidos en el archivo [requirements.txt](./requirements.txt)
```
pip install -r requirements.txt
```
Y posteriormente se puede correr en un ambiente de desarrollo la aplicación con el comando
```
flask run
```
