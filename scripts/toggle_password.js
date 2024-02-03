

function togglePasswordVisibility() {
    
    var button = document.getElementById("show-hide-pass");

    if (button.innerHTML === "Show") button.innerHTML = "Hide";
    else button.innerHTML = "Show";

    var passwordInput = document.getElementById("passwordInput");
    var icon = document.querySelector('.toggle-password');

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-lock");
        icon.classList.add("fa-unlock");
    } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-unlock");
        icon.classList.add("fa-lock");
    }
}