# Comandos Git

## 1- clone 
Clonar el repositorio en nuestra carpeta.  
Comando: git clone "url del repositorio".  
> Ejemplo:  
> git clone https://github.com/avallarino-ar/MCDatos

## 2- init
El primer paso es inicializar el repositorio, para git pueda saber que hacemos dentro de la carpeta. Para ello abrimos la terminal, nos vamos a nuestra carpeta con el comando "cd nombre_carpeta" y ejecutamos luego el comando "git init".  

> cd MCDatos 
> git init  

## 3- status
Comprueba si hemos modificado algo en la carpeta y que podemos añadir al repositorio. 
> git status

## 4- add
Podemos añadir los archivos uno a uno al repositorio con:
> git add archivo1.txt  
> git add archivo2.txt

O podemos añadir todo de una vez con el comando:
> git add -A  
> git add .

## 5- commit
Para subir los cambios al repositorio vamos a usar el siguiente comando
> git commit -m "mensaje de ayuda para la subida"

El -m "mensaje de ayuda para la subida" es opcional, pero a larga es muy necessario para saber que se ha hecho en esa subida, así que usadlo si o si por favor.

## 6- push
Enviar los cambios al repositorio: git push "url del repositorio"  
> git push https://github.com/avallarino-ar/MCDatos

## 7- Pull
Para actualizar tu repositorio local al último commit, ejecutar git pull en tu directorio local.
> git pull

# En caso de no se dueño de la cuenta:  
1.- Fork: Permite traer a nuestra cuenta el repositorio a modificar.  
2.- Clone: en el terminat nos posicionamos en el directorio de trabajo y lo clonamos a nuesto repositorio local para poder modificarlo  
> git clone https://github.com/avallarino-ar/PropedeuticoDataScience2017.git  
3.- Hacer los cambios en el dir. local  
4.- Subir cambios a nuestra cuenta:  
> git push  
> git add -A
> git commit -m "descripcion de la modificación"
> git push
