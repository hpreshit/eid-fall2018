var AWS = require("aws-sdk");

var QUEUE_URL1 = queue_url;

var sqs = new AWS.SQS();

var maxTemp = 0;
var minTemp = 0;
var maxHum = 0;
var minHum = 0;
var avgTemp = 0;
var avgHum = 0;
var sampleCount = 0;



exports.handler = function(event, context) {
    console.log('timestamp =', event.timestamp);
    console.log('temperature =', event.temperature);
    console.log('humidity =', event.humidity); 
    
    avgTemp = ((parseFloat(avgTemp)*sampleCount)+parseFloat(event.temperature))/(sampleCount+1);
    avgTemp = avgTemp.toFixed(2);
    console.log("avg Temp ",avgTemp);
    
    avgHum = ((parseFloat(avgHum)*sampleCount)+parseFloat(event.humidity))/(sampleCount+1);
    avgHum = avgHum.toFixed(2);
    console.log("avg Hum ",avgHum);
    
    maxTemp = Math.max(event.temperature,maxTemp);
        
    minTemp = Math.min(event.temperature,minTemp);
    
    maxHum = Math.max(event.humidity,maxHum);
        
    minHum = Math.min(event.humidity,minHum);
    
    if(minTemp==0){
        minTemp = event.temperature;   
    }
    
    if(minHum==0){
        minHum = event.humidity;   
    }
    
    sampleCount = sampleCount+1;
    
    var sendParams = {
        MessageBody: event.timestamp + "," + event.temperature + "," +avgTemp+ "," +maxTemp+ "," +minTemp+ "," +event.humidity+ "," +avgHum+ "," +maxHum+ "," +minHum,
        MessageGroupId: 'sensordata',
        QueueUrl: QUEUE_URL1
    };
    
    sqs.sendMessage(sendParams, function(err,data){
        if(err) {
            console.log("Error in SendMessage to 1st Queue");
            context.done('error', "ERROR Put SQS");  // ERROR with message
        }else{
            console.log("Message Sent to 1st Queue");
            context.done(null,'');  // SUCCESS
        }
    });
}; 