$(document).ready(() => {
  console.log("Form ready!");

  $("#contact-form-response").hide();
  $("#contact-form-name-error").hide();
  $("#contact-form-email-error").hide();
  $("#contact-form-message-error").hide();
  $("#contact-form-error").hide();

  const scriptURL = 'https://script.google.com/macros/s/AKfycbzBHOF2hcp7c2cWBWc8r2QoeCMHU6HGvN3pCFBlFG0UiPzwdP4/exec'
  const form = document.forms['contact-to-google-sheets']

  $(".contact-form-submit-button").click(target => {
    target.preventDefault();

    var errors = false;

    // Name field required testing
    var name = $("#contact_name").val();
    if (name == '') {
      $("#contact-form-name-error").fadeToggle(500);
        setTimeout(() => {
          $("#contact-form-name-error").fadeToggle(500);
        }, 5000);
      errors = true
    }

    // Email regex testing - this field is not required but if it is used, check that the email is formatted properly
    var emailRegex = /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/
    var email = $("#contact_email").val();
    if (email != '' && !emailRegex.test(email)) {
      $("#contact-form-email-error").fadeToggle(500);
        setTimeout(() => {
          $("#contact-form-email-error").fadeToggle(500);
        }, 5000);
      errors = true;
    }

    // Message field required testing
    var message = $("#contact_message").val();
    if (message == '') {
      $("#contact-form-message-error").fadeToggle(500);
        setTimeout(() => {
          $("#contact-form-message-error").fadeToggle(500);
        }, 5000);
      errors = true
    }

    if (!errors) {
      fetch(scriptURL, { method: 'POST', body: new FormData(form)})
      .then(response => {
        console.log('Success!', response);
        document.getElementById("google-sheets-form").reset();
        $("#contact-form-response").fadeToggle(500);
        setTimeout(() => {
          $("#contact-form-response").fadeToggle(500);
        }, 5000);
      })
      .catch(error => {
        console.error('Error!', error.message);
        document.getElementById("google-sheets-form").reset();
        $("#contact-form-error").fadeToggle(500);
        setTimeout(() => {
          $("#contact-form-error").fadeToggle(500);
        }, 5000)
      });
    }
  });
});