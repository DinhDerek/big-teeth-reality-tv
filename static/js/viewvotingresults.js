$(document).ready(function(){
    $("<h1>"+voting_info.episode_title+", "+voting_info.air_date+"</h1>").appendTo("#header");
    $("<h2>Contestant ID "+voting_info.app_id+ ": "+voting_info.name+"</h2>").appendTo("#general");
    $("<p>Sum of votes: "+voting_info.votes+"</p>").appendTo("#general");
})