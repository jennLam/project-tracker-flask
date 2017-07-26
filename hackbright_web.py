"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    projects = hackbright.get_grades_by_github(github)

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github, 
                           projects=projects)
    return html


@app.route("/student-search")
def get_student_form(): 
    """Show form for searching for a student """

    return render_template("student_search.html")

@app.route("/student-create")
def show_new_student_form(): 
    """Show form for creating a new student"""

    return render_template("student_create.html")

@app.route("/student-add", methods=['POST'])
def student_add(): 
    """Add a student. """

    firstname = request.form.get("first_name")
    lastname = request.form.get("last_name")
    github = request.form.get("github_name")

    hackbright.make_new_student(firstname, lastname, github)

    return render_template("student_success.html", firstname=firstname,
                            lastname=lastname, github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
