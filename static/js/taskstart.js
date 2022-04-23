$(document).ready(function(){
    var count_contestant = 1;
    $("#add_contestant").on("click", function(){
        count_contestant += 1;
        if (count_contestant > 1) {
            $("<div/>").attr({class: "line"}).appendTo("#contestants");
        }
        $("<input/>").attr({ type: "number", name: "contestant_"+count_contestant}).appendTo("#contestants").wrap($("<p>Enter ID of contestant # "+count_contestant+"<p/>"));
        $("<input/>").attr({ type: "text", name: "result_"+count_contestant}).appendTo("#contestants").wrap($("<p>Enter result of contestant # "+count_contestant+"<p/>"));
        $("<input/>").attr({ type: "number", name: "points_"+count_contestant, min: "0", max: "100"}).appendTo("#contestants").wrap($("<p>Enter points earned by contestant #"+count_contestant+"<p/>"));
    });
})

function confirmationDialogue(){
    alert("Task recorded for event " + event_id + "!");
}