from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add_form():
    """Shows form for adding a new student."""

    return render_template("add_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    github = request.form.get('github')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    hackbright.make_new_student(fname, lname, github)

    html = render_template("student_created.html",
                           github=github)
    return html


@app.route("/project-search")
def project_search_form():
    """ Shows form for searching projects. """

    return render_template("project_search.html")


@app.route("/project")
def get_project():
    """Show information about a project."""

    title = request.args.get('title')
    project_title, description, max_grade = hackbright.get_project_by_title(title)
    html = render_template("project_info.html",
                           title=project_title,
                           description=description,
                           max_grade=max_grade)
    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
