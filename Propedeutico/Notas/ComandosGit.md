# Comandos Git
## 1- Flujo básico

Una vez creado nuestro repositorio en GitHub, para realizar una copia y poder trabajar en forma local debemos ejecutar los siguientes comandos:  

### 1.1- clone 
Permite hacer una copia del repositorio a un directorio local.
> Ejemplo:  
> git clone https://github.com/your-username/your-repository.git

### 1.2- init
El primer paso es inicializar el repositorio, para que git pueda saber qué hacemos dentro de la carpeta. Para ello abrimos la terminal, nos ubicamos en el directorio de trabajo "cd nombre_carpeta" y ejecutamos el comando **git init**.  
> cd your-repository  
> git init  

### 1.3- add  
Luego de realizar nuestros cambios en forma local, ya sea creando nuevos archivos y/o modificaciones los existentes, debemos agregar los cambios al reposiotrio.   
Se puede hacer archivo por archivo:
> git add archivo1.txt  
> git add archivo2.txt

O podemos añadir todo de una vez con el comando:
> git add -A  
*otra opcion es:*    
> git add .  

### 1.4- commit
Para enviar los cambios al repositorio vamos a usar el siguiente comando:
> git commit -m "Descripción del contenido de la subida"

El **-m "Descripción del contenido de la subida"** es opcional, pero a larga es muy necessario para saber que se ha hecho en esa subida, así que usadlo si o si por favor.

### 1.5- push
Sube los cambios al repositorio:
> git push https://github.com/your-username/your-repository.git


## 2- Validación y Actualización:
### 2.1- status
Comprobar diferencias entre el repositorio y el directorio local:
> git status

### 2.2- Pull
Permite actualizar el repositorio local al último commit.  
> git pull

## 3- Fork  
### Permite trabajar con un repositorio del cual no somos dueños.
### 3.1.- Fork
Desde GitHub debemos generar un **Fork** en el repositorio que queremos trabajar para que nos permita descargarnos nuestra copia local.  
### 3.2.- Clone
En la terminal nos posicionamos en el directorio de trabajo y lo clonamos a nuesto repositorio local para poder modificarlo  
> git clone https://github.com/your-username/fork-proyect.git  

### 3.3.- Hacer los cambios en el dir. local  
### 3.4.- Subir cambios a nuestro repositorio *"forkeado"*:  
> git add -A       
> git commit -m "descripcion de la modificación"  
> git push https://github.com/your-username/fork-proyect.git  

### 3.5.- Pull Request
En nuestro repositorio debemos crear un **Pull Request** para que el propietario del repositorio origianl incorpore los cambios.

## 4- Actualizar un proyecto *"forkeado"* en Github  
Cuando realizamos el fork de un proyecto en Github para realizar algún cambio al proyecto y realizar un Pull Request con nuestras modificaciones suele pasar que el proyecto del que realizamos el fork ya fue actualizado muchas veces y nuestros cambios podrían entrar en conflicto. Para evitar esto es conveniente realizar la actualización de nuestro repositorio forkeado, para lo cuál podemos hacer lo siguiente:  

Una vez realizado el fork del proyecto, lo que normalmente hacemos es clonar nuestro proyecto:  

> git clone https://github.com/your-username/fork-repository.git      
> cd proyecto  

Lo que tenemos que hacer después es agregar el repositorio padre como un origen remoto.  

> git remote add upstream https://github.com/original/fork-repository.git   
> git fetch upstream  

Con el último comando lo que hicimos fue hacer un Pull a los cambios que hay en el repositorio original pero sin mezclarlo en nuestra repositorio.  

Si queremos actualizar nuestro repositorio con los cambios del repositorio padre utilizamos los siguientes comandos:  

> git fetch upstream  
> git merge upstream/master  

Con eso estamos mezclando la rama master del repositorio padre, a nuestra rama, si queremos mezclar otra rama loa cambiamos en el último comando.  
