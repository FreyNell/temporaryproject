# temporaryproject
Repo for temporary projects
if you want to backup your database data:
docker-compose run web python backend/manage.py dumpdata --exclude contenttypes --format=json > db.json
