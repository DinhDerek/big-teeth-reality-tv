$(document).ready(function(){
    $("<h1>\""+episode_info.episode_title+"\" Episode Information</h1>").appendTo("#header");
    $("<h2>General Information</h2>").appendTo("#general");
    $("<p>Title: "+episode_info.episode_title+"</p>").appendTo("#general");
    $("<p>Air Date: "+episode_info.air_date+"</p>").appendTo("#general");
    $("<p>Producer: "+episode_info.producer+"</p>").appendTo("#general");
    $("<p>Director: "+episode_info.director+"</p>").appendTo("#general");
    $("<div/>").attr({class: "line"}).appendTo("#general");
    $("<h2>Episode Actions</h2>").appendTo("#actions");
    for (let action_count = 0; action_count < episode_info.episode_actions.length; action_count++) {
        let action = episode_info.episode_actions[action_count];
        $("<div/>").attr({id: "seq_" + action_count}).appendTo("#actions");
        $("<h3>Sequence #" +action.seq+"</h3>").appendTo("#seq_" + action_count);
        $("<p>Description: "+action.desc+"</p>").appendTo("#seq_" + action_count);
        $("<p>Cameras required: "+action.cameras+"</p>").appendTo("#seq_" + action_count);
        $("<p>Estimated time: "+action.estimated_time+" minutes</p>").appendTo("#seq_" + action_count);
    }
    $("<div/>").attr({class: "line"}).appendTo("#actions");
    $("<h2>Events</h2>").appendTo("#events");
    for (let event_count = 0; event_count < episode_info.episode_events.length; event_count++) {
        let event = episode_info.episode_events[event_count];
        $("<div/>").attr({id: "event_" + event_count}).appendTo("#events");
        if (event_count > 0) {
            $("<div/>").attr({class: "event_line"}).appendTo("#event_" + event_count);
        }
        $("<h3>Event #"+(event_count+1)+": "+event.title+"</h3>").appendTo("#event_" + event_count);
        $("<p>Description: "+event.description+"</p>").appendTo("#event_" + event_count);
        $("<p>Estimated time: "+event.estimated_time+" minutes</p>").appendTo("#event_" + event_count);
        $("<p>Estimated danger: "+event.estimated_danger+"/10</p>").appendTo("#event_" + event_count);

        for (let task_count = 0; task_count < event.tasks.length; task_count++) {
            let task = event.tasks[task_count];
            $("<div/>").attr({id: "event_"+event_count+"task_"+task_count}).appendTo("#event_" + event_count);
            $("<h4>Task #"+(task_count+1)+": "+task.name+"</h4>").appendTo("#event_"+event_count+"task_"+task_count);
            $("<p>Prize: "+task.prize+" minutes</p>").appendTo("#event_"+event_count+"task_"+task_count);

            for (let contestant_count = 0; contestant_count < task.contestants.length; contestant_count++) {
                let contestant = task.contestants[contestant_count];
                $("<div/>").attr({id: "event_"+event_count+"task_"+task_count+"contestant_"+contestant_count}).appendTo("#event_"+event_count+"task_"+task_count);
                $("<h5>Contestant #"+(contestant_count+1)+": "+contestant.name+"</h4>").appendTo("#event_"+event_count+"task_"+task_count+"contestant_"+contestant_count);
                $("<p>Result: "+contestant.result+"</p>").appendTo("#event_"+event_count+"task_"+task_count+"contestant_"+contestant_count);
                $("<p>Points earned: "+contestant.points+"</p>").appendTo("#event_"+event_count+"task_"+task_count+"contestant_"+contestant_count);
            }
        }
    }
})