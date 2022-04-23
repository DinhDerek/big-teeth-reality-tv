$(document).ready(function(){
    var count_record = 0;
    $("#add_record").on("click", function(){
        count_record += 1;
        if (count_record > 1) {
            $("<div/>").attr({class: "line"}).appendTo("#records");
        }
        $("<input/>").attr({ type: "date", name: "date_"+count_record}).appendTo("#records").wrap($("<p>Enter date of record #"+count_record+"<p/>"));
        $("<input/>").attr({ type: "text", name: "category_"+count_record}).appendTo("#records").wrap($("<p>Enter category of record #"+count_record+"<p/>"));
        $("<input/>").attr({ type: "text", name: "desc_"+count_record}).appendTo("#records").wrap($("<p>Enter description of record #"+count_record+"<p/>"));
        $("<input/>").attr({ type: "text", name: "outcome_"+count_record}).appendTo("#records").wrap($("<p>Enter outcome of record #"+count_record+"<p/>"));
    });
})

function confirmationDialogue(){
    alert("Background check recorded for contestant " + app_id + "!");
}