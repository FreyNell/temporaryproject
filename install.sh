docker-compose down
docker-compose up
docker-compose run web python backend/manage.py makemigrations
docker-compose run web python backend/manage.py migrate
docker-compose run web python backend/manage.py loaddata db.yml
