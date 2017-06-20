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

# Fork  
### Permite trabajar con un repositorio del cual no somos dueños.
1.- Fork: Permite traer a nuestra cuenta el repositorio a modificar.  
2.- Clone: en el terminat nos posicionamos en el directorio de trabajo y lo clonamos a nuesto repositorio local para poder modificarlo  
> git clone https://github.com/avallarino-ar/PropedeuticoDataScience2017.git  

3.- Hacer los cambios en el dir. local  
4.- Subir cambios a nuestra cuenta:  
> git push    
> git add -A       
> git commit -m "descripcion de la modificación"  
> git push  

5.- En el Hub crear Pull Request

# Actualizar un proyecto "forkeado" en Github  

Cuando realizamos el fork de un proyecto en Github para realizar algún cambio al proyecto y realizar un Pull Request con nuestras modificaciones suele pasar que el proyecto del que realizamos el fork ya fue actualizado muchas veces y nuestros cambios podrían entrar en conflicto. Para evitar esto es conveniente realizar la actualización de nuestro repositorio forkeado, para lo cuál podemos hacer lo siguiente:  

Una vez realizado el fork del proyecto, lo que normalmente hacemos es clonar nuestro proyecto:  

> git clone https://github.com/username/proyecto.git    
> cd proyecto  

Lo que tenemos que hacer después es agregar el repositorio padre como un origen remoto.  

> git remote add upstream https://github.com/original/proyecto.git  
> git fetch upstream  

Con el último comando lo que hicimos fue hacer un Pull a los cambios que hay en el repositorio original pero sin mezclarlo en nuestra repositorio.  

Si queremos actualizar nuestro repositorio con los cambios del repositorio padre utilizamos los siguientes comandos:  

> git fetch upstream  
> git merge upstream/master  

Con eso estamos mezclando la rama master del repositorio padre, a nuestra rama, si queremos mezclar otra rama loa cambiamos en el último comando.  
