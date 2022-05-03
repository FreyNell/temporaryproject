nohup docker-compose down &
sleep 10
nohup docker-compose up &
sleep 10
nohup docker-compose run web python backend/manage.py makemigrations &
sleep 5
nohup docker-compose run web python backend/manage.py migrate &
sleep 5
nohup docker-compose run web python backend/manage.py loaddata db.json &
sleep 5
echo "Finished"
