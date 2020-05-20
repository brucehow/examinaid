$(document).ready(() => {
  console.log("The main index.js file is ready!");
  // All code must go within the ready callback.

  // Console spam REEEEE
  /*
  $(document).mousemove((target) => {
    console.log("Mouse moved over (" + target.pageX + ", " + target.pageY + ").");
  });
  */

  // Originally preventing form submit
  /*
  $("#unit-test-form").submit(target => {
    console.log("Test submitted!")
    target.preventDefault();
    console.log($("#unit-test-form").serialize());
  });
  */

  $("#test-file-upload").on("change", () => {
    if ($("#test-file-upload").get(0).files.length === 0) console.log("No files!");
    else {
      var filename = document.getElementById("test-file-upload").value.split("\\");
      console.log(filename);
      document.getElementById("name-of-file").innerHTML = filename[filename.length - 1];
    }
  });
  
});