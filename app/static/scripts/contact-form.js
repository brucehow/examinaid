$(document).ready(() => {
  console.log("Form ready!");

  const scriptURL = 'https://script.google.com/macros/s/AKfycbzBHOF2hcp7c2cWBWc8r2QoeCMHU6HGvN3pCFBlFG0UiPzwdP4/exec'
  const form = document.forms['submit-to-google-sheet']

  form.addEventListener('submit', target => {
    target.preventDefault();
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
      .then(response => console.log('Success!', response))
      .catch(error => console.error('Error!', error.message));
  });

});