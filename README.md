
>*This project is not production ready.*

# Introduction
In this Project we are going to Read the x-ui's data base file From [Mr.Sanaei's](https://github.com/MHSanaei/3x-ui) x-ui panel and display some useful information in Telegram using a Telegram bot.
# Project Goals
The goal of this project is to eventually turn into a webpage based application that utilizes Django and JS Frameworks to Display user information on a webpage and in telegram automatically without much effort.

# Paths And Variables
Since the Project is currently not in any position to be production ready i have not added an automation system yet,how ever if you wish to use the project you must get a Token and a user ID from telegram and put it in a **.env** file with the variables **API_TOKEN** and **USR_NAME** in the same directory as the main.py file and **change the path** to your x-ui db file in **read_db.py**

# Running the project
The project can be run using `nohup` until a docker file is added for proper application hosting and building on linux servers and hosts.

```nohup python3 main.py > /dev/null 2>&1 & echo $! > run.pid```

in case the need arises to kill the current running proccess access the pid.log file and execute 
```kill -9 $(cat run.pid)```