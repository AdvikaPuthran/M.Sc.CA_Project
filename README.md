<b>Description:</b> This project is a fully simulated Smart Parking and Traffic Management System
designed to tackle the challenges of urban traffic congestion and inefficient parking. All features,
including IoT sensor input, payment gateway, traffic data, and reservation logic, are successfully
simulated without any physical hardware or third-party payment integration.

<b>Software:</b> Visual Studio Code 1.99.3, MySQL Workbench 8.0 CE, StarUML 6.3.2

<b>Web Framework:</b> Django 5.1.6

<b>Steps to run this website:</b>
1. Install Visual Studio Code 1.99.3 and MySQL Workbench 8.0 CE
2. Install Python
    Make sure Python is installed on your system.

    To check:

    python --version  # or python3 --version
    Download: https://www.python.org/downloads/
3. Set up environment variables if required. Add Python to the path.
4. Open Visual Studio Code 1.99.3 and open the Smart_Parking_and_Traffic_Management project folder in it.

5. Create & Activate a Virtual Environment (optional but recommended)
    Create virtual environment (name can be anything, e.g., venv)
    python -m venv venv

    Activate it
    For Windows:
      Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
      .\venv\Scripts\Activate.ps1

    For macOS/Linux:
      source venv/bin/activate

6. If not, manually install Django:

      pip install django
7. If you don't have one, you can manually reinstall the packages you used (like django, mysqlclient, etc.):
    pip install django mysqlclient
8. Run the MySQL queries from smart_parking_db.sql which are required in MySQL Workbench.
9. Navigate to the Project Directory
    cd your_project_folder
10. Install Required Dependencies
    Check if a requirements.txt file exists. If yes:

    pip install -r requirements.txt
11. Run Migrations (to set up the database)
      python manage.py migrate
12. Run the Development Server
      python manage.py runserver
      Now open your browser and visit:
      👉 http://127.0.0.1:8000/

<b>Screenshots:</b><br><br>
<img width="1280" height="914" alt="home1" src="https://github.com/user-attachments/assets/263821e2-d3ba-4fe6-9696-39a6deb391e6" /><br><br>
<img width="1280" height="982" alt="home2" src="https://github.com/user-attachments/assets/9e426363-d14b-47a1-b647-bff9a268a63d" /><br><br>
<img width="1280" height="973" alt="about" src="https://github.com/user-attachments/assets/57678d70-9c06-4722-95ee-fe6cfb2d0481" /><br><br>
<img width="1280" height="967" alt="contact" src="https://github.com/user-attachments/assets/5fff2760-0340-457d-9cce-74a84e871cc4" /><br><br>
<img width="1280" height="960" alt="parking_slots1" src="https://github.com/user-attachments/assets/6f9324e8-bd38-4a3f-8084-a3695dba23f1" /><br><br>
<img width="1280" height="969" alt="parking_slots2" src="https://github.com/user-attachments/assets/d68db664-4f20-4070-a72c-0441327d3344" /><br><br>
<img width="1280" height="841" alt="parking_res" src="https://github.com/user-attachments/assets/4291d6b1-9fd8-47f4-b914-eddae148e645" /><br><br>
<img width="1280" height="931" alt="payment" src="https://github.com/user-attachments/assets/b4564a1a-3065-44ed-8244-a34fcfae5798" /><br><br>
<img width="1280" height="852" alt="reserve_success" src="https://github.com/user-attachments/assets/56faa672-db78-48a1-b86d-09b497c4fe7b" /><br><br>
<img width="1280" height="960" alt="traffic_status2" src="https://github.com/user-attachments/assets/28c42a61-2bb9-44e5-ab1f-aaa03255f025" /><br><br>
<img width="1280" height="960" alt="traffic_status1" src="https://github.com/user-attachments/assets/bd60b249-0562-46ab-b03c-97b07f022de3" /><br><br>
<img width="1280" height="945" alt="register" src="https://github.com/user-attachments/assets/67b01174-ed0b-43fa-8964-be4a63823c23" /><br><br>
<img width="1280" height="965" alt="login" src="https://github.com/user-attachments/assets/20448a37-8dac-4a0c-a9e2-d2920633d4a8" /><br><br>
<img width="1280" height="970" alt="dashboard" src="https://github.com/user-attachments/assets/c93b13eb-cb21-41a3-b84a-3f9846fb3632" />
















