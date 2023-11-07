from flask import Flask, render_template, request

app = Flask(__name__)


# Make a homepage
@app.route('/')
def homepage():
    # aboutmeInfo = ["I'm currently a full time students, majoring in Computer Science, at University of Rio Grand Valley"]    
    return render_template('homepage.html', Name ="Eric")
# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)


# @app.route('/hello/<name>')
# def hello(name):
#     listOfNames = [name, "Eepy", "Little"]
#     return render_template('name.html', Sname = name, nameList=listOfNames)


# Add the option to run this file directly
if __name__== "__main__":
    app.run(debug=True)