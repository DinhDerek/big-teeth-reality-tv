$(document).ready(function(){
    displayError();
})

function displayError() {
    if (episode_info.found == "false") {
        alert("Episode with title " + episode_info.episode_title + " and air date " + episode_info.air_date + " not found, please try again!");
        window.location.href = "view-ep-info";
    } else {
        alert("Episode with title " + episode_info.episode_title + " and air date " + episode_info.air_date + " retrieved!");
        window.location.href = "view-ep-info-results";
    }
}