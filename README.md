<b>Description:</b> This project is a fully simulated Smart Parking and Traffic Management System
designed to tackle the challenges of urban traffic congestion and inefficient parking. All features,
including IoT sensor input, payment gateway, traffic data, and reservation logic, are successfully
simulated without any physical hardware or third-party payment integration.

<b>Software:</b> Visual Studio Code 1.99.3, MySQL Workbench 8.0 CE, StarUML 6.3.2

<b>Web Framework:</b> Django 5.1.6

<b>Steps to run this website:</b>
1. Install Python
Make sure Python is installed on your system.

To check:

python --version  # or python3 --version
Download: https://www.python.org/downloads/

2. Create & Activate a Virtual Environment (optional but recommended)
# Create virtual environment (name can be anything, e.g., venv)
python -m venv venv

# Activate it
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
3. Install Required Dependencies
Check if a requirements.txt file exists. If yes:

pip install -r requirements.txt
If not, manually install Django:

pip install django
4. Navigate to the Project Directory
cd your_project_folder
5. Run Migrations (to set up the database)
python manage.py makemigrations
python manage.py migrate

6. Run the Development Server
python manage.py runserver
Now open your browser and visit:
👉 http://127.0.0.1:8000/


