  // log function
  log = function(data){
    $("div#terminal").prepend("</br>" +data);
    console.log(data);
  };

  $(document).ready(function () {

    $("div#value_details").hide();
    $("div#security_details").show();
    $("div#connection_details").show();

    var ws;

    // $("#signIn").click(function(evt) {
    // // evt.preventDefault();
    // var a="pi";
    // var b="pi";
    //
    // if (($("#usernameVal").val()==a) && ($("#passwordVal").val()== b))
    // {
    //     $("#value_details").hide();
    //     $("#security_details").hide();
    //     $("#connection_details").show();
    // }
    // else
    //   alert("Wrong Username and Password");
    // });

    $("#open").click(function(evt) {
      evt.preventDefault();

      var host = $("#host").val();
      var port = 8888;
      var uri = "/ws";

      var a="pi";
      var b="pi";

      if (($("#usernameVal").val()==a) && ($("#passwordVal").val()== b))
      {
          // create websocket instance
          ws = new WebSocket("ws://" + host + ":" + port + uri);
          $("div#value_details").show();
          $("#usernameVal").val('');
          $("#passwordVal").val('');
          $("#host").val('');
          $("#host").css("background", "#00ff00");
          alert("Connection Established");
          // $("#security_details").hide();
          // $("#connection_details").show();
      }
      else
      {
        alert("Wrong Username and Password");
        $("#host").css("background", "#F5F5F5");
        $("#host").val('');
      }
      // $("#value_details").show();

      // Handle incoming websocket message callback
      ws.onmessage = function(evt) {
       var str_array = evt.data.split(',');
       if (str_array[0]=="Get Current Temperature")
          {
              $("#curTempVal").val(str_array[1].toString());
                $("#curTempTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Current Humidity")
          {
              $("#curHumVal").val(str_array[1].toString());
                $("#curHumTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Average Temperature")
          {
              $("#avgTempVal").val(str_array[1].toString());
                $("#avgTempTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Average Humidity")
          {
              $("#avgHumVal").val(str_array[1].toString());
                $("#avgHumTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Highest Temperature")
          {
              $("#highTempVal").val(str_array[1].toString());
                $("#highTempTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Highest Humidity")
          {
              $("#highHumVal").val(str_array[1].toString());
                $("#highHumTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Lowest Temperature")
          {
              $("#lowTempVal").val(str_array[1].toString());
                $("#lowTempTS").val(str_array[2].toString());
            }
        else if (str_array[0]=="Get Lowest Humidity")
          {
              $("#lowHumVal").val(str_array[1].toString());
                $("#lowHumTS").val(str_array[2].toString());
            }

        else if (str_array[0]=="Sensor Disconnected")
          {
            alert("Sensor Disconnected");
            $("#curTempVal").val('');
            $("#curTempTS").val('');
            $("#curHumVal").val('');
            $("#curHumTS").val('');
            $("#avgTempVal").val('');
            $("#avgTempTS").val('');
            $("#avgHumVal").val('');
            $("#avgHumTS").val('');
            $("#highTempVal").val('');
            $("#highTempTS").val('');
            $("#highHumVal").val('');
            $("#highHumTS").val('');
            $("#lowTempVal").val('');
            $("#lowTempTS").val('');
            $("#lowHumVal").val('');
            $("#lowHumTS").val('');
            $("div#value_details").hide();
            }

        };

      // Close Websocket callback
      ws.onclose = function(evt) {
        log("***Connection Closed***");
        alert("Connection closed");
        $("#host").css("background", "#F5F5F5");
        $("#host").val('');
        // $("#port").css("background", "#ff0000");
        // $("#uri").css("background",  "#ff0000");
        $("#curTempVal").val('');
        $("#curTempTS").val('');
        $("#curHumVal").val('');
        $("#curHumTS").val('');
        $("#avgTempVal").val('');
        $("#avgTempTS").val('');
        $("#avgHumVal").val('');
        $("#avgHumTS").val('');
        $("#highTempVal").val('');
        $("#highTempTS").val('');
        $("#highHumVal").val('');
        $("#highHumTS").val('');
        $("#lowTempVal").val('');
        $("#lowTempTS").val('');
        $("#lowHumVal").val('');
        $("#lowHumTS").val('');
        $("div#value_details").hide();

        };

      // Open Websocket callback
      ws.onopen = function(evt) {
        $("#host").css("background", "#00ff00");
        // $("#port").css("background", "#00ff00");
        // $("#uri").css("background", "#00ff00");
        log("***Connection Opened***");
      };
    });


    // Send websocket message function
    $("#send").click(function(evt) {
        log("Sending Message: "+$("#message").val());
        ws.send($("#message").val());

    });


    $("#curTemp").click(function(evt) {
      ws.send($("#curTemp").val());
     });

    $("#curHum").click(function(evt) {
       ws.send($("#curHum").val());
    });

    $("#avgTemp").click(function(evt) {
      ws.send($("#avgTemp").val());
    });

    $("#avgHum").click(function(evt) {
      ws.send($("#avgHum").val());
    });

    $("#highTemp").click(function(evt) {
      ws.send($("#highTemp").val());
    });

    $("#highHum").click(function(evt) {
      ws.send($("#highHum").val());
    });

    $("#lowTemp").click(function(evt) {
      ws.send($("#lowTemp").val());
    });

    $("#lowHum").click(function(evt) {
      ws.send($("#lowHum").val());
    });

    $("#close").click(function(evt) {
      evt.preventDefault();
      ws.close();
      log("***Connection Closed***");
      $("#host").css("background", "#ff0000");
      // $("#port").css("background", "#ff0000");
      // $("#uri").css("background",  "#ff0000");
      $("#curTempVal").val('');
      $("#curTempTS").val('');
      $("#curHumVal").val('');
      $("#curHumTS").val('');
      $("#avgTempVal").val('');
      $("#avgTempTS").val('');
      $("#avgHumVal").val('');
      $("#avgHumTS").val('');
      $("#highTempVal").val('');
      $("#highTempTS").val('');
      $("#highHumVal").val('');
      $("#highHumTS").val('');
      $("#lowTempVal").val('');
      $("#lowTempTS").val('');
      $("#lowHumVal").val('');
      $("#lowHumTS").val('');
      $("div#value_details").hide();

    });
    
    $("#plot").click(function(evt) {
      if(confirm("This will open a PopUp")){
        window.location = "http://10.0.0.215:8888/graph.jpg"
      }
    });

    $("#clear").click(function(evt) {
      $("#curTempVal").val('');
      $("#curTempTS").val('');
      $("#curHumVal").val('');
      $("#curHumTS").val('');
      $("#avgTempVal").val('');
      $("#avgTempTS").val('');
      $("#avgHumVal").val('');
      $("#avgHumTS").val('');
      $("#highTempVal").val('');
      $("#highTempTS").val('');
      $("#highHumVal").val('');
      $("#highHumTS").val('');
      $("#lowTempVal").val('');
      $("#lowTempTS").val('');
      $("#lowHumVal").val('');
      $("#lowHumTS").val('');
    });

  });
