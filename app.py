#this is my first actual website, built with flask and python
from cmath import phase
import json
from os import link
import requests
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

en_translations = {
  'home': 'Home',
  'aboutme': 'About Me',
  'projects': 'Projects',
  'knowledge': 'Shared Knowledge',
  'quote': '"As a cybersecurity professional and Computer-Science Student with a passion for programming, I try to bring a unique blend of technical expertise and practical experience to every project."'
}

de_translations = {
  'home': 'Start',
  'aboutme': 'Über Mich',
  'projects': 'Projekte',
  'knowledge': 'Ressourcen',
  'quote': '"Als Informatik-Student und Cyber-Security-Enthusiast, versuche ich in jedes Projekt eine einzigartige Mischung von beiden Welten miteinzubringen."'
}

language = "en"

def get_translation(key, language):
  if language == 'de':
    return de_translations.get(key)
  else:
    return en_translations.get(key)

@app.route('/language', methods=['POST'])
def set_language():
    global language
    if language == 'en':
        language = 'de'
    else:
        language = 'en'
    return redirect(request.referrer)  # Redirect back to the referring page

@app.route('/', methods=['GET', 'POST'])
def index():
    global language
    if request.method == 'POST':
        language = request.form['lang']
    name = "J. Hofer"
    home = get_translation('home', language)
    aboutme = get_translation('aboutme', language)
    projects = get_translation('projects', language)
    knowledge = get_translation('knowledge', language)
    quote = get_translation('quote', language)
    otherlanguage = "EN" if language == "de" else "DE"
    github = "https://github.com/Peanut1906"
    linkedin = "https://www.linkedin.com/in/joshi-h-293914240"
    instagram = ""
    email = "pinatsu@proton.me"

    return render_template('index.html',name=name,home=home,aboutme=aboutme,projects=projects,knowledge=knowledge,quote=quote,otherlanguage=otherlanguage,github=github,linkedin=linkedin,instagram=instagram,email=email)

@app.route('/aboutme')
def aboutme():
    global language
    if request.method == 'POST':
        language = request.form['lang']
    name = "JH"
    home = get_translation('home', language)
    aboutme = get_translation('aboutme', language)
    projects = get_translation('projects', language)
    knowledge = get_translation('knowledge', language)
    otherlanguage = "EN" if language == "de" else "DE"

    return render_template('aboutme.html', name=name,home=home,aboutme=aboutme,projects=projects,knowledge=knowledge,otherlanguage=otherlanguage)

@app.route('/projects')
def projects():
    global language
    if request.method == 'POST':
        language = request.form['lang']
    name = "JH"
    home = get_translation('home', language)
    aboutme = get_translation('aboutme', language)
    projects = get_translation('projects', language)
    knowledge = get_translation('knowledge', language)
    otherlanguage = "EN" if language == "de" else "DE"

    return render_template('projects.html', name=name,home=home,aboutme=aboutme,projects=projects,knowledge=knowledge,otherlanguage=otherlanguage)

@app.route('/knowledge')
def knowledge():
    global language
    if request.method == 'POST':
        language = request.form['lang']
    name = "JH"
    home = get_translation('home', language)
    aboutme = get_translation('aboutme', language)
    projects = get_translation('projects', language)
    knowledge = get_translation('knowledge', language)
    otherlanguage = "EN" if language == "de" else "DE"

    return render_template('knowledge.html', name=name,home=home,aboutme=aboutme,projects=projects,knowledge=knowledge,otherlanguage=otherlanguage)


"""
@app.route('/education')
def education():
    df_education.fillna('',inplace=True)
    d = {}
    for i in range(len(df_education)):
        institute = df_education.iloc[i]['Institute']
        degree = df_education.iloc[i]['Degree']
        date = df_education.iloc[i]['Date']
        extrainfo = df_education.iloc[i]['Extra Info']
        image = df_education.iloc[i]['Image']
        d[institute]={}
        d[institute]['degree']=degree
        d[institute]['date']=date
        d[institute]['extrainfo']=extrainfo
        d[institute]['image']=image
    return render_template('education.html',educationinfo=d,name=name)

@app.route('/experience')
def experience():
    df_experience.fillna('',inplace=True)
    d = {}
    for i in range(len(df_experience)):
        designation = df_experience.iloc[i]['Designation']
        company = df_experience.iloc[i]['Company']
        image = df_experience.iloc[i]['Image']
        date = df_experience.iloc[i]['Date']
        info = df_experience.iloc[i]['Info']
        d[company]={}
        d[company]['designation']=designation
        d[company]['image']=image
        d[company]['date']=date
        d[company]['info']=info
    return render_template('experience.html',experienceinfo=d,name=name)

@app.route('/projects')
def projects():
    df_projects.fillna('',inplace=True)
    d = {}
    for i in range(len(df_projects)):
        projectname = df_projects.iloc[i]['Project Name']
        description = df_projects.iloc[i]['Description']
        image = df_projects.iloc[i]['Image']
        date = df_projects.iloc[i]['Date']
        d[projectname]={}
        d[projectname]['image']=image
        d[projectname]['description']=description
        d[projectname]['date']=date
    return render_template('projects.html',projectinfo=d,name=name)

@app.route('/resume')
def resume():
    df_basic_info.fillna('',inplace=True)
    resumelink = df_basic_info[df_basic_info['Column']=='Resume Link']['Value'].values[0]
    return render_template('resume.html',resumelink=resumelink,name=name)

"""

if __name__ == '__main__':
    app.run(debug=True)
