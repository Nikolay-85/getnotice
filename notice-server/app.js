'use strict';

var app = require('express')(),
    conf = require( './config'),
    http = require('http').Server(app),
    redis = require('redis'),
    Q = require('q'),
    argv = require('optimist').argv;

var pub = redis.createClient(),
    sub = redis.createClient(),
    rclient = redis.createClient();


console.log("Connected to redis");

var http = require('http');
var sockjs = require('sockjs');

sub.subscribe('broadcast');

var echo = sockjs.createServer();

echo.on('connection', function(conn) {
    console.log('New client connected')

    sub.on("message", function(channel, message) {
        conn.write(message);
    });

    conn.on('close', function() {
        // cleanup
    });

});

var server = http.createServer();
echo.installHandlers(server, {prefix:'/echo'});
server.listen(9999, '0.0.0.0');


