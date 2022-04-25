

import json


class DBTool:
    def __init__(self, cursor):
        self.cursor = cursor

    def insert_application(self, app_fields):
        self.cursor.execute("ALTER TABLE application AUTO_INCREMENT=1")
        formatted_app_fields = [app_fields["first_name"].upper(), 
                                app_fields["last_name"].upper(), 
                                app_fields["address"].upper(),    
                                app_fields["postal"].upper(),     
                                app_fields["city"].upper(),     
                                app_fields["state"].upper(),     
                                app_fields["country"].upper(),    
                                app_fields["daytime_phone"],     
                                app_fields["night_phone"],     
                                app_fields["email"].upper(),     
                                app_fields["dob"],    
                                app_fields["gender"].upper(), 
                                app_fields["photo"],  
                                app_fields["video_id"],  
                                app_fields["candidate_essay"],   
                                app_fields["producer_rating"],    
                                app_fields["director_rating"]]
        self.cursor.execute("INSERT INTO application (first_name, last_name, address, postal, city, state, country, daytime_phone, night_phone, email, dob, gender, photo, video_id, candidate_essay, producer_rating, director_rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", formatted_app_fields)
        return self.cursor.lastrowid

    def insert_medication(self, app_id, medication):
        self.cursor.execute("ALTER TABLE medication AUTO_INCREMENT=1")
        num_medication = len(medication) // 2
        if num_medication == 0:
            return 0
        else:
            for i in range(1, num_medication + 1):
                med_data = [medication["med_" + str(i)].upper(), medication["reason_" + str(i)]]
                
                self.cursor.execute("SELECT medication_id FROM medication WHERE medication_name = %s", [med_data[0]])
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("INSERT INTO medication (medication_name) VALUES (%s)", [med_data[0]])
                    med_id = self.cursor.lastrowid
                else:
                    med_id = result[0]
                self.cursor.execute("INSERT INTO applicant_medication (app_id, medication_id, reason) VALUES (%s, %s, %s)", [app_id, med_id, med_data[1]])

    def insert_job(self, app_id, jobs):
        self.cursor.execute("ALTER TABLE jobs AUTO_INCREMENT=1")
        num_jobs = len(jobs) // 4
        if num_jobs == 0:
            return 0
        else:
            for i in range(1, num_jobs + 1):
                job_data = [jobs["job_" + str(i)].upper(), jobs["start_" + str(i)], jobs["end_" + str(i)], jobs["desc_" + str(i)]]
                
                self.cursor.execute("SELECT job_id FROM jobs WHERE job_title = %s", [job_data[0]])
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("INSERT INTO jobs (job_title) VALUES (%s)", [job_data[0]])
                    job_id = self.cursor.lastrowid
                else:
                    job_id = result[0]
                self.cursor.execute("INSERT INTO applicant_jobs (app_id, job_id, start_date, end_date, description) VALUES (%s, %s, %s, %s, %s)", [app_id, job_id, job_data[1], job_data[2], job_data[3]])

    def insert_background(self, background_fields):
        self.cursor.execute("ALTER TABLE background_check AUTO_INCREMENT=1")
        formatted_background_fields = [background_fields["app_id"], 
                                        background_fields["national_id"], 
                                        background_fields["religion"].upper(),    
                                        background_fields["appearance_rating"],     
                                        background_fields["strength_rating"]]    
        self.cursor.execute("INSERT INTO background_check (app_id, national_id, religion, appearance_rating, strength_rating) VALUES (%s, %s, %s, %s, %s)", formatted_background_fields)
        return self.cursor.lastrowid

    def insert_employer(self, app_id, emps):
        self.cursor.execute("ALTER TABLE employer AUTO_INCREMENT=1")
        num_emps = len(emps) // 3
        if num_emps == 0:
            return 0
        else:
            for i in range(1, num_emps + 1):
                emp_data = [emps["emp_" + str(i)].upper(), emps["phone_" + str(i)], emps["comments_" + str(i)]]
                
                self.cursor.execute("SELECT employer_id FROM employer WHERE employer_name = %s", [emp_data[0]])
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("INSERT INTO employer (employer_name, phone) VALUES (%s, %s)", [emp_data[0], emp_data[1]])
                    employer_id = self.cursor.lastrowid
                else:
                    employer_id = result[0]
                self.cursor.execute("INSERT INTO applicant_employer (app_id, employer_id, comments) VALUES (%s, %s, %s)", [app_id, employer_id, emp_data[2]])

    def insert_education(self, app_id, edu):
        self.cursor.execute("ALTER TABLE education AUTO_INCREMENT=1")
        num_edu = len(edu) // 4
        if num_edu == 0:
            return 0
        else:
            for i in range(1, num_edu + 1):
                edu_data = [edu["edu_" + str(i)].upper(), edu["phone_" + str(i)], edu["degree_" + str(i)].upper(), edu["comments_" + str(i)]]
                
                self.cursor.execute("SELECT education_id FROM education WHERE education_name = %s", [edu_data[0]])
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("INSERT INTO education (education_name, phone) VALUES (%s, %s)", [edu_data[0], edu_data[1]])
                    education_id = self.cursor.lastrowid
                else:
                    education_id = result[0]
                self.cursor.execute("INSERT INTO applicant_education (app_id, education_id, degree, comments) VALUES (%s, %s, %s, %s)", [app_id, education_id, edu_data[2], edu_data[3]])

    def insert_record(self, app_id, records):
        self.cursor.execute("ALTER TABLE poljud AUTO_INCREMENT=1")
        num_records = len(records) // 4
        if num_records == 0:
            return 0
        else:
            for i in range(1, num_records + 1):
                record_data = [records["date_" + str(i)], records["category_" + str(i)].upper(), records["desc_" + str(i)].upper(), records["outcome_" + str(i)].upper()]
                
                self.cursor.execute("SELECT poljud_id FROM poljud WHERE category = %s", [record_data[1]])
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("INSERT INTO poljud (category) VALUES (%s)", [record_data[1]])
                    record_id = self.cursor.lastrowid
                else:
                    record_id = result[0]
                self.cursor.execute("INSERT INTO applicant_records (app_id, poljud_id, description, outcome) VALUES (%s, %s, %s, %s)", [app_id, record_id, record_data[2], record_data[3]])

    def insert_episode(self, episode):
        self.cursor.execute("ALTER TABLE episode AUTO_INCREMENT=1")
        formatted_ep_fields = [episode["episode_title"].upper(), 
                                episode["air_date"], 
                                episode["producer"].upper(),    
                                episode["director"].upper()]
        self.cursor.execute("INSERT INTO episode (title, air_date, producer, director) VALUES (%s, %s, %s, %s)", formatted_ep_fields)
        return self.cursor.lastrowid

    def insert_action(self, episode_id, actions):
        self.cursor.execute("ALTER TABLE episode_actions AUTO_INCREMENT=1")
        num_actions = len(actions) // 4
        if num_actions == 0:
            return 0
        else:
            for i in range(1, num_actions + 1):
                action_data = [actions["seq_" + str(i)], actions["desc_" + str(i)].upper(), actions["cameras_" + str(i)], actions["est_" + str(i)]]
                
                self.cursor.execute("SELECT action_id FROM episode_actions WHERE seq = %s", [action_data[0]])
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("INSERT INTO episode_actions (episode_id, seq, description, cameras, estimated_time) VALUES (%s, %s, %s, %s, %s)", [episode_id, action_data[0], action_data[1], action_data[2], action_data[3]])
                    action_id = self.cursor.lastrowid
                else:
                    action_id = result[0]

    def insert_event(self, episode_id, event):
        self.cursor.execute("ALTER TABLE event AUTO_INCREMENT=1")
        formatted_event_fields = [episode_id,
                                event["event_title"].upper(), 
                                event["desc"], 
                                event["est"].upper(),    
                                event["danger"].upper()]
        self.cursor.execute("INSERT INTO event (episode_id, title, description, estimated_time, estimated_danger) VALUES (%s, %s, %s, %s, %s)", formatted_event_fields)
        return self.cursor.lastrowid

    def insert_task(self, event_id, task):
        self.cursor.execute("ALTER TABLE event_tasks AUTO_INCREMENT=1")
        self.cursor.execute("ALTER TABLE task_contestants AUTO_INCREMENT=1")

        task_data = [event_id, task["task_name"].upper(), task["prize"].upper()]
        self.cursor.execute("INSERT INTO event_tasks (event_id, name, prize) VALUES (%s, %s, %s)", task_data)
        task_id = self.cursor.lastrowid

        num_contestants = (len(task) - 2) // 3
        if num_contestants == 0:
            return 0
        else:
            for i in range(1, num_contestants + 1):
                contestant_data = [task_id, task["contestant_" + str(i)], task["result_" + str(i)].upper(), task["points_" + str(i)]]
                self.cursor.execute("INSERT INTO task_contestants (task_id, app_id, result, points) VALUES (%s, %s, %s, %s)", contestant_data)

    def insert_voting(self, episode_info):
        self.cursor.execute("ALTER TABLE voting AUTO_INCREMENT=1")
        voting_data = [episode_info["episode_title"], episode_info["air_date"]]
        self.cursor.execute("SELECT episode_id FROM episode WHERE title LIKE %s AND air_date = %s", voting_data)
        episode_id =  self.cursor.fetchone()[0]
        self.cursor.execute("SELECT voting_id FROM voting WHERE episode_id = %s", [episode_id])
        result = self.cursor.fetchone()
        if result == None:
            self.cursor.execute("INSERT INTO voting (episode_id) VALUES (%s)", [episode_id])
            return self.cursor.lastrowid
        else:
            return result[0]

    def insert_votingcontestant(self, voting_id, voting_info):
        self.cursor.execute("ALTER TABLE voting_contestants AUTO_INCREMENT=1")
        num_votes = (len(voting_info) - 1) // 5
        if num_votes == 0:
            return 0
        else:
            for i in range(1, num_votes + 1):
                region_data = [voting_info["city_" + str(i)].upper(), voting_info["state_" + str(i)].upper(), voting_info["country_" + str(i)].upper()]
                self.cursor.execute("SELECT region_id FROM region WHERE city LIKE %s AND state LIKE %s AND country LIKE %s", region_data)
                result = self.cursor.fetchone()
                if result == None:
                    self.cursor.execute("ALTER TABLE region AUTO_INCREMENT=1")
                    self.cursor.execute("INSERT INTO region (city, state, country) VALUES (%s, %s, %s)", region_data)
                    region_id = self.cursor.lastrowid
                else:
                    region_id = result[0]
                voting_contestant_data = [voting_id, voting_info["app_id"], region_id, voting_info["method_" + str(i)].upper(), voting_info["total_" + str(i)]]
                self.cursor.execute("INSERT INTO voting_contestants (voting_id, app_id, region_id, method, votes) VALUES (%s, %s, %s, %s, %s)", voting_contestant_data)

    def delete_applicant(self, app_id):
        self.cursor.execute("SELECT * FROM application where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result == None:
            return "false"
        else:
            self.delete_voting_contestant(app_id)
            self.delete_task_contestant(app_id)
            self.delete_background_contestant(app_id)
            self.delete_education_contestant(app_id)
            self.delete_employer_contestant(app_id)
            self.delete_job_contestant(app_id)
            self.delete_medication_contestant(app_id)
            self.delete_records_contestant(app_id)
            self.cursor.execute("DELETE FROM application where app_id = %s", [app_id])
            return "true"
    
    def delete_voting_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM voting_contestants where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM voting_contestants where app_id = %s", [app_id])

    def delete_task_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM task_contestants where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM task_contestants where app_id = %s", [app_id])
    
    def delete_background_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM background_check where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM background_check where app_id = %s", [app_id])
    
    def delete_education_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM applicant_education where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM applicant_education where app_id = %s", [app_id])
    
    def delete_medication_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM applicant_medication where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM applicant_medication where app_id = %s", [app_id])
    
    def delete_employer_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM applicant_employer where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM applicant_employer where app_id = %s", [app_id])
    
    def delete_job_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM applicant_jobs where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM applicant_jobs where app_id = %s", [app_id])
    
    def delete_records_contestant(self, app_id):
        self.cursor.execute("SELECT * FROM applicant_records where app_id = %s", [app_id])
        result = self.cursor.fetchone()
        if result != None:
            self.cursor.execute("DELETE FROM applicant_records where app_id = %s", [app_id])

    def view_episode(self, episode_info):
        return_dict = {"episode_title": episode_info["episode_title"].upper(), "air_date": episode_info["air_date"]}

        self.cursor.execute("SELECT episode_id, producer, director FROM episode WHERE title = %s AND air_date = %s", [episode_info["episode_title"].upper(), episode_info["air_date"]])
        result = self.cursor.fetchone()
        if result == None:
            return_dict["found"] = "false"
            return return_dict
        else:
            return_dict["producer"] = result[1]
            return_dict["director"] = result[2]
            return_dict["episode_actions"] = self.view_episode_actions(result[0])
            return_dict["episode_events"] = self.view_episode_events(result[0])
            return_dict["found"] = "true"
            return return_dict

    def view_episode_actions(self, episode_id):
        self.cursor.execute("SELECT seq, description, cameras, estimated_time FROM episode_actions WHERE episode_id = %s", [episode_id])
        result_list = []
        query_results = self.cursor.fetchall()
        for result in query_results:
            temp_dict = {}
            temp_dict["seq"] = result[0]
            temp_dict["desc"] = result[1]
            temp_dict["cameras"] = result[2]
            temp_dict["estimated_time"] = result[3]
            result_list.append(temp_dict)
        return result_list

    def view_episode_events(self, episode_id):
        self.cursor.execute("SELECT event_id, title, description, estimated_time, estimated_danger FROM event WHERE episode_id = %s", [episode_id])
        result_list = []
        query_results = self.cursor.fetchall()
        for result in query_results:
            temp_dict = {}
            temp_dict["title"] = result[1]
            temp_dict["description"] = result[2]
            temp_dict["estimated_time"] = result[3]
            temp_dict["estimated_danger"] = result[4]
            temp_dict["tasks"] = self.view_event_tasks(result[0])
            result_list.append(temp_dict)
        return result_list

    def view_event_tasks(self, event_id):
        self.cursor.execute("SELECT task_id, name, prize FROM event_tasks WHERE event_id = %s", [event_id])
        result_list = []
        query_results = self.cursor.fetchall()
        for result in query_results:
            temp_dict = {}
            temp_dict["name"] = result[1]
            temp_dict["prize"] = result[2]
            temp_dict["contestants"] = self.view_task_contestants(result[0])
            result_list.append(temp_dict)
        return result_list

    def view_task_contestants(self, task_id):
        self.cursor.execute("SELECT a.first_name, a.last_name, t.result, t.points FROM application a INNER JOIN task_contestants t ON t.app_id = a.app_id WHERE t.task_id = %s", [task_id])
        result_list = []
        query_results = self.cursor.fetchall()
        for result in query_results:
            temp_dict = {}
            temp_dict["name"] = result[0] + " " + result[1]
            temp_dict["result"] = result[2]
            temp_dict["points"] = result[3]
            result_list.append(temp_dict)
        return result_list

    def view_med(self, app_id):
        return_dict = {"app_id": app_id}

        self.cursor.execute("SELECT a.first_name, a.last_name, a.dob, a.gender, m.medication_name, am.reason FROM applicant_medication am INNER JOIN application a ON am.app_id=a.app_id INNER JOIN medication m ON am.medication_id=m.medication_id WHERE am.app_id=%s", [app_id])
        query_results = self.cursor.fetchall()
        if len(query_results) == 0:
            return_dict["found"] = "false"
            return return_dict
        else:
            return_dict["name"] = query_results[0][0] + " " + query_results[0][1]
            return_dict["dob"] = query_results[0][2].strftime("%m/%d/%Y")
            return_dict["gender"] = query_results[0][3]
            result_list = []
            for result in query_results:
                temp_dict = {}
                temp_dict["medication_name"] = result[4]
                temp_dict["reason"] = result[5]
                result_list.append(temp_dict)
            return_dict["medication"] = result_list
            print(return_dict)
            return return_dict

    def view_job(self):
        self.cursor.execute("SELECT job_title from jobs")
        query_results = self.cursor.fetchall()
        if len(query_results) == 0:
            return []
        else:
            return_list = []
            for result in query_results:
                return_list.append({"job_title": result[0]})
            return return_list

    def view_voting(self, voting_info):
        return_dict = {"app_id": voting_info["app_id"], "episode_title": voting_info["episode_title"].upper(), "air_date": voting_info["air_date"]}

        self.cursor.execute("SELECT * FROM episode WHERE title=%s AND air_date=%s", [voting_info["episode_title"], voting_info["air_date"]])
        results = self.cursor.fetchone()
        if results == None:
            return_dict["found"] = "episode"
            return return_dict

        self.cursor.execute("SELECT * FROM application WHERE app_id=%s", [voting_info["app_id"]])
        results = self.cursor.fetchone()
        if results == None:
            return_dict["found"] = "contestant"
            return return_dict

        self.cursor.execute("SELECT a.first_name, a.last_name, SUM(vc.votes) FROM application a INNER JOIN voting_contestants vc ON a.app_id=vc.app_id INNER JOIN voting v ON vc.voting_id=v.voting_id INNER JOIN episode e ON v.episode_id=e.episode_id WHERE e.title=%s AND e.air_date=%s", [voting_info["episode_title"], voting_info["air_date"]])
        query_results = self.cursor.fetchone()
        return_dict["name"] = query_results[0] + " " + query_results[1]
        return_dict["votes"] = query_results[2]
        return return_dict