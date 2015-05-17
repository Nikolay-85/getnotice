# README #

Simple notification service. 

Command line utility sends messages using REST. Django side (API) receives this messages and publishes it via redis. Node.js based server subscribes to this channel and serves clients connections. It pushes this messages to clients.

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
./tools/post-message.sh -m 'Hello World' -p 80 -l "warning"

```
* You should get something like this:
![Selection_033.png](https://bitbucket.org/repo/jr74qK/images/3206648382-Selection_033.png)

#### 2. Developer mode ####
In developer mode you will get developer environment.

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
* Frontend part can be more usefull (auto destroy message after N minutes, auto count time on messages, some css based animations of messages). Anyway I need to understand ember.js concepts deeply.
* Messages can be accumulated (e.g. in redis zset) to allow any user get recent list on page load.
* API can return number of receivers
* Node.js based server can be more complex. For now I have no idea which feature i can add except configuration file support.
* Django settings should be divided into dev/prod/qa (not necessary for now)
* If moving to production some parts of this system should be separated to its own repository (because it would be deployed separately)