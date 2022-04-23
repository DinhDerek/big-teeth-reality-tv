$(document).ready(function(){
    $("<h1>Contestant ID "+med_info.app_id+" Medication Information</h1>").appendTo("#header");
    $("<h2>General Information</h2>").appendTo("#general");
    $("<p>Name: "+med_info.name+"</p>").appendTo("#general");
    $("<p>Date of birth: "+med_info.dob+"</p>").appendTo("#general");
    $("<p>Gender: "+med_info.gender+"</p>").appendTo("#general");
    $("<div/>").attr({class: "line"}).appendTo("#general");
    $("<h2>Medication</h2>").appendTo("#medication");
    for (let med_count = 0; med_count < med_info.medication.length; med_count++) {
        let med = med_info.medication[med_count];
        $("<div/>").attr({id: "med_" + med_count}).appendTo("#medication");
        if (med_count > 0) {
            $("<div/>").attr({class: "event_line"}).appendTo("#med_" + med_count);
        }
        $("<h3>Medication #" +(med_count+1)+"</h3>").appendTo("#med_" + med_count);
        $("<p>Medication name: "+med.medication_name+"</p>").appendTo("#med_" + med_count);
        $("<p>Reason for medication: "+med.reason+"</p>").appendTo("#med_" + med_count);
    }
})