import os

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
# a simple page that says hello
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/<page>')
def serve_pages(page):
    bootnamen = ["Virtus", "Vijf Pijlen", "Concordia"]
    leden = ["Kuijt", "Gaaij", "Brummer", "Slotboom"]
    if page == "index.html":
       return render_template('index.html')
    if page == "boten.html":
        return render_template('boten.html', bootnamen=bootnamen)
    if page == "leden.html":
        return render_template('leden.html', leden=leden)
    if page == "contact.html":
        return render_template('contact.html')
    if page == "sponsors.html":
        return render_template('sponsors.html')
    if page == "index.html":
        return render_template("index.html")
    else:
        return page_not_found()

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(username)

# @app.route('/hello/<page>')
# def differentpages(page=None):
#     if page =='boten':
#         return redirect(url_for('boten'))
#     elif page =='admin':
#         return redirect(url_for('hello_admin'))
#     elif page =='admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('404'))

# @app.route('/hello/<name>')
# def hello2(name=None):
#     return render_template('base.html',name=name)
# return app
