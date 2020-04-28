$(document).ready(() => {
  console.log("The DOM is ready!");
  // All code must go within the ready callback.

  $("#example-test-form").submit(target => {
    target.preventDefault();
    console.log($("#example-test-form").serialize());
  });

});