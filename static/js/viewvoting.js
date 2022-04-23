$(document).ready(function(){
    displayError();
})

function displayError() {
    if (voting_info.found == "episode") {
        alert("Episode with title " + voting_info.episode_title + " and air date " + voting_info.air_date + " not found, please try again!");
        window.location.href = "view-voting-info";
    } else if (voting_info.found == "contestant") {
        alert("Contestant with ID " + voting_info.app_id + " not found, please try again!");
        window.location.href = "view-voting-info";
    } else {
        alert("Episode with title " + voting_info.episode_title + " and air date " + voting_info.air_date + " retrieved!");
        window.location.href = "view-voting-info-results";
    }
}