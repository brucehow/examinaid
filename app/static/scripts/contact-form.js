$(document).ready(() => {
  console.log("Form ready!");

  $("#contact-form-response").hide();

  const scriptURL = 'https://script.google.com/macros/s/AKfycbzBHOF2hcp7c2cWBWc8r2QoeCMHU6HGvN3pCFBlFG0UiPzwdP4/exec'
  const form = document.forms['contact-to-google-sheets']

  $(".contact-form-submit-button").click(target => {
    target.preventDefault();
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
      .then(response => {
        console.log('Success!', response);
        document.getElementById("google-sheets-form").reset();
        $("#contact-form-response").fadeToggle(500);
        setTimeout(() => {
          $("#contact-form-response").fadeToggle(500);
        }, 5000)
      })
      .catch(error => {
        console.error('Error!', error.message);
      });
  });
});