$(document).ready(function(){
    var count_job = 0;
    $("#add_job").on("click", function(){
        count_job += 1;
        if (count_job > 1) {
            $("<div/>").attr({class: "line"}).appendTo("#jobs");
        }
        $("<input/>").attr({ type: "text", name: "job_"+count_job}).appendTo("#jobs").wrap($("<p>Enter job #" + count_job + "'s name<p/>"));
        $("<input/>").attr({ type: "date", name: "start_"+count_job}).appendTo("#jobs").wrap($("<p>Enter start date for job #"+count_job+"<p/>"));
        $("<input/>").attr({ type: "date", name: "end_"+count_job}).appendTo("#jobs").wrap($("<p>Enter end date for job #"+count_job+"<p/>"));
        $("<input/>").attr({ type: "text", name: "desc_"+count_job}).appendTo("#jobs").wrap($("<p>Enter job description for job #"+count_job+"<p/>"));
    });
})

function confirmationDialogue(){
    alert("Application recorded for contestant " + app_id + "!");
}