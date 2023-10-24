

function LogOut(){
    eel.logout_user()(function (response){
        if (response === "success"){
            window.location.href = "index.html";
            document.getElementById("message").textContent = "LOG OUT SUCCESSFULL";
        }
        else{
            document.getElementById("message").textContent = "SOMETHING WENT WRONG";
        }
    });
}