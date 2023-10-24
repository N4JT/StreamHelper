document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var rememberLogin = document.getElementById("RememberLogin").checked;
   
    eel.login(username, password,rememberLogin)(function (response) {
        if (response === "success") {
            
            document.getElementById("message").textContent = "successfully logged in";
            window.location.href="dashboard.html";
        }
         else {
            document.getElementById("message").textContent = "Login failed. Please try again.";
        }
    });
});

eel.javascriptPreLogin()(function (response) {
    if (response === "success") {
        document.getElementById("message").textContent = "successfully logged in";
        window.location.href="dashboard.html";
    } 
    else if(response === "NotAutoLogin"){
            
    }
    else {
        document.getElementById("message").textContent = "Login failed. Please try again.";
    }
});
