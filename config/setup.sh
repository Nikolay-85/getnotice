#!/bin/bash

# Script to set up a Django project on Vagrant.

# Installation settings
echo "Setting up messaging server"
echo $1

PROJECT_NAME=getnotice

DB_NAME=$PROJECT_NAME
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME
LOCAL_SETTINGS_PATH="/$PROJECT_NAME/settings/local.py"

DBPASSWD=gn
DBNAME=gn
DBUSER=gn


apt-get update -y
apt-get install -y python python-dev

apt-get -y install vim curl build-essential python-software-properties git

add-apt-repository ppa:chris-lea/node.js > /dev/null 2>&1

apt-get install -y python-pip
apt-get install -y libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev

apt-get -y install nodejs
apt-get -y install npm
apt-get -y install libmysqlclient-dev
apt-get -y install redis-server

echo -e "\n--- Install MySQL specific packages and settings ---\n"
echo "mysql-server mysql-server/root_password password $DBPASSWD" | debconf-set-selections
echo "mysql-server mysql-server/root_password_again password $DBPASSWD" | debconf-set-selections
apt-get install -y mysql-server

mysql -uroot -p$DBPASSWD -e "CREATE DATABASE $DBNAME"
mysql -uroot -p$DBPASSWD -e "grant all privileges on $DBNAME.* to '$DBUSER'@'localhost' identified by '$DBPASSWD'"

if [[ ! -f /usr/local/bin/virtualenv ]]; then
    pip install virtualenv virtualenvwrapper stevedore virtualenv-clone
fi

# JS related
# TODO npm install, bower install
# bower compatibility
ln -s /usr/bin/nodejs /usr/bin/node
cd $PROJECT_DIR
npm install -g bower
su - vagrant -c "npm install"
su - vagrant -c "bower install --config.interactive=false"

# virtualenv setup for project
su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    $VIRTUALENV_DIR/bin/pip install -r $PROJECT_DIR/requirements.txt"

echo "source $VIRTUALENV_DIR/bin/activate" >> /home/vagrant/.bashrc

# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

# Django project setup
su - vagrant -c "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && ./manage.py syncdb --noinput && ./manage.py migrate"

# Rabbitmq related
#apt-get -y install rabbitmq-server
#rabbitmqctl add_vhost gn
#rabbitmqctl add_user gn gn
#rabbitmqctl set_permissions -p gn gn ".*" ".*" ".*"

# Test environment (headless firefox etc)
apt-get install -y Xvfb
apt-get install -y libasound2
apt-get install -y libdbus-glib-1-dev 
echo "deb http://packages.linuxmint.com debian import" >> /etc/apt/sources.list
apt-get update
apt-get install -y --force-yes firefox
  

if [ $1 == "demo" ]; then
  echo "Setting up demo machine"
  apt-get install -y upstart
  apt-get install -y apache2 apache2.2-common apache2-mpm-prefork apache2-utils libexpat1 ssl-cert
  apt-get install -y libapache2-mod-wsgi
  
  # node service
  cp /home/vagrant/getnotice/config/node-srv /etc/init.d/
  chmod +x /etc/init.d/node-srv 
  update-rc.d node-srv defaults
  /etc/init.d/node-srv start
  
  # apache virtual
  cp /home/vagrant/getnotice/config/mserver.conf /etc/apache2/sites-available/
  ln -s /etc/apache2/sites-available/mserver.conf /etc/apache2/sites-enabled/
  unlink /etc/apache2/sites-enabled/000-default.conf
  /etc/init.d/apache2 reload

  # static files
  su - vagrant -c "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && ./manage.py collectstatic --noinput"


  

fi
