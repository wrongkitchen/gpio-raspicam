var Gpio = require('onoff').Gpio;
var RaspiCam = require("raspicam");
var client = require('scp2')

var button = new Gpio(18, 'in', 'both');

var pending = true;

var deviceNumber = 'cam1';

var camera = new RaspiCam({
	mode: "photo",
	output: "./photo/image.jpg",
	encoding: "jpg",
	width: '1920',
	height: '1080',
	timeout: 5 // take the picture immediately
});

camera.on("started", function( err, timestamp ){
	console.log("photo started at " + timestamp );
});

camera.on("exit", function( timestamp ){
	console.log("photo child process has exited at " + timestamp + ", start upload.");
	client.scp('./photo/image.jpg', 'admin:19880622@wrongkitchen.mycloudnas.com:/share/HDA_DATA/Qweb/scp2/'+ deviceNumber + timestamp + '.jpg', function(err) {
		if(err)
			console.log(err);
		else
			console.log('Upload done without error.');
		pending = true;
	})
	
});

button.watch(function(err, value) {
	if(value && pending){
		pending = false;
		camera.start();		
	}
});
