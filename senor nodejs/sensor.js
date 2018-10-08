//@author - Preshit Harlikar
//@node version - v10.11.0
//@reference - https://github.com/momenso/node-dht-sensor

//import library
var sensor = require('./node-dht-sensor');

console.log('');

//Initialize variables
var temp = [];
var hum = [];
var tempsum = 0;
var humsum = 0;
var i = 0;

//read data from sensor
var iid = setInterval(function() {
	sensor.read(22, 4, function(err, temperature, humidity) {
	    if (err){ 
		console.warn('' + err);
	    }
	    else{
		temp[i] = ((temperature*1.8)+32).toFixed(1);
		hum[i] = humidity.toFixed(1);
		tempsum = (tempsum + +temp[i]);
		humsum = (humsum + +hum[i]);
	     	console.log("%d - Temperature: %s°F, Humidity: %s%%",i+1,temp[i],hum[i]);
		i++;
		if(i==10){
			console.log('');
			console.log("Lowest Temp : %s°F", Math.min(...temp));
			console.log("Lowest Hum  : %s%%", Math.min(...hum));
			console.log("Highest Temp: %s°F", Math.max(...temp));
			console.log("Highest Hum : %s%%", Math.max(...hum));
			console.log("Average Temp: %s°F", (tempsum/10).toFixed(1));
			console.log("Average Hum : %s%%", (humsum/10).toFixed(1));
			console.log('');
			console.log('');
			i = 0;
			tempsum = 0;
			humsum = 0;
		}	
	    }
	});
}, 1000);
