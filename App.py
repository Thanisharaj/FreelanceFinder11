from flask import Flask, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to FreelanceFinder</h1><p>This is the homepage served from Flask.</p>"

@app.route("/freelancers")
def freelancers():
    freelancers_list = []
    with open("users.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            freelancers_list.append(row)
    return str(freelancers_list)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        skill = request.form.get("skill")
        email = request.form.get("email")
        with open("users.csv", mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, skill, email])
        return redirect("/")
    return """
    <form method='POST'>
        Name: <input type='text' name='name'><br>
        Skill: <input type='text' name='skill'><br>
        Email: <input type='email' name='email'><br>
        <input type='submit' value='Register'>
    </form>
    """
