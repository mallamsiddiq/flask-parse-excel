# Hey!! Read Me

# Documentation on my solution

Firstly, my humble apologies for turning in my solution this late. I realized apart from just getting familiar with flask/blueprint/almendic structure, the code base isn't working on startup as some lines needed debugging, I presume it was deliberate on purpose.

I have solved the problem with the flask environment as required and with it created a solution that solved the outlined.

it's a simple python app meant to run locally


##	Navigation

This solution is built on docker image to reduce command line interfacing, aid generic virtual environment among other benefits.

Right in this project root,

###	1. with docker installed on your machine; 


Build the image. simply run:

	$ docker-compose build


And run:

	$ docker-compose up -d

To spin up.

And BOOM! your app is running on : 

	http://localhost:5000

	navigte to http://localhost:5000/home/all-users


###	2. withouth docker installed on your machine


And if you don't have docker installed, Don't' fret. I've got you covered. Again, right in the project root,

with python and pip installed, create a new virtual environment and  

	$ pip install -r requirements.txt

SET ENVIRONMENT VARIABLES

	$ export FLASK_APP=application.py

	$ export APP_SETTINGS=instance.config.DoleAppConfig	

	$ export FLASK_DEBUG=1;

OR, IF ON WINDOWS

	$ set FLASK_APP=application.py

	$ set APP_SETTINGS=instance.config.DoleAppConfig	

	$ set FLASK_DEBUG=1;	

Then lastly, 

	$ flask run

And again you app is running on : 

	http://localhost:5000

	navigte to http://localhost:5000/home/all-users


the db is preceeded with users data from ealier by default


The db was preceded with users data from earlier.


I created some views to handle events based on business' logics, you must be a logged in user to access most functionalities of the app as you'll be redirected to login on such clicks.

i have created a user account -> 

	--> username : dole user

	--> password : dole

You can log in with that.

The homepage `/home/all-users`  is visible to all and it contains a table listing all users in the company. Each row in the table is clickable and points to the respective user's details on the endpoint `/home/users/<user_id>` that tells their story so far in the industry across several units. the total years spent by this employee is highlighted in bold on their details’ page

A column on this table that shows summation of total years spent by each user across units worked is made hidden until you are logged in.

there is a link 'Company Stats' that points to `/home/units` where you'll see the company statistics on years spent by all employees so far in different units, there's a table, a graph and a doughnut chart

The endpoint `/home/upload-excel` points to a view where you can upload an excel file, the view will loop through its rows and update our database by values of users, units and related years active. A clickable link also points to this from the navbar with identifier-text 'upload excel'. a quick run through list of users in the uploaded file is returned and displayed in a table on the same page. 

You can login at the endpoint `/auth/login`, logout at `auth/logout` and also create a new account at `auth/users/create`.

***[NEW] I have created another endpoint where you can delete all records in the tables. `/home/delete`***

***[NEW]Also kindly run the app with internet connection to ensure proper running of the imported CDNs [jquery, bootstrap etc]***



## 	Thoughts' process


I notice there's issues of dependency from the exercise folder i received, perhaps due the diverse environments of developers. As a result,
I have used docker and docker compose to run the app on a virtual machine solving the issues of conflicting environment dependencies.

Since i will be saving the data from the excel sheet on our db, i leave the statical data to be manually computed by annotation generation from the db to prevent the user from experiencing long time wait after upload due to a computational heavy process of grouping the data, annotating the values in various forms, also this will enable future lookup and query of users-units' info.

To record more information about users and the units they worked at [ a relationship instance] I created an extra 'Association table’ : Employment that keeps track of the users details at the units -> 'years active' and 'title of employee at the Unit'.

I followed the `blueprint` structure religiously as it conforms so well with standard ways of application structuring aiding loose coupling, maintainability among others


## 	NOTE

This is test app and expected to be run locally as it is not production ready as best standard is requred


### Thank you for reading this far and I hope you have fun playing with the app


### Contact the developer @mallamsiddiq@gmail.com

Thanks.
