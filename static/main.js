addEventListener("DOMContentLoaded", function() {
  // Grab all of the elements with a class of command
  var commandButtons = document.querySelectorAll(".command");
  for (var i=0, l=commandButtons.length; i<l; i++) {
    var button = commandButtons[i];
    // For each button, listen for the "click" event
    button.addEventListener("click", function(e) {
      e.preventDefault();
      var clickedButton = e.target;
      var command = clickedButton.value;
      var request = new XMLHttpRequest();
      request.onload = function() {
          <!--alert(request.responseText);-->
      };
      // We point the request at the appropriate command
      request.open("GET", "/cmd/" + command, true);
      // and then we send it off
      request.send();
    });
  }
  document.getElementById("msg-submit").addEventListener("click", function(e) {
    e.preventDefault();
    msgTextarea = document.getElementById("msg")
    msg = msgTextarea.value
    msgTextarea.value = ""
    var request = new XMLHttpRequest();
    request.open("GET", "/cmd/talk" + "?msg=" + msg, true);
    request.send();
  })
}, true);