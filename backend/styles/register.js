document.getElementById("register-form").addEventListener("submit", function (event) {
    event.preventDefault();
    let email = document.getElementById("email").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let repeat_password=document.getElementById("repeat-password0").value;
    let rememberLogin = document.getElementById("RememberLogin").checked;
    eel.register_user(username, password,email)(function (response) {
        if (response === "success") {
            
            document.getElementById("message").textContent = "successfully logged in";
            window.location.href="dashboard.html";
        } else {
            document.getElementById("message").textContent = "Login failed. Please try again.";
        }
    });
});

