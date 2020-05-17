$(document).ready(() => {
  console.log("The DOM is ready!");
  // All code must go within the ready callback.

  $("#example-test-form").submit(target => {
    target.preventDefault();
    console.log($("#example-test-form").serialize());
  });
  
  $("#test-file-upload").on("change", () => {
    if ($("#test-file-upload").get(0).files.length === 0) console.log("No files!");
    else {
      var filename = document.getElementById("test-file-upload").value.split("\\");
      console.log(filename);
      document.getElementById("name-of-file").innerHTML = filename[filename.length - 1];
    }
  });
  
});