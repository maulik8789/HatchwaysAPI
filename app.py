from flask import Flask, render_template, request, flash, session
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

#home page shows all posts..............................
@app.route('/')
def home():
    url = "https://api.hatchways.io/assessment/blog/posts?tag="
    r = requests.get(url)
    data = json.loads(r.text)
    return render_template('home.html', data = data)

#showing posts related to tag/tags......................
@app.route('/showposts', methods = ['POST'])
def posts():
    s = str(request.form.get('tag'))
    if s == "" :
        flash("Tags parameter is required")
        return render_template('home.html')
    s= s.replace("," , "&") 
    url = f"https://api.hatchways.io/assessment/blog/posts?tag={s}"
    r = requests.get(url)
    data = json.loads(r.text)
    return render_template('list.html', data = data, s = s)            
