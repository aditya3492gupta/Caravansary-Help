function myFunction() {
    var x = document.getElementById("inputpassword");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }