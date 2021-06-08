from flask import Flask, render_template, url_for
app = Flask(__name__)

# TODO CHANGE DESCRIPTIONS
# TODO SEPARATE @MEDIA STYLES INTO RESPECTIVE FILES

# TO RUN FLASK APP, TYPE THIS IN THE TERMINAL:
    # export FLASK_APP=routes.py
    # source venv/bin/activate
    # cd src
    # pip3 ins$ export FLASK_APP=hello
    # flask run

@app.route('/')
def landing():
    title = "PVCS Club"
    description = "Landing page for The Pleasant Valley Computer Science Club"
    stylesheet = "index.css"
    jsFile = "index.js"
    return render_template(
        "index.html", 
        title=title, 
        description=description,
        stylesheet=stylesheet,
        jsFile=jsFile,
)

@app.route('/projects.html')
def projects():
    title = "Projects"
    description = "Projects page for The Pleasant Valley Computer Science Club"
    stylesheet = "projects.css"
    jsFile = "projects.js"
    return render_template(
        "projects.html", 
        title=title, 
        description=description,
        stylesheet=stylesheet,
        jsFile=jsFile,
)

@app.route('/resources.html')
def resources():
    title = "Resources"
    description = "Resources page for The Pleasant Valley Computer Science Club"
    stylesheet = "resources.css"
    jsFile = "resources.js"
    return render_template(
        "resources.html", 
        title=title, 
        description=description,
        stylesheet=stylesheet,
        jsFile=jsFile,
)

@app.route('/opportunities.html')
def opportunities():
    title = "Opportunities"
    description = "Opportunities page for The Pleasant Valley Computer Science Club"
    stylesheet = "opportunities.css"
    jsFile = "opportunities.js"
    return render_template(
        "opportunities.html", 
        title=title, 
        description=description,
        stylesheet=stylesheet,
        jsFile=jsFile,
)

@app.route('/about.html')
def about():
    title = "About"
    description = "About page for The Pleasant Valley Computer Science Club"
    stylesheet = "about.css"
    jsFile = "about.js"
    return render_template(
        "about.html", 
        title=title, 
        description=description,
        stylesheet=stylesheet,
        jsFile=jsFile,
)

@app.route('/join.html')
def join():
    title = "Join The Club"
    description = "Join The Pleasant Valley Computer Science Club"
    stylesheet = "join.css"
    jsFile = "join.js"
    return render_template(
        "join.html", 
        title=title, 
        description=description,
        stylesheet=stylesheet,
        jsFile=jsFile,
)

@app.errorhandler(404)
def not_found(error):
    title = "404 Error"
    description = "404: Page Not Found"
    stylesheet = "404.css"
    return render_template(
        "404.html",
        title=title,
        description=description,
        stylesheet=stylesheet
    )

if __name__ == "__main__":
    app.run()