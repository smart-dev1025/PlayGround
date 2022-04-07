# PlayGround
A free, open-source Startup project based on the "Django".

------------
### Features

- "PlayGround" section to PlayGround List
- "Admin" section to create and edit a PlayGround
- Translation ready
- Auth system (login & logout and forget a password)
- Front-end forms to create new object
------------
### How to install and run (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/smart-dev318/PlayGround		# clone the project
cd PlayGround		                                        # go to the project DIR
virtualenv -p python3 .venv		                        # Create virtualenv named .venv
source .venv/bin/activate		                        # Active virtualenv named .venv
pip install -r requirements.txt		                        # Install project requirements in .venv
python manage.py makemigrations		                        # Create migrations files
python manage.py migrate		                        # Create database tables
python manage.py createsuperuser                        # Create Super User for admin
python manage.py runserver		                        # Run the project
```
3. Go to  `http://127.0.0.1:8000/playground` to use project
4. Go to  `http://127.0.0.1:8000/admin` to run admin
------------

------------
### TODO list

- [x] Create search section
- [x] Create user Login/Logout forms in front-end
- [x] Create dynamic forms to add contents in front-end
