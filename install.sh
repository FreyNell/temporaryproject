docker-compose run web python backend/manage.py makemigrations
docker-compose run web python backend/manage.py migrate
docker-compose run web python backend/manage.py loaddata db.json
