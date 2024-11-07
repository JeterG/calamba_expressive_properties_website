

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure the MongoDB client
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase?directConnection=true"

# mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/services.html")
def services():
    return render_template("services.html")


@app.route("/projects.html")
def projects():
    # List project folders from 'static/images/projects/'
    project_folder = os.path.join(app.static_folder, "images/projects")
    projects = []
    for project in os.listdir(project_folder):
        project_path = os.path.join(project_folder, project)
        if os.path.isdir(project_path):
            images = [
                f
                for f in os.listdir(project_path)
                if os.path.isfile(os.path.join(project_path, f))
                if f.endswith(".jpeg")
            ]
            if images:
                first_image = images[0]
                projects.append({"name": project, "image": first_image})
    return render_template("projects.html", projects=projects)


@app.route("/project/<project_name>.html")
def project_detail(project_name):
    # List images in the project folder and read .txt files
    project_folder = os.path.join(app.static_folder, "images/projects", project_name)
    images = []
    text_content = []
    for item in os.listdir(project_folder):
        item_path = os.path.join(project_folder, item)
        if os.path.isfile(item_path):
            if item.lower().endswith(".txt"):
                with open(item_path, "r") as file:
                    text_content.append(file.read())
            else:
                images.append(item)
    return render_template(
        "project_detail.html",
        project_name=project_name,
        images=images,
        text_content=text_content,
    )


@app.route("/team.html")
def team():
    return render_template("team.html")


@app.route("/achievements.html")
def achievements():
    image_folder = os.path.join(app.static_folder, "images/achievements")
    images = [
        f
        for f in os.listdir(image_folder)
        if os.path.isfile(os.path.join(image_folder, f))
        if f != ".DS_Store"
    ]
    return render_template("achievements.html", images=images)


@app.route("/partners.html")
def partners():
    image_folder = os.path.join(app.static_folder, "images/partners")
    images = [
        f
        for f in os.listdir(image_folder)
        if os.path.isfile(os.path.join(image_folder, f))
        if f != ".DS_Store"
    ]
    return render_template("partners.html", images=images)


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


# @app.route("/submit_contact")
# def submit_contact():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     message = request.form.get("message")

#     # Here you can add code to process the contact form submission
#     # For example, send an email, save to the database, etc.

#     # Flash a message to indicate the form was submitted successfully
#     flash("Your message has been sent successfully!", "success")

#     return redirect(url_for("contact"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
