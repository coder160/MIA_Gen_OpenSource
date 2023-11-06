# MIA_Gen_BackEnd
**M**i **I**nteligencia **A**rtificial **Gen**erativa de Código Abierto
*BackEnd*


## Pre-Requisitos:


Hardware:

*   Sistema Operativo           :   **Linux**
*   Espacio Libre               :   **40 GB**
*   Tarjeta RAM                 :    **8 GB**
*   Tarjeta VRam(Video)         :   **14 GB**

Software:

*   Docker

Siga las instrucciones para instalar su servidor 
**Verifique los prerequisitos en caso de no tener instalado Docker o FastApi*


0)  **mkdir pruebas; cd pruebas**

    *Crea tu directorio en la ubicación que desees y accede a él.*

1)  **git clone https://github.com/coder160/fastapi_docker_template**
   
    *Clona el reposito en tu directorio local desde mis repositorios.*

2)  **cd fastapi_docker_template**
    
    *Una vez descargado/clonado, accede a la carpeta principal del proyecto.*

3)  **docker build -t fastapi_image_test .**
    
    *Construye la 'fastapi_image_test" utilizando todos los archivos dentro del directorio.*
    *Importante incluir el punto final '.'*

4)  **docker run -d --name fastapi_container_test p-8080:9028 fastapi_image_test**
    
    *Crea tu contenedor llamado 'fastapi_container_test' y lo corre en el puerto 8080 de tu máquina local,
    desde el puerto 9028 configurado en el Dockerfile corriendo en tu máquina virtual, utilizando la imagen
    previamente creada 'fastapi_image_test'*
    
5)  **docker ps**
    
    *Verifica que tu contenedor esté corriendo, deberías tener algo similar a la siguiente información:*
    *CONTAINER ID    IMAGE              COMMAND  CREATED  STATUS       PORTS            NAMES*
    *xxxxxxxxxxxx  fastapi_image_test  xxxxxxxx  xxxxxxx    up        8080:9028   fastapi_container_test*
    
6)  **http://localhost:8080/docs**
    
    *Accede a la ruta de tu localhost, en el puerto 8080 para acceder al método principal de tu api.*
    *Accede a la ruta /docs para instanciar el modo de pruebas por defecto de FastApi.*






## Agradecimientos Especiales

Gracias a las siguientes herramientas colaborativas de código abierto este proyecto es posible

| Sitio_Oficial                                     | Repositorio   |
| -------------------------------------             | ------------- |
| [Python](https://www.python.org/)                 | [![](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/python)        |
| [Docker](https://huggingface.co)                  | [![](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/docker)        |
| [FastApi](https://fastapi.tiangolo.com/)          | [![](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tiangolo/fastapi)|
