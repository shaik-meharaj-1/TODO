📝 Todo List Application

A simple and user-friendly Todo List Web Application built using Django, HTML, CSS, and SQLite.
This project helps users create, update, and manage daily tasks efficiently

🚀 Features
- ➕ Add new tasks
- ✔️ Mark tasks as completed
- ✏️ Edit existing tasks
- ❌ Delete tasks
- 📅 Stores data using SQLite (default Django database)
- 🎨 Clean and responsive UI using HTML & CSS
- ⚡ Built using Django’s MVT architecture

🛠️ Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS
- Database: SQLite
- Architecture: MVT (Model-View-Template)

Installation

Follow the steps below to run the project locally:

1. Clone the repository :
   
       git clone https://github.com/shaik-meharaj-1/TODO.git
       cd todo-project

3. Create a virtual environment :

       python -m venv venv

Activate it:

In Windows:

    venv\Scripts\activate

OR macOS/Linux:

    source venv/bin/activate

3. Install dependencies :
   
        pip install -r requirements.txt

5. Apply migrations :

       python manage.py migrate

7. Run the server :

       python manage.py runserver

Open your browser and visit:

    http://127.0.0.1:8000/
