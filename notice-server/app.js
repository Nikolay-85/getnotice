var amqp = require('amqp');

var connection = amqp.createConnection({
    host: 'localhost',
    vhost: 'gn',
    login: 'gn',
    password: 'gn'});

// Wait for connection to become established.
console.log('connecting');
connection.on('ready', function () {
  // Use the default 'amq.topic' exchange
  connection.queue('my-queue', function (q) {
        console.log('ready');
      // Catch all messages
      q.bind('#');

      // Receive messages
      q.subscribe(function (message) {
        // Print messages to stdout
        console.log(message);
      });
  });
});