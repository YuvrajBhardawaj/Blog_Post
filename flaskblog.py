from flask import Flask, render_template, url_for
app = Flask(__name__)

posts=[
    {
        'author':'Robert Frost',
        'title':'Blog Post1',
        'content':'1st Post content',
        'date_posted':'April 21, 2024'
    },
    {
        'author':'Steve',
        'title':'Blog Post2',
        'content':'2nd Post content',
        'date_posted':'April 25, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if(__name__ == '__main__'):
    app.run(debug=True)