from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asdf",   # 🔹 change if your MySQL password is different
    database="placement_db"
)
cursor = db.cursor(dictionary=True)


# ---------- HOME ----------
@app.route('/')
def index():
    return render_template('index.html')


# ---------- STUDENT CRUD ----------
@app.route('/students')
def students():
    cursor.execute("SELECT * FROM Student")
    data = cursor.fetchall()
    return render_template('students.html', students=data)

@app.route('/add_student', methods=['POST'])
def add_student():
    cursor.execute("INSERT INTO Student (Name, Email, Phone, Department, CGPA, ResumeURL) VALUES (%s,%s,%s,%s,%s,%s)",
                   (request.form['name'], request.form['email'], request.form['phone'],
                    request.form['dept'], request.form['cgpa'], request.form['resume']))
    db.commit()
    return redirect('/students')

@app.route('/delete_student/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM Student WHERE StudentID=%s", (id,))
    db.commit()
    return redirect('/students')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        cursor.execute("UPDATE Student SET Name=%s, Email=%s, Phone=%s, Department=%s, CGPA=%s, ResumeURL=%s WHERE StudentID=%s",
                       (request.form['name'], request.form['email'], request.form['phone'],
                        request.form['dept'], request.form['cgpa'], request.form['resume'], id))
        db.commit()
        return redirect('/students')
    else:
        cursor.execute("SELECT * FROM Student WHERE StudentID=%s", (id,))
        student = cursor.fetchone()
        return render_template('edit_student.html', student=student)


# ---------- COMPANY CRUD ----------
@app.route('/companies')
def companies():
    cursor.execute("SELECT * FROM Company")
    data = cursor.fetchall()
    return render_template('companies.html', companies=data)

@app.route('/add_company', methods=['POST'])
def add_company():
    cursor.execute("INSERT INTO Company (CompanyName, Email, Industry, Location) VALUES (%s,%s,%s,%s)",
                   (request.form['name'], request.form['email'], request.form['industry'], request.form['location']))
    db.commit()
    return redirect('/companies')

@app.route('/delete_company/<int:id>')
def delete_company(id):
    cursor.execute("DELETE FROM Company WHERE CompanyID=%s", (id,))
    db.commit()
    return redirect('/companies')


# ---------- JOB CRUD ----------
@app.route('/jobs')
def jobs():
    cursor.execute("""
        SELECT Job.JobID, Title, Description, CTC, EligibilityCriteria, PostedDate, CompanyName
        FROM Job JOIN Company ON Job.CompanyID = Company.CompanyID
    """)
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM Company")
    companies = cursor.fetchall()

    return render_template('jobs.html', jobs=data, companies=companies)

@app.route('/add_job', methods=['POST'])
def add_job():
    cursor.execute("INSERT INTO Job (Title, Description, CTC, EligibilityCriteria, PostedDate, CompanyID) VALUES (%s,%s,%s,%s,%s,%s)",
                   (request.form['title'], request.form['desc'], request.form['ctc'],
                    request.form['criteria'], request.form['date'], request.form['company']))
    db.commit()
    return redirect('/jobs')

@app.route('/delete_job/<int:id>')
def delete_job(id):
    cursor.execute("DELETE FROM Job WHERE JobID=%s", (id,))
    db.commit()
    return redirect('/jobs')


# ---------- APPLICATION CRUD ----------
@app.route('/applications')
def applications():
    cursor.execute("""
        SELECT ApplicationID, ApplicationDate, Status, Student.Name AS StudentName, Job.Title AS JobTitle
        FROM Application
        JOIN Student ON Application.StudentID = Student.StudentID
        JOIN Job ON Application.JobID = Job.JobID
    """)
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM Job")
    jobs = cursor.fetchall()

    return render_template('applications.html', applications=data, students=students, jobs=jobs)

@app.route('/add_application', methods=['POST'])
def add_application():
    cursor.execute("INSERT INTO Application (ApplicationDate, Status, StudentID, JobID) VALUES (%s,%s,%s,%s)",
                   (request.form['date'], request.form['status'], request.form['student'], request.form['job']))
    db.commit()
    return redirect('/applications')

@app.route('/delete_application/<int:id>')
def delete_application(id):
    cursor.execute("DELETE FROM Application WHERE ApplicationID=%s", (id,))
    db.commit()
    return redirect('/applications')


# ---------- SKILL CRUD ----------
@app.route('/skills')
def skills():
    cursor.execute("SELECT * FROM Skill")
    skills = cursor.fetchall()
    return render_template('skills.html', skills=skills)

@app.route('/add_skill', methods=['POST'])
def add_skill():
    cursor.execute("INSERT INTO Skill (SkillName) VALUES (%s)", (request.form['name'],))
    db.commit()
    return redirect('/skills')

@app.route('/delete_skill/<int:id>')
def delete_skill(id):
    cursor.execute("DELETE FROM Skill WHERE SkillID=%s", (id,))
    db.commit()
    return redirect('/skills')


# ---------- STUDENT-SKILL RELATION ----------
@app.route('/student_skills')
def student_skills():
    cursor.execute("""
        SELECT StudentSkill.StudentID, StudentSkill.SkillID, Student.Name AS StudentName, Skill.SkillName
        FROM StudentSkill
        JOIN Student ON StudentSkill.StudentID = Student.StudentID
        JOIN Skill ON StudentSkill.SkillID = Skill.SkillID
    """)
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM Skill")
    skills = cursor.fetchall()

    return render_template('student_skills.html', student_skills=data, students=students, skills=skills)

@app.route('/add_student_skill', methods=['POST'])
def add_student_skill():
    cursor.execute("INSERT INTO StudentSkill (StudentID, SkillID) VALUES (%s,%s)",
                   (request.form['student'], request.form['skill']))
    db.commit()
    return redirect('/student_skills')

@app.route('/delete_student_skill/<int:student_id>/<int:skill_id>')
def delete_student_skill(student_id, skill_id):
    cursor.execute("DELETE FROM StudentSkill WHERE StudentID=%s AND SkillID=%s", (student_id, skill_id))
    db.commit()
    return redirect('/student_skills')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
