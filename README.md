# README #

Simple notification service.

### Requirements ###

* Vagrant

### Set up ###
#### 1. Demo mode ####
In demo mode you will get server ready to use.
* Install vagrant
* `git clone git@bitbucket.org:michae1/getnotice.git`
* In project folder `S_MODE='demo' vagrant up`.
* After set up open dashboard in browser: http://localhost:8088
* To send message: 

```
#!shell
vagrant ssh
cd getnotice 
./post-message.sh -m 'Hello World' -p 80 -l "warning"

```
#### 2. Developer mode ####
In developer mode you will get developer envirement.
* Install vagrant
* `git clone git@bitbucket.org:michae1/getnotice.git`
* In project folder `vagrant up`.
* To start django development server:
```
#!shell
vagrant ssh
cd getnotice 
./manage.py runserver

```
* Now you can develop django application as usual (Do not forget start notice-server)

### Testing? ###
* To run integration tests for whole system: 
```
#!shell
vagrant ssh
cd getnotice 
./manage test fts

```
* To run unit tests for message API: 
```
#!shell
vagrant ssh
cd getnotice 
./manage test notices

```

### Features ###
* This system can be scaled easily, by multiplying node instances using same redis.
* Realtime messages
* Tested

### Possible Improvements? ###
* In case node instances cannot be in one area redis pub/sub can be replaced by some distributed pub/sub or MQ
* Vagrant provisioning scripts can be replaced by Chief/Ansible to make it easier to deploy multiple nodes.
* Frontend part can be more usefull (auto destroy message after N minutes, auto count time on messages, some css based animations of messages)
* Messages can be accumulated (e.g. in redis zset) to allow any user get full list on page load.
* API can return number of receivers
* Node.js based server can be more complex. For now I have no idea how except config file.