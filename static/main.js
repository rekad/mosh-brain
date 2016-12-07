// Only run what comes next *after* the page has loaded
addEventListener("DOMContentLoaded", function() {
  // Grab all of the elements with a class of command
  // (which all of the buttons we just created have)
  var commandButtons = document.querySelectorAll(".command");

  for (var i=0, l=commandButtons.length; i<l; i++) {
    var button = commandButtons[i];
    // For each button, listen for the "click" event
    button.addEventListener("click", function(e) {
      // When a click happens, stop the button
      // from submitting our form (if we have one)
      e.preventDefault();

      var clickedButton = e.target;
      var command = clickedButton.value;

      // Now we need to send the data to our server
      // without reloading the page - this is the domain of
      // AJAX (Asynchronous JavaScript And XML)
      // We will create a new request object
      // and set up a handler for the response
      var request = new XMLHttpRequest();
      request.onload = function() {
          // We could do more interesting things with the response
          // or, we could ignore it entirely

          <!--alert(request.responseText);-->
      };
      // We point the request at the appropriate command
      request.open("GET", "/" + command, true);
      // and then we send it off
      request.send();
    });
  }
  document.getElementById("msg-submit").addEventListener("click", function(e) {
  e.preventDefault();
  msg = document.getElementById("msg").value
  var request = new XMLHttpRequest();
  request.onload = function() {
        // We could do more interesting things with the response
        // or, we could ignore it entirely

        <!--alert(request.responseText);-->
    };
    // We point the request at the appropriate command
    request.open("GET", "/talk" + "?msg=" + msg, true);
    // and then we send it off
    request.send();
  })
}, true);