App = Ember.Application.create();

App.Message = Ember.Object.extend({});

App.Router.map(function() {
  this.resource('messages', { path: '/' });
});

App.ApplicationRoute = Ember.Route.extend({
  model: function () {
    return [];
  },
});

App.MessagesController = Ember.ArrayController.extend({
    time: null,
    text: null,
    init: function () {
        this._super.apply(this, arguments);
        var _this = this,
            recInterval,
            retryNum = 0;

        var newConnection = function(){
            var sock = new SockJS(globalConfig.messagingServerUrl);

            sock.onopen = function() {
                clearInterval(recInterval);
                console.log('connection open', retryNum ? 'after '+retryNum+'retry number': '');
            };
            sock.onmessage = function(e) {
                var message;
                try {
                    message = JSON.parse(e.data);
                } catch (e) {
                    console.log('invalid message receved')
                    return false;
                }
                 
                var adoptedMesage = {'text': message.text, 'time': new Date(message.time*1000)};
                _this.get('content').unshiftObject(App.Message.create(adoptedMesage));
                
            };
            sock.onclose = function() {
               console.log('close, reconnect');
               retryNum++;
               recInterval = setTimeout(function () {
                    newConnection();
                }, 2000);
            };
        }
        newConnection();
    }
});

Ember.Handlebars.registerBoundHelper('timeFormatted', function(d) {
  return [
            d.getHours(),
            d.getMinutes(),
            d.getSeconds()
        ].join(':');
});