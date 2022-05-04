# temporaryproject
Repo for temporary projects
if you want to backup your database data:
docker-compose run web python backend/manage.py dumpdata --exclude contenttypes --format=json > db.json


Pasos de instalación:

1. Tener docker instalado. Si estás en una máquina windows, instalate Docker Desktop.
2. En una consola de WSL ingresa el comando: ```git clone https://github.com/FreyNell/temporaryproject```
3. luego ejecuta el comando: ```cd temporaryproject```
4. Ejecuta  ```bash install.sh```.
5. Esperas a que termine.
6. Entras a la web ```http://localhost:8000``` en un navegador cualquiera.