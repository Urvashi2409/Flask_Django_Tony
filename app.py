from flask import Flask, render_template 

# making a new project
app = Flask(__name__)

#decorator 
@app.route("/")
def index():
    return "Hello world!"

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)
