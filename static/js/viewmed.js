$(document).ready(function(){
    displayError();
})

function displayError() {
    if (med_info.found == "false") {
        alert("Contestant with ID " + med_info.app_id + " not found, please try again!");
        window.location.href = "view-med-info";
    } else {
        alert("Contestant with ID " + med_info.app_id + "'s medication information retrieved!");
        window.location.href = "view-med-info-results";
    }
}