$(document).ready(function(){
    console.log("test")
    displayError();
})

function displayError() {
    if (deleted == false) {
        alert("Contestant with ID " + app_id + " not found, please try again!");
        window.location.href = "delete-get-app-id";
    } else {
        alert("Contestant with ID " + app_id + " deleted from the database!");
        window.location.href = "/";
    }
}