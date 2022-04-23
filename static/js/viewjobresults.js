$(document).ready(function(){
    console.log(job_info)
    for (let job_count = 0; job_count < job_info.length; job_count++) {
        let job = job_info[job_count];
        $("<p>"+job.job_title+"</p>").appendTo("#jobs");
    }
})