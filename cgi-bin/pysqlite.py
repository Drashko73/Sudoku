import json
import random
import sqlite3
import hashlib

POINTS = {
    "Easy"      :2,
    "Medium"    :4,
    "Hard"      :6,
    "Expert"    :8
}

class Database(object):
    """ Class for communication with the database """
    
    global POINTS
    
    def __init__(self) -> None:
        self.conn = sqlite3.connect("./db/database.db")    # provide valid path to a database

    ####################################################################
    # Get user information by given sessid
    ####################################################################
    def find_user_by_sessid(self, sessid):
        sql = "SELECT * FROM users WHERE sessid='{}'".format(sessid)
        q = self.conn.cursor()
        q.execute(sql)
        self.conn.commit()
        for row in q.fetchall():
            response = {}
            response["id"]          = row[0]        # store user's id
            response["email"]       = row[1]        # store user's email
            response['firstName']   = row[2]        # store user's first name
            response['lastName']    = row[3]        # store user's last name
            response['balance']     = row[5]        # store user's balance
            response['totalPlayed'] = row[7]        # store how many games user completed
            q.close()   # close cursor
            return response

    ####################################################################
    # Get user information by given email and password
    ####################################################################
    def get_user(self, email: str, password: str):
        
        response = {}
        sql_select = "SELECT * FROM users WHERE email = '{}' AND password = '{}'".format(email, password)
        q = self.conn.cursor()
        q.execute(sql_select)
        self.conn.commit()
        result = q.fetchone()

        if result:
            response = {
                "id"            : result[0],
                'email'         : result[1],
                'firstName'     : result[2],
                'lastName'      : result[3],
                'balance'       : result[5],
                'sessid'        : result[6],
                'totalPlayed'   : result[7]
            }
            return response

        return False
    
    ####################################################################
    # Check whether given email exists or not
    ####################################################################
    def email_exists(self, email: str):
        sql_select = "SELECT * FROM users WHERE email = '{0}'".format(email)
        
        q = self.conn.cursor()
        q.execute(sql_select)
        self.conn.commit()
        result = q.fetchone()

        return True if result else False
    
    ####################################################################
    # Register new user
    ####################################################################
    def register_user(self, info):
        
        info = json.loads(info)
        mail_exists = self.email_exists(info["email"])
        response=dict()
        
        response['register']='False'
        if not mail_exists:
            sessid = "-1"
            password=hashlib.sha256(info['password'].encode('utf-8')).hexdigest()   # hesiranje sifre
            sql="INSERT INTO users (email, firstName, lastName, password, balance, sessid) VALUES ('{}', '{}', '{}', '{}', '{}','{}');".format(info['email'], info['firstName'], info['lastName'], password, 0.0, sessid)
            q = self.conn.cursor()
            q.execute(sql)
            self.conn.commit()
            q.close()
            response['register'] = 'True'
        return response
    
    ####################################################################
    # Login user
    ####################################################################
    def login_user(self, email, password):
        response = {}
        response['login']='False'
        hashed_pass=hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = self.get_user(email, hashed_pass)
        
        if not user: return response
        
        user["sessid"] = random.randint(10**13, 10**14 - 1)
        sql="UPDATE users SET sessid = '{}' WHERE email = '{}';".format(user["sessid"], email)
        q = self.conn.cursor()
        q.execute(sql)
        self.conn.commit()
        q.close()
        
        response['login'] = "True"
        response["info"] = user
        return response
    
    ####################################################################
    # Logout user
    ####################################################################
    def logout_user(self, sessid):
        sql = "UPDATE users set sessid='-1' where sessid='{}'".format(sessid)
        q = self.conn.cursor()
        q.execute(sql)
        self.conn.commit()
        result = q.fetchone
        if result:
            return True
    
    ####################################################################
    # Get user information by email address
    ####################################################################
    def get_user_by_email(self, email: str):
        response = {}
        sql_select = "SELECT * FROM users WHERE email = '{}'".format(email)
        q = self.conn.cursor()
        q.execute(sql_select)
        self.conn.commit()
        result = q.fetchone()

        if result:
            response = {
                "id"            : result[0],
                'email'         : result[1],
                'firstName'     : result[2],
                'lastName'      : result[3],
                'balance'       : result[5],
                'sessid'        : result[6],
                'totalPlayed'   : result[7],
                'playedEasy'    : result[8],
                'bestEasy'      : result[9],
                'playedMedium'  : result[10],
                'bestMedium'    : result[11],
                'playedHard'    : result[12],
                'bestHard'      : result[13],
                'playedExpert'  : result[14],
                'bestExpert'    : result[15],
                'totalPoints'   : result[16]
            }
            return response

        return False
    
    ####################################################################
    # Compare two strings representing time (time format - 00:00:00)
    ####################################################################
    def compare_time(self, time_format_1, time_format_2):
        splitted1 = time_format_1.split(":")
        splitted2 = time_format_2.split(":")
        
        time1 = int(splitted1[0])*3600 + int(splitted1[1])*60 + int(splitted1[2])
        time2 = int(splitted2[0])*3600 + int(splitted2[1])*60 + int(splitted2[2])
        
        return time1 < time2
    
    ####################################################################
    # Update stats for given player
    ####################################################################
    def increase_total_completed(self, email, level, time):
        sql_select = "UPDATE users SET totalPlayed = totalPlayed + 1 WHERE email = '{}'".format(email)
        q = self.conn.cursor()
        q.execute(sql_select)
        self.conn.commit()
        
        if level == "Easy": sql = "UPDATE users SET playedEasy = playedEasy + 1 WHERE email = '{}'".format(email)
        elif level == "Medium": sql = "UPDATE users SET playedMedium = playedMedium + 1 WHERE email = '{}'".format(email)
        elif level == "Hard": sql = "UPDATE users SET playedHard = playedHard + 1 WHERE email = '{}'".format(email)
        else: sql = "UPDATE users SET playedExpert = playedExpert + 1 WHERE email = '{}'".format(email)
        
        q = self.conn.cursor()
        q.execute(sql)
        self.conn.commit()
        
        sql_n = "UPDATE users SET totalPoints = totalPoints + {} WHERE email = '{}'".format(POINTS[level], email)
        q = self.conn.cursor()
        q.execute(sql_n)
        self.conn.commit()
        
        sql1 = ""
        user = self.get_user_by_email(email)
        if level == "Easy" and self.compare_time(time, user["bestEasy"]):
            sql1 = "UPDATE users SET bestEasy = '{}' WHERE email = '{}'".format(time, email)
        elif level == "Medium" and self.compare_time(time, user["bestMedium"]):
            sql1 = "UPDATE users SET bestMedium = '{}' WHERE email = '{}'".format(time, email)
        elif level == "Hard" and self.compare_time(time, user["bestHard"]):
            sql1 = "UPDATE users SET bestHard = '{}' WHERE email = '{}'".format(time, email)
        else:
            if self.compare_time(time, user["bestExpert"]):
                sql1 = "UPDATE users SET bestExpert = '{}' WHERE email = '{}'".format(time, email)
        
        if sql1 != "":
            q = self.conn.cursor()
            q.execute(sql1)
            self.conn.commit()
        
        return True
    
    ####################################################################
    # Get all users that played at least a single game
    ####################################################################
    def get_all_users(self):
        response = []
        sql_select = "SELECT * FROM users WHERE totalPlayed > 0 ORDER BY totalPoints DESC"
        q = self.conn.cursor()
        q.execute(sql_select)
        self.conn.commit()
        results = q.fetchall()

        for row in results:
            user = {
                "id"            : row[0],
                'email'         : row[1],
                'firstName'     : row[2],
                'lastName'      : row[3],
                'balance'       : row[5],
                'sessid'        : row[6],
                'totalPlayed'   : row[7],
                'playedEasy'    : row[8],
                'bestEasy'      : row[9],
                'playedMedium'  : row[10],
                'bestMedium'    : row[11],
                'playedHard'    : row[12],
                'bestHard'      : row[13],
                'playedExpert'  : row[14],
                'bestExpert'    : row[15],
                'totalPoints'   : row[16]
            }
            response.append(user)

        return response