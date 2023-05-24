// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
    var timerElement = document.querySelector('.timer');
    var timeLeft = 30;
  
    // Function to update the timer display
    function updateTimer() {
      timerElement.textContent = timeLeft;
  
      if (timeLeft === 0) {
        // Timer finished, click the next button
        clearInterval(timerInterval);
        var nextButton = document.getElementById('next');
        nextButton.click();
      } else {
        timeLeft--;
      }
    }
  
    // Call the updateTimer function initially
    updateTimer();
  
    // Set up an interval to update the timer every second
    var timerInterval = setInterval(updateTimer, 1000);
  });
  