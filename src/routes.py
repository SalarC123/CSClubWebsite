from flask import Flask, render_template, url_for
app = Flask(__name__)

# TODO CHANGE DESCRIPTIONS
# TODO SEPARATE @MEDIA STYLES INTO RESPECTIVE FILES

# TO RUN FLASK APP, TYPE THIS IN THE TERMINAL:
    # export FLASK_APP=routes.py
    # MAC:
      # python3 -m venv venv
      # . venv/bin/activate
    # WINDOWS:
      # py -3 -m venv venv
      # venv\Scripts\activate
    # cd src
    # pip3 install -r requirements.txt
    # flask run

# TO RUN APP ON REPL.IT
  # create .replit file and add
    # language = "bash"
    # run = "python3 -m pip install --user --upgrade pip && pip install --upgrade pip && export FLASK_APP=routes.py && python3 -m venv venv && . venv/bin/activate && cd src && pip3 install -r requirements.txt && flask run --host=0.0.0.0 --port=8000"
  # Now click repl's "run" button
  # The second time you run it, you need to remove everything before "export" in the "run" command 
  # if you reload the page, add the original "run" command in the .replit file again

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

@app.route('/programs/physics.html')
def physics():
  title = "Physics TI84 Programs"
  description = "Physics programs for graphing calculators"
  stylesheet = "physics.css"
  jsFile = "physics.js"
  return render_template(
    "TIphysics.html",
    title=title,
    description=description,
    stylesheet=stylesheet,
    jsFile=jsFile,
  )

@app.route('/programs/geometry.html')
def geometry():
  title = "Geometry TI84 Programs"
  description = "Geometry programs for graphing calculators"
  stylesheet = "geometry.css"
  jsFile = "geometry.js"
  return render_template(
    "TIgeometry.html",
    title=title,
    description=description,
    stylesheet=stylesheet,
    jsFile=jsFile,
  )

@app.route('/programs/converters.html')
def converters():
  title = "Conversion TI84 Programs"
  description = "Conversion programs for graphing calculators"
  stylesheet = "converters.css"
  jsFile = "converters.js"
  return render_template(
    "TIconverters.html",
    title=title,
    description=description,
    stylesheet=stylesheet,
    jsFile=jsFile,
  )

@app.route('/legal.html')
def legal():
  title = "Terms of Service & Privacy Policy"
  description = "Terms of Service of the Website and Privacy Policy Notice of Website"
  stylesheet = "legal.css"
  return render_template(
    "legal.html",
    title=title,
    description=description,
    stylesheet=stylesheet,
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