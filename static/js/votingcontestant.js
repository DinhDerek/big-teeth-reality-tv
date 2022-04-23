$(document).ready(function(){
    var count_voting = 1;
    $("#add_votes").on("click", function(){
        count_voting += 1;
        if (count_voting > 1) {
            $("<div/>").attr({class: "line"}).appendTo("#votes");
        }
        $("<input/>").attr({ type: "text", name: "city_"+count_voting}).appendTo("#votes").wrap($("<p>Enter the city for voting entry #"+count_voting+"</p>"));
        $("<input/>").attr({ type: "text", name: "state_"+count_voting}).appendTo("#votes").wrap($("<p>Enter the state for voting entry "+count_voting+"</p>"));
        $("<input/>").attr({ type: "text", name: "country_"+count_voting}).appendTo("#votes").wrap($("<p>Enter the country for voting entry "+count_voting+"</p>"));
        $("<input/>").attr({ type: "text", name: "method_"+count_voting}).appendTo("#votes").wrap($("<p>Enter the method of voting for voting entry #"+count_voting+"</p>"));
        $("<input/>").attr({ type: "number", name: "total_"+count_voting}).appendTo("#votes").wrap($("<p>Enter the total number of votes for voting entry #"+count_voting+"</p>"));
    });
})

function confirmationDialogue(){
    alert("Contestant votes recorded for episode " + episode_id + "!");
}