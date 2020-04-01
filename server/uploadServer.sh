#!/bin/bash

password=$1
user=$2

folder='fairness-algorithm-rest'

echo "Creating App folder"
echo $password | sudo mkdir -p /var/www/html/$folder
echo $password | sudo chown $user:$user /var/www/html/$folder
cd /var/www/html/$folder/
git clone https://github.com/DanielAbergel/Distribution-Algorithm.git .
cd /server

echo 'Installing Environment dependencies and python Virtual Environment'
echo $password | sudo apt-get install python3-pip python3-dev libpq-dev
echo $password | pip3 install virtualenv
echo $password | sudo apt-get install virtualenv
echo $password | virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
deactivate

# -- uWSGI Install --
echo 'setting uWSGI service'
echo $password | sudo mv /var/www/html/$folder/server/devTools/uwsgi_fairness_algorithm_rest.service /etc/systemd/system/uwsgi_fairness_algorithm_rest.service
echo $password | sudo systemctl start uwsgi_fairness_algorithm_rest
uwsgiExitCode=$?
if [[ "$secssesfullMake" -gt 0 ]]; then
echo "uWSGI problem has occured please check '/etc/systemd/system/uwsgi_fairness_algorithm_rest.service' and uwsgi.ini files"
exit 1
fi

# -- NGINX Install --
echo 'Installing NGINX'
echo $password | sudo apt-get install nginx

echo 'Enable UFW (ubuntu firewall)'
echo $password | sudo ufw allow 'Nginx HTTP'
echo $password | sudo ufw allow ssh
echo $password | sudo ufw enable

echo 'setting NGINX configurtion'
echo $password | sudo mv /var/www/html/$folder/server/devTools/fairness-algorithm-rest.conf /etc/nginx/sites-available/fairness-algorithm-rest.conf
echo $password | sudo rm /etc/nginx/sites-enabled/default
echo $password | sudo ln -s /etc/nginx/sites-available/fairness-algorithm-rest.conf /etc/nginx/sites-enabled/
echo $password | sudo systemctl start nginx
if [[ "$secssesfullMake" -gt 0 ]]; then
echo "NGINX problem has occured please check '/etc/nginx/sites-available/fairness-algorithm-rest.conf' "
exit 1
fi

echo $password | sudo systemctl reload nginx
echo $password | sudo systemctl restart nginx
