\# 🎓 PlacementApp



PlacementApp is a \*\*Flask + MySQL\*\* web application for managing \*\*students, companies, jobs, applications, and skills\*\* — all in one modern dashboard.  



It comes with \*\*auto database setup + sample data\*\*, so you can start immediately after cloning.  



---



\## 🚀 Features

\- 👨‍🎓 \*\*Students\*\* → Add, update, delete, and view profiles  

\- 🏢 \*\*Companies\*\* → Manage recruiters and company details  

\- 💼 \*\*Jobs\*\* → Post jobs and link them to companies  

\- 📑 \*\*Applications\*\* → Track student job applications with statuses  

\- 🛠️ \*\*Skills\*\* → Maintain skills and assign them to students  

\- ⚡ \*\*Auto Database Setup\*\* → Just run `db\_setup.py` (or `run.py`)  

\- 🎨 \*\*Modern UI\*\* → HeyFriends-inspired playful + clean design  

\- 🎓 \*\*Favicon included\*\* for branding  



---



\## 📋 Requirements

\- Python \*\*3.10+\*\*  

\- MySQL (running locally)  

\- pip (Python package installer)  



---



\## ⚡ First-Time Setup (Step by Step)



\### 1. Clone the Repository

```bash

git clone https://github.com/Arun-Reddy350/placement\_app.git

cd placement\_app

2\. Create a Virtual Environment

bash

Copy code

python -m venv venv



\# Activate on Windows (PowerShell)

venv\\Scripts\\Activate.ps1



\# Activate on macOS/Linux

source venv/bin/activate

3\. Install Dependencies

bash

Copy code

pip install -r requirements.txt

4\. Configure Environment Variables

Copy .env.example → .env



Open .env and set your MySQL username \& password:



dotenv

Copy code

MYSQL\_HOST=localhost

MYSQL\_USER=root

MYSQL\_PASSWORD=your\_mysql\_password

MYSQL\_DB=placement\_db

FLASK\_ENV=development

FLASK\_DEBUG=1

5\. Setup Database (Auto Create + Sample Data)

bash

Copy code

python db\_setup.py

6\. Run the App

Option 1: One-Step Run (Recommended)

bash

Copy code

python run.py

This will:



📦 Run db\_setup.py → create DB, tables, and seed sample data



🚀 Run app.py → start the Flask server



Open in your browser:



cpp

Copy code

http://127.0.0.1:5000

Option 2: Run Manually

bash

Copy code

python db\_setup.py   # creates DB and tables

python app.py        # starts Flask server

📂 Project Structure

php

Copy code

placement\_app/

├─ app.py              # Main Flask app (routes + CRUD)

├─ db\_setup.py         # Creates DB, tables, and seeds sample data

├─ run.py              # One-step script (setup + start server)

├─ requirements.txt    # Python dependencies

├─ .env.example        # Sample env config (copy → .env)

├─ static/

│   ├─ favicon.ico     # App favicon 🎓

│   └─ style.css       # Styles

└─ templates/          # HTML templates

&nbsp;  ├─ base.html

&nbsp;  ├─ index.html

&nbsp;  ├─ dashboard.html

&nbsp;  ├─ students.html

&nbsp;  ├─ companies.html

&nbsp;  ├─ jobs.html

&nbsp;  ├─ applications.html

&nbsp;  └─ skills.html

🛠️ Development Tips

Restart server automatically while coding:



bash

Copy code

set FLASK\_ENV=development   # Windows

export FLASK\_ENV=development # macOS/Linux

python app.py

If favicon doesn’t show → clear browser cache or use incognito.

