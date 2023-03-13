const body = document.querySelector("body"),
    modeToggle = body.querySelector(".mode-toggle");
sidebar = body.querySelector("nav");
sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark") {
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if (getStatus && getStatus === "close") {
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        localStorage.setItem("mode", "dark");
    } else {
        localStorage.setItem("mode", "light");
    }
});
// Get the button and the pop-up box elements
var popupButton = document.getElementById("popup-button");
var popupBox = document.getElementById("popup-box");
var closeButton = document.getElementById("close-button");

// Add an event listener to the button that shows the pop-up box
popupButton.addEventListener("click", function () {
    popupBox.style.display = "block";
});

// Add an event listener to the close button that hides the pop-up box
closeButton.addEventListener("click", function () {
    popupBox.style.display = "none";
});


sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if (sidebar.classList.contains("close")) {
        localStorage.setItem("status", "close");
    } else {
        localStorage.setItem("status", "open");
    }
});

