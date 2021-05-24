






##Artificially Intelligent Surveillance Tower(AIST)

##User Manual








Table of Contents
1.0 GENERAL INFORMATION
    1.1 System Overview
    1.2 Organization of the Manual
2.0 SYSTEM SUMMARY
    2.1 System Configuration
    2.2 Types of User
3.0 SYSTEM DEPLOYMENT
    3.1 Deploying the System on Ground
3.2 Setting up the Software Environment
3.2.1 Setting up the Virtual Environment
3.2.2 Installing the Library Packages
3.2.3 Setting up the Database Management System
3.2.4 Setting up the Email Notification
3.2.5 Creating admin users
4.0 USER ACCESS
4.1 Admin User
4.1.1 Admin User Panel
4.2 Operator User
5.0 USING THE SYSTEM
5.1 Using the System as Admin User
5.1.1 Admin Dashboard Overview
5.1.2 Detection Log
    5.1.2.1 Photos
    5.1.2.2 Log Report
5.1.3 Tower Feed
5.1.4 Map
5.1.5 User Management
    5.1.5.1 Create User
    5.1.5.2 All Users
    5.1.5.3 Delete User
5.2 Using the System as an Operator
    5.2.1 Operator Dashboard Overview
    5.2.2 Detection Log
        5.2.2.1 Photos
        5.2.2.2 Log Report
    5.2.3 Tower Feed
    5.2.4 Map
6.0 RISK MANAGEMENT

#1.0 GENERAL INFORMATION
Constant surveillance is a very important aspect of the external and internal security of a country. In the context of Bangladesh, our military forces have many secured installations all over which need constant 24/7 surveillance. We have mobile and static surveillance posts for defending those installations along with sensitive borders that we share with our neighboring countries. And these posts are constantly being guarded physically by man. Alongside many important installations situated inside the country need 24/7 surveillance for internal security and safety. But handling all these check/monitoring/surveillance posts that include some difficult terrains like CHT are hard to man all the time.
To mitigate this situation and ensure constant surveillance in the borders and the Key Point Defence Installations we can apply an unmanned AI based surveillance system.
To serve this purpose, we want to establish the AI Surveillance Tower in our national borders(land/sea), Key Point Defence Installations and on difficult terrains to strengthen the security of our country. It will also focus our national defence and security into a dynamic view.
#1.1 System Overview
The purpose of the AI based surveillance system is to provide 24/7 surveillance in difficult as well as sensitive terrains without any physical involvement. Alongside it will provide identification of trace pacers and military vehicles. This system will also be able to detect the infiltration of all kind of intruders and generate an alarm.



#1.2 Organization of the Manual
The user’s manual consists of the following sections.
General Information
System summary
System deployment
User access
Using the system

2.0 SYSTEM SUMMARY
System Summary provides a general overview of the system. It outlines the uses of the system’s hardware and software requirements, System’s configuration, user access and risk factors.

2.1 System Configuration
The AI Surveillance System will be a hardware and software-based system for surveillance which will be fully functional without any physical involvement. With a solar power source, it will be self-propelled and automated. Mainly, it will be a machine learning based human detection system through a wide-angle camera without any human interaction to generate alarm/warning-message to inform the concerned.

2.2 Types of User
There are two types of users:
Admin Users
Operators




3.0 SYSTEM DEPLOYMENT

To work with the system the hardware modules need to be set up on the terrain. 

3.1 Deploying the System on Ground
Set the tower in an open place.
Set the cameras at the top of the tower
Set the solar panels beside the tower in such a way so that it gets most of the daylight.
Set the Sealed Stainless box beside the tower. And Connect all the cables with the hardware modules.
Test the hardware modules.
Ensure that all the hardwares is running properly.
Get the GPS data for the particular location.

3.2 Setting up the Software Environment

Now it's time to set up the Software Environment. As the system is still in it’s Beta version, so the system is not available as a single package. So you need to do some extra work.

3.2.1 Setting up the Virtual Environment

For setting up the virtual environment do the following.
Create a folder in any directory in the deployed system.
Inside the folder open command prompt.
Make sure pip version 3 is installed on the machine. To check the pip version type the following:
py -m pip --version
In the terminal type 
pip install virtualenv
After the successful installation of virtual environment create a virtual environment for your system
Virtualenv env
When the virtual environment is created make sure by following the directory as yourSystemDirectory > env
Run the virtual environment by typing:
.\env\Scripts\activate (for windows) 

 3.2.2 Installing the Library Packages

For deploying the system you need the following python packages. Before that make sure your machine has python installed : python --version in the terminal.

  arrow==1.0.3
   asgiref==3.3.1
   branca==0.4.2
   certifi==2020.12.5
   chardet==4.0.0
   Django==3.1.7
    folium==0.12.1
    idna==2.10
    imutils==0.5.4
Jinja2==2.11.3
    MarkupSafe==1.1.1
numpy==1.20.2
opencv-contrib-python==4.5.1.48
pandas==1.2.4
     Pillow==8.2.0
playsound==1.2.2
     psycopg2==2.8.6
pycairo==1.20.0
python-dateutil==2.8.1
pytz==2021.1
requests==2.25.1
six==1.15.0
sqlparse==0.4.1
threaded==4.1.0
times==0.7
urllib3==1.26.4

 To install the packages you can install by pip inside the virtual environment. Make sure the virtual environment is activated already.
Pip install packageName
Or you can install the packages altogether. For that you need to copy the whole project folder inside the main directory for the software. Then in the terminal do the following:
cd surveillance
pip install -r requirements.txt 
It will take time to install all the packages. Be patient.
After the successful installation of all the packages you can find the installed packages with
Pip freeze

3.2.3 Setting up the Database Management System

To use Postgre in your machine, you need to install:
Postgre Database Server
A graphical tool to administer and manage the DB. pgAdmin is the most popular tool GUI Tool for Postgre
You could individually Download PostgreSQL for Windows and install these components but coupling the settings between the DB server, and a GUI tool could be a challenge. It's best to use a bundled installer which takes care of configuration complexities.
Following is a step by step process on How to Install PostgreSQL

Go to https://www.postgresql.org/download and select Windows 

 You are given two options

1. Interactive Installer by EnterpriseDB
2. Graphical Installer by BigSQL
BigSQL currently installs pgAdmin version 3 which is deprecated. It's best to choose EnterpriseDB which installs the latest version 4

You will be prompted to the desired PostgreSQL version and operating system. Select the latest PostgreSQL version and OS as per your environment
Click the Download Button

Once you Download PostgreSQL, open the downloaded exe and Click next on the install welcome screen. 


Change the Installation directory if required, else leave it to default
Click Next
You may choose the components you want to install in your system. You may uncheck Stack Builder
Click Next
You may change the data location
Click Next
Enter super user password. Make a note of it
Click Next
Leave the port number default
Click Next
Check the pre-installation summary:
Click Next
Click the next button 
Once install is complete you will see the Stack Builder prompt
Uncheck that option. We will use Stack Builder in more advance tutorials
Click Finish
To launch PostgreSQL go to Start Menu and search pgAdmin 4 
You will see pgAdmin homepage 
Click on Servers > PostgreSQL 10 in the left tree 
Enter super user password set during installation
Click OK
You will see the Dashboard
Inside the settings.py of the software change the DATABASES section according to your your superuser and password.


That's it to PostgreSQL installation. 

3.2.4 Setting up the Email Notification

Your software can automatically generate email notification for detection log and user creation. For that reason you need to set up the email configuration. For configuring the email do the following:
Go to settings.py inside YourSoftwareDirectory > surveillance > surveillance > settings.py and set the following:


3.2.5 Creating admin users

To create admin users:
First we’ll need to create a user who can login to the admin site. Run the following command:
python manage.py createsuperuser
 Enter your desired username and press enter.
Username: admin
You will then be prompted for your desired email address:
Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
Password: **********
Password (again): *********
Superuser created successfully.

4.0 USER ACCESS

User can access in two modes. As Admin user and as operator. To login the software user need to start the development server by 
python manage.py runserver
Then go to the following link for the local server access: http://127.0.0.1:8000/ 
The first page is the login page. Give your login credential and login the system.

4.1 Admin User

For login as admin user use your superuser credentials.

4.1.1 Admin User Panel
 
To login in to the admin user panel go to the following link:
http://127.0.0.1:8000/admin
Give your super user credentials to login. You will find a page similar to this. This is django admin user panel. You can do some stuff here:


4.2 Operator User

At the starting of the launch of the new tower there is no operator user. Admin must create an operator user for login access as an operator. That will be covered in the section 5.1.5.1 Create User.
 
After creation of operator user go to the following link:
http://127.0.0.1:8000/
Use your given credentials to login as an operator
You will land in to the operator dashboard


5.0 USING THE SYSTEM

Let’s find out how to use the software. You can use the software as Admin user and Operator User.

5.1 Using the System as Admin User

To use the system as Admin user login as Admin user at the home page.

5.1.1 Admin Dashboard Overview

After you successfully login to the system as admin user you will find the following dashboard:


5.1.2 Detection Log

First button at the admin panel is Detection Log. Which includes 
Photos
Log Report


5.1.2.1 Photos

In this page all the detected photos are shown as a gallery

5.1.2.2 Log Report

In this page all the log reports of the detected images are shown as list.
Each log report includes:
Name
Detection Date
Detection Time
Image Name

5.1.3 Tower Feed

Inside this page all the Towers in the area are shown as a single clickable button. You can start seeing the feed from any of the towers.



5.1.4 Map

Inside this page all the towers in the area are shown in the map of their original location. Each tower is shown with markers. Each marker contains:
Name
Location
Latitude
Longitude
Tower Feed Link

5.1.5 User Management

Operators’ dashboard differ from Admin dashboard in case of User Management. Only the admin can have access to user management. User management has the following options:
Create user 
All Users 
Delete User


5.1.5.1 Create User

You can create an Operator user from this option. 
To create an user provide
User Name
Email
Password
Confirm Password
After successful creation of a user provided email address will get a confirmation email for new user creation. But the email will not contain a password for security purposes. To get the password the operator needs to contact the admin panel.

5.1.5.2 All Users

This option contains all the users as a list including the admin users.
Each row in the table contains:
User Name
First Name
Second Name
Email
Date Joined
Last Login
Is Staff (whether admin user or not)

5.1.5.3 Delete User

This option is for deleting an operator user from the system.
Each user entries contain:
User Name
First Name
Second Name
Email
Date Joined
Last Login
Delete
Admin users are not shown in this list.
Selecting delete will take you to the delete confirmation page. 
If you confirm the deletion then only the user will be deleted.

5.2 Using the System as an Operator

To use the system as an Operator, login as an operator user at the home page.

5.2.1 Operator DashBoard Overview

After you successfully login to the system as an operator you will find the following dashboard:





5.2.2 Detection Log

First button at the operator panel is Detection Log. Which includes 
Photos
Log Report


5.2.2.1 Photos

In this page all the detected photos are shown as a gallery

5.2.2.2 Log Report

In this page all the log reports of the detected images are shown as a list.
Each log report includes:
Name
Detection Date
Detection Time
Image Name

5.2.3 Tower Feed

Inside this page all the Towers in the area are shown as a single clickable button. You can start seeing the feed from any of the towers.



5.2.4 Map

Inside this page all the towers in the area are shown in the map of their original location. Each tower is shown with markers. Each marker contains:
Name
Location
Latitude
Longitude
Tower Feed Link




6.0 RISK MANAGEMENT









## License and Copyright

Copyright © 2021, [MD Rafsun Sheikh](https://github.com/rafsunsheikh).
Released under the [MIT License](LICENSE).
