var sheet = document.styleSheets[2];
var rules = sheet.cssRules || sheet.rules;

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('letterF', function(msg) {
    rules[0].style.backgroundColor = '#' + msg;
    console.log('Received letterF: ' + msg);
});

socket.on('letterO', function(msg) {
    rules[1].style.backgroundColor = '#' + msg;
    console.log('Received letterO: ' + msg);
});

socket.on('letterR', function(msg) {
    rules[2].style.backgroundColor = '#' + msg;
    console.log('Received letterR: ' + msg);
});

socket.on('letterG', function(msg) {
    rules[3].style.backgroundColor = '#' + msg;
    console.log('Received letterG: ' + msg);
});

socket.on('letterE', function(msg) {
    rules[4].style.backgroundColor = '#' + msg;
    console.log('Received letterE: ' + msg);
});