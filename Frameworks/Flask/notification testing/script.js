
  // Get the target date (replace this with your target date)
  var targetDate = new Date("2023-09-22T00:00:00Z");

  // Function to check if the target date has been reached
  function checkTargetDate() {
    var currentDate = new Date();
    
    if (currentDate >= targetDate) {
      // If the target date has been reached, disable the button
      document.getElementById("myButton").disabled = true;
    }
  }

  // Call the function to check the target date when the page loads
  window.onload = function() {
    checkTargetDate();
  };