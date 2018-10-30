var http = require('http');
var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Hello content!', function(err) {
	if (err) throw err;
	console.log('Saved!');
});

fs.open('mynewfile2.txt', 'w', function(err, file) {
	if (err) throw err;
	console.log('Saved!');
});

fs.writeFile('mynewfile3.txt','Hello content!', function(err) {
	if (err) throw err;
	console.log('Saved!');
});

fs.appendFile('mynewfile1.txt', 'This is my text', function(err) {

});

fs.writeFile('mynewfile3.txt', 'replace it', function(err) {

});

fs.unlink('mynewfile2.txt', function(err) {

});
/*
http.createServer(function (req, res) {
  fs.readFile('demofile1.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });
}).listen(8080);*/