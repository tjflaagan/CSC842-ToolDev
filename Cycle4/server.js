var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var metasploitClient = require('msfnode');


var activeConsole = 0;
var data;

var onConnect = function(err,token) {
    if (err) {
        console.log(err.error_message);
        process.exit(0);
    }
    metasploitVersion();
    startConsole();
}

var metasploitVersion = function() {

    var args = ['core.version'];

    client.exec(args,function(err,r) {

        if (err) return console.log('Error: '+err);
        console.log('-> Version: '+r.version);
        console.log('-> Api: '+r.api);
        console.log('-> Ruby: '+r.ruby);
    });

    var args = ["console.create"];
   
	client.exec(args, function(err,r) {
		if (err) return console.log('Error: '+err);
		activeConsole = r;
		console.log(activeConsole.id);

	});	
}

var startConsole = function(err,token){
	if(err){
		console.log(err.error_message);
		process.exit(0);
	}
	var args = ["console.list"];
	client.exec(args, function(err,r) {
		if (err) return console.log('Error: '+err);
		console.log(r);

	});
}


var client = new metasploitClient({
    login:'msf',
    password:'test',
    host:'192.168.159.128',   // optional
    port:55553,         // optional
    protocol:'https',   // optional
    apiVersion:'1.0',   // optional
    apiPath:'/api/'     // optional
});

client.on('connected',onConnect);



// Create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use(express.static('public'));
app.get('/index.htm', function (req, res) {
   res.sendFile( __dirname + "/" + "index.htm" );

   	client.exec(["console.read", activeConsole.id], function(err,r) {
   		if (err) return console.log('Error: '+err);
   })
})



app.post('/index.htm', urlencodedParser, function (req, res) {
   // Prepare output in JSON format
   response = {
      command: req.body.command,
   };


   client.exec(["console.write", activeConsole.id, req.body.command+"\n"],  function(err,r){
   		if (err) return console.log('Error: '+err);
   		console.log(r);

   })

   client.exec(["console.read", activeConsole.id], function(err,r) {
   		if (err) return console.log('Error: '+err);
   		console.log(r);
   		console.log(r.data.toString());
   		data = r.data.toString();
   })
   
   console.log(response);
   // res.end(JSON.stringify(response));
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Running at http://%s:%s", host, port)

})

