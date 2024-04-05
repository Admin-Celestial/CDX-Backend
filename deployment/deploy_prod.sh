#!/bin/sh

ssh -t ubuntut@54.198.135.250 <<EOF
  cd fairway-api
  git pull 
  source env/bin/activate
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF