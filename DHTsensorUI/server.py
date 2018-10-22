import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import sqlite3 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('New Connection Opened')

    def on_message(self, message):
        
        # connect withe the myTable database 
        connection = sqlite3.connect("localdht.db") 
  
        # cursor object 
        crsr = connection.cursor() 
        
        crsr.execute("SELECT * FROM dht_data ORDER BY Timestamp DESC LIMIT 1")
        data = crsr.fetchone()
        
        Time,Temp,Unit,AvgTemp,HighTemp,LowTemp,Hum,AvgHum,HighHum,LowHum = data
        print('Message Received:  %s' % message)

        if (message == "Get Current Temperature"):
            # Reverse Message and send it back
            print('Sending Current Temperature')
            #print(repr(Time))
            self.write_message(message+","+repr(Temp)+Unit+","+Time)
            
        elif (message == "Get Average Temperature"):
            # Reverse Message and send it back
            print('Sending Average Temperature')
            self.write_message(message+","+repr(AvgTemp)+Unit+","+Time)
            
        elif (message == "Get Highest Temperature"):
            # Reverse Message and send it back
            print('Sending Highest Temperature')
            self.write_message(message+","+repr(HighTemp)+Unit+","+Time)
            
        elif (message == "Get Lowest Temperature"):
            # Reverse Message and send it back
            print('Sending Lowest Temperature')
            self.write_message(message+","+repr(LowTemp)+Unit+","+Time)
            
        elif (message == "Get Current Humidity"):
            # Reverse Message and send it back
            print('Sending Current Humidity')
            self.write_message(message+","+repr(Hum)+"%"+","+Time)
            
        elif (message == "Get Average Humidity"):
            # Reverse Message and send it back
            print('Sending Average Humidity')
            self.write_message(message+","+repr(AvgHum)+"%"+","+Time)
            
        elif (message == "Get Highest Humidity"):
            # Reverse Message and send it back
            print('Sending Highest Humidity')
            self.write_message(message+","+repr(HighHum)+"%"+","+Time)
            
        elif (message == "Get Lowest Humidity"):
            # Reverse Message and send it back
            print('Sending Lowest Humidity')
            self.write_message(message+","+repr(LowHum)+"%"+","+Time)
            
        connection.close()
 
    def on_close(self):
        print('Connection Closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
