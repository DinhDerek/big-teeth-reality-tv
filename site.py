import mysql.connector as mysql
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from dbtool import DBTool


db = mysql.connect(host="localhost", user="root", password="", database="big_teeth_reality_tv")
cursor = db.cursor(buffered=True)
db_tool = DBTool(db.cursor(buffered=True))
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        if "appform" in request.form:
            return redirect(url_for('appgeneral'))
        elif "backgroundform" in request.form:
            return redirect(url_for('backgroundbasic'))
        elif "episodeform" in request.form:
            return redirect(url_for('episodeinformation'))
        elif "votingform" in request.form:
            return redirect(url_for('votingstart'))
        elif "viewepform" in request.form:
            return redirect(url_for('viewepinfo'))
        elif "viewmedform" in request.form:
            return redirect(url_for('viewmedinfo'))
        elif "viewjobform" in request.form:
            job_info = db_tool.view_job()
            if len(job_info) == 0:
                return redirect(url_for('viewjobinfosecondary'))
            else:
                session["job_info"] = job_info
                return redirect(url_for('viewjobinforesults'))
        elif "viewvoteform" in request.form:
            return redirect(url_for('viewvotinginfo'))
        elif "deleteappform" in request.form:
            return redirect(url_for('deletegetappid'))
    else:
        return render_template("index.html")

@app.route('/application-form-general', methods =["GET", "POST"])
def appgeneral():
    if request.method == "POST":
        if "submit" in request.form:
            session["app_id"] = db_tool.insert_application(request.form)
            return redirect(url_for('appmedical'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("appgeneral.html")

@app.route('/application-form-medical', methods =["GET", "POST"])
def appmedical():
    if request.method == "POST":
        db_tool.insert_medication(session["app_id"], request.form)
        return redirect(url_for('appjobs'))
    else:
        return render_template("appmedical.html")

@app.route('/application-form-jobs', methods =["GET", "POST"])
def appjobs():
    if request.method == "POST":
        db_tool.insert_job(session["app_id"], request.form)
        db.commit()
        return redirect(url_for('home'))
    else:
        return render_template("appjobs.html", data={"app_id": session["app_id"]})

@app.route('/background-form-basic', methods =["GET", "POST"])
def backgroundbasic():
    if request.method == "POST":
        if "submit" in request.form:
            session["app_id"] = request.form["app_id"]
            db_tool.insert_background(request.form)
            return redirect(url_for('backgroundemployer'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("backgroundbasic.html")

@app.route('/background-form-employer', methods =["GET", "POST"])
def backgroundemployer():
    if request.method == "POST":
        db_tool.insert_employer(session["app_id"], request.form)
        return redirect(url_for('backgroundeducation'))
    else:
        return render_template("backgroundemployer.html")

@app.route('/background-form-education', methods =["GET", "POST"])
def backgroundeducation():
    if request.method == "POST":
        db_tool.insert_education(session["app_id"], request.form)
        return redirect(url_for('backgroundrecords'))
    else:
        return render_template("backgroundeducation.html")

@app.route('/background-form-records', methods =["GET", "POST"])
def backgroundrecords():
    if request.method == "POST":
        db_tool.insert_record(session["app_id"], request.form)
        db.commit()
        return redirect(url_for('home'))
    else:
        return render_template("backgroundrecords.html", data={"app_id": session["app_id"]})

@app.route('/episode-information', methods =["GET", "POST"])
def episodeinformation():
    if request.method == "POST":
        if "submit" in request.form:
            session["episode_id"] = db_tool.insert_episode(request.form)
            return redirect(url_for('episodeactions'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("episodeinformation.html")

@app.route('/episode-actions', methods =["GET", "POST"])
def episodeactions():
    if request.method == "POST":
        db_tool.insert_action(session["episode_id"], request.form)
        return redirect(url_for('eventstart'))
    else:
        return render_template("episodeaction.html")

@app.route('/event-start', methods =["GET", "POST"])
def eventstart():
    if request.method == "POST":
        session["event_id"] = db_tool.insert_event(session["episode_id"], request.form)
        return redirect(url_for('taskstart'))
    else:
        return render_template("eventstart.html")

@app.route('/task-start', methods =["GET", "POST"])
def taskstart():
    if request.method == "POST":
        db_tool.insert_task(session["event_id"], request.form)
        return redirect(url_for('taskmainpage'))
    else:
        return render_template("taskstart.html", data={"event_id": session["event_id"]})

@app.route('/task-main-page', methods =["GET", "POST"])
def taskmainpage():
    if request.method == "POST":
        if "taskform" in request.form:
            return redirect(url_for('taskstart'))
        elif "backtoeventform" in request.form:
            return redirect(url_for('eventmainpage'))
    else:
        return render_template("taskmain.html")

@app.route('/event-main-page', methods =["GET", "POST"])
def eventmainpage():
    if request.method == "POST":
        if "eventform" in request.form:
            return redirect(url_for('eventcontinue'))
        elif "finishform" in request.form:
            db.commit()
            return redirect(url_for('home'))
    else:
        return render_template("eventmain.html", data={"episode_id": session["episode_id"]})

@app.route('/event-continue', methods =["GET", "POST"])
def eventcontinue():
    if request.method == "POST":
        session["event_id"] = db_tool.insert_event(session["episode_id"], request.form)
        return redirect(url_for('taskstart'))
    else:
        return render_template("eventcontinue.html")

@app.route('/voting-start', methods =["GET", "POST"])
def votingstart():
    if request.method == "POST":
        if "submit" in request.form:
            session["voting_id"] = db_tool.insert_voting(request.form)
            return redirect(url_for('votingcontestant'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("votingstart.html")

@app.route('/voting-contestant', methods =["GET", "POST"])
def votingcontestant():
    if request.method == "POST":
        db_tool.insert_votingcontestant(session["voting_id"], request.form)
        return redirect(url_for('votingmainpage'))
    else:
        return render_template("votingcontestant.html", data={"episode_id": session["episode_id"]})

@app.route('/voting-main-page', methods =["GET", "POST"])
def votingmainpage():
    if request.method == "POST":
        if "votingform" in request.form:
            return redirect(url_for('votingcontestant'))
        elif "finishform" in request.form:
            db.commit()
            return redirect(url_for('home'))
    else:
        return render_template("votingmain.html", data={"episode_id": session["episode_id"]})

@app.route('/delete-get-app-id', methods =["GET", "POST"])
def deletegetappid():
    if request.method == "POST":
        if "submit" in request.form:
            session["delete_app_result"] = db_tool.delete_applicant(request.form["app_id"])
            session["app_id"] = request.form["app_id"]
            db.commit()
            return redirect(url_for('deletegetappidsecondary'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("deletegetappid.html")

@app.route('/delete-get-app-id-secondary', methods =["GET", "POST"])
def deletegetappidsecondary():
    return render_template("deletegetappidsecondary.html", data={"deleted": session["delete_app_result"], "app_id": session["app_id"]})

@app.route('/view-ep-info', methods =["GET", "POST"])
def viewepinfo():
    if request.method == "POST":
        if "submit" in request.form:
            session["episode_info"] = db_tool.view_episode(request.form)
            return redirect(url_for('viewepinfosecondary'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("viewepinfo.html")

@app.route('/view-ep-info-secondary', methods =["GET", "POST"])
def viewepinfosecondary():
    return render_template("viewepinfosecondary.html", data=session["episode_info"])

@app.route('/view-ep-info-results', methods =["GET", "POST"])
def viewepinforesults():
    if request.method == "POST":
        if "back" in request.form:
            return redirect(url_for('viewepinfo'))
    else:
        return render_template("viewepinforesults.html", data=session["episode_info"])

@app.route('/view-med-info', methods =["GET", "POST"])
def viewmedinfo():
    if request.method == "POST":
        if "submit" in request.form:
            session["med_info"] = db_tool.view_med(request.form["app_id"])
            return redirect(url_for('viewmedinfosecondary'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("viewmedinfo.html")

@app.route('/view-med-info-secondary', methods =["GET", "POST"])
def viewmedinfosecondary():
    return render_template("viewmedinfosecondary.html", data=session["med_info"])

@app.route('/view-med-info-results', methods =["GET", "POST"])
def viewmedinforesults():
    if request.method == "POST":
        if "back" in request.form:
            return redirect(url_for('viewmedinfo'))
    else:
        return render_template("viewmedinforesults.html", data=session["med_info"])

@app.route('/view-job-info-secondary', methods =["GET", "POST"])
def viewjobinfosecondary():
    return render_template("viewjobinfosecondary.html")

@app.route('/view-job-info-results', methods =["GET", "POST"])
def viewjobinforesults():
    if request.method == "POST":
        if "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("viewjobinforesults.html", data=session["job_info"])

@app.route('/view-voting-info', methods =["GET", "POST"])
def viewvotinginfo():
    if request.method == "POST":
        if "submit" in request.form:
            session["voting_info"] = db_tool.view_voting(request.form)
            return redirect(url_for('viewvotinginfosecondary'))
        elif "back" in request.form:
            return redirect(url_for('home'))
    else:
        return render_template("viewvotinginfo.html")

@app.route('/view-voting-info-secondary', methods =["GET", "POST"])
def viewvotinginfosecondary():
    return render_template("viewvotinginfosecondary.html", data=session["voting_info"])

@app.route('/view-voting-info-results', methods =["GET", "POST"])
def viewvotinginforesults():
    if request.method == "POST":
        if "back" in request.form:
            return redirect(url_for('viewvotinginfo'))
    else:
        return render_template("viewvotinginforesults.html", data=session["voting_info"])

if __name__ == "__main__":
    app.run()
