var q = 'gnq';

var open = require('amqplib').connect('amqp://guest:guest@localhost');

// Consumer
open.then(function(conn) {
  console.log('opened')
  var ok = conn.createChannel();
  console.log('ok', ok)
  ok = ok.then(function(ch) {
    console.log('ok ok ')
    ch.assertQueue(q, {durable: false});
    ch.consume(q, function(msg) {
      console.log('consumed')
      if (msg !== null) {
        console.log(msg.content.toString());
        ch.ack(msg);
      }
    });
  });
  return ok;
}).then(null, console.warn);