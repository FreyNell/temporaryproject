#!/bin/bash
# progress bar function
prog() {
    local w=80 p=$1;  shift
    # create a string of spaces, then change them to dots
    printf -v dots "%*s" "$(( $p*$w/100 ))" ""; dots=${dots// /.};
    # print those dots on a fixed-width space plus the percentage etc. 
    printf "\r\e[K|%-*s| %3d %% %s" "$w" "$dots" "$p" "$*"; 
}

docker-compose down
nohup docker-compose up &

# test loop
for x in {1..100..10} ; do
    prog "$x" still working...
    sleep 1   # do some work here
done ; echo

docker-compose run web python backend/manage.py makemigrations
docker-compose run web python backend/manage.py migrate
docker-compose run web python backend/manage.py loaddata db.json