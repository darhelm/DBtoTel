import sqlite3
import pandas as pd
import datetime
import json
from dotenv import dotenv_values

SECRET = dotenv_values(".env")

# If you have more than one data base to check add their PATH variables here
# add '/etc/x-ui/x-ui.db' for linux make sure it is in string format

PATHS = ['x-ui.db', 'x-ui-chess.db'] 

def findEmail(email, id=None):


    for path in PATHS:
        connect = sqlite3.connect(path)

        try:
            data = pd.read_sql(f"SELECT email, up, down, expiry_time FROM 'client_traffics' WHERE email = '{email}'", con=connect)
        
            data_array = data.to_numpy()
            data_array = data_array[0]

        except IndexError:
            pass
        else:
            ls = []
            email = str(data_array[0])
            upload = int(data_array[1])/ 10**9 # 1 GB = 10^9 MB
            download = int(data_array[2]) / 10**9
            traffic_sum = round(upload + download, 2)

            expiry_time = datetime.datetime.utcfromtimestamp(data_array[3]/1000).strftime('%Y-%m-%d %H:%M:%S')
            
            if expiry_time == "1970-01-01 00:00:00":
                expiry_time = "No Time Limit"

            if id == None:
                items = [email, download, upload, traffic_sum, expiry_time]

            elif id != None:
                items = [email, download, upload, traffic_sum, expiry_time, id]
            
            ls.extend(items)
            
            return ls
        


def findId(id):
    
    # if id exists in 'inbounds' table of db in the settings column turn it into a json file 
    # and return the email of that id to the searchEmail function

    for path in PATHS:
        con = sqlite3.connect(path)
        cur = con.cursor()
        
        data = pd.read_sql("SELECT id FROM 'inbounds'", con=con)
        inboundId = data.to_numpy()
        inboundId = [num[0] for num in inboundId]
        
        for num in inboundId:

            res = cur.execute(f"SELECT settings FROM 'inbounds' WHERE id = {num}")
            stupid_json = res.fetchone()

            json_objects = stupid_json[0].strip().split('\n},\n{')
            json_string = f'[{",".join(json_objects)}]'

            json_data = json.loads(json_string)

            # if you need to store the json file
            # with open("settings.json", "a+") as f:
            #      json.dump(json_data, f, indent=4)

            try:
                for sets in json_data[0]["clients"]:
                    if id == sets["id"]:
                        email = sets["email"]
                        return findEmail(email, id)
            except KeyError:
                break
        
# Simple promp test

# options = ["id", "email"]
# choice = input(f"would you like to select with {options[0]} or {options[1]} : ")

# if choice not in options:
#     print("your input was not recognized")

# elif choice == "id":

#     id = input("enter your id : ").__str__()
#     if type(findId(id)) != list:
#         print(f"the id,{id} did not exist or was not entered correctly!")

#     print(findId(id))

# elif choice == "email":

#     email = input("enter your email : ").__str__()
#     if type(findEmail(email)) != list:
#         print("the email did not exist or was not entered correctly!")

#     print(findEmail(email))