#!/bin/sh

ssh -t -i /var/lib/jenkins/private_key ubuntu@54.198.135.250 <<EOF
  cd CDX-Backend
  git pull 
  source env/bin/activate
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF