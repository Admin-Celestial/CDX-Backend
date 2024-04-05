#!/bin/sh

ssh -t ubuntut@34.227.165.129 <<EOF
  cd fairway-api
  git pull 
  source env/bin/activate
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF