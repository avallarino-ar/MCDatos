# Comandos Git
## Comandos para trabajar con Git en local

## 1- clone
Clonar el repositorio en nuestra carpeta.
Comando "git clone"
Ejemplo:
  git clone https://github.com/avallarino-ar/MCDatos

## 2- init
El primer paso es inicializar el repositorio, para git pueda saber que hacemos dentro de la carpeta. Para ello abrimos la terminal, nos vamos a nuestra carpeta con el comando "cd nombre_carpeta" y ejecutamos luego el comando "git init"
  cd repo-ejemplo
  git init  

## 3- status
Comprueba si hemos modificado algo en la carpeta y que podemos añadir al repositorio. 
  git status

## 4- add
Podemos añadir los archivos uno a uno al repositorio con:
  git add archivo1.txt
  git add archivo2.txt

O podemos añadir todo de una vez con el comando:
  git add .

## 5- commit
Para subir los cambios al repositorio vamos a usar el siguiente comando
  git commit -m "mensaje de ayuda para la subida"

El -m "mensaje de ayuda para la subida" es opcional, pero a larga es muy necessario para saber que se ha hecho en esa subida, así que usadlo si o si por favor.

## 6- push
Envía los cambios al repositorio:
	git push <url del repositorio>
