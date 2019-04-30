from flask import Flask, request, render_template, redirect
from templates import signup
import re

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
    <style>
        .error {{ color:red }}
        <link rel="stylesheet" type="text/css" href="style.css"/>
    </style>
        
    </head>
    <body>
        <h1>Please sign in!</h1>
        <form  action="/" method="post">
            <div>
                <label for="username">Username:</label>
                <input name="username" type="text" value='{username}'/>
                <p class="error">{usernameerror}</p>
            </div>
            <div>
                <label for="password">Password:</label>
                <input name="password" type="text" value='{password}'/>
                <p class="error">{passworderror}</p>
            </div>
            <div>
                <label for="passwordagain">Confirm password:</label>
                <input name="passwordagain" type="text" value='{passwordagain}'/>
                <p class="error">{passwordagainerror}</p>
            </div>
            <div>
                <label for="email">Email:</label>
                <input name="email" type="text" value='{email}' />
                <p class="error">{emailerror}</p>
            </div>
            <br></br>
            <div>
                <input type="submit" value="Signup!">
            </div>
        </form>   
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(usernameerror='', passworderror='', passwordagainerror='', emailerror='',
    username='', password='', passwordagain='',email='')


@app.route("/", methods=['POST'])
def validatesignup():

    username = request.form['username']
    password = request.form['password']
    passwordagain = request.form['passwordagain']
    email = request.form['email']

    usernameerror = ''
    passworderror = ''
    passwordagainerror = ''
    emailerror = ''

    if username == '':
        usernameerror = 'Username cannot be blank.'
    elif len(username) <= 3 or len(username) > 20:
        usernameerror = 'Username must be at least 3 characters but no more than 20 long.'
        username = ''
    elif " " in username:
        usernameerror = 'The username may not contain any spaces.'
        username = ''

    if password == '':
        passworderror = 'Password cannot be blank.'
    elif len(password) <=3 or len(username) > 20:
        passworderror = 'Password must be at least 3 characters but no more than 20 long.'
    elif " " in password:
        passworderror = 'The password may not contain any spaces.'
    
    if passwordagain == '':
        passwordagainerror = 'Confirmation password cannot be blank.'
    elif password != passwordagain:
        passwordagainerror = 'The passwords do not match.'
        
    if email != '': 
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                emailerror = 'The email in invalid and must contain both of the following: period(.) and atsign(@).'
                email = ''
    if not usernameerror and not passworderror and not passwordagainerror and not emailerror:
        username = username
        return '<h1>Welcome, ' + username + '</h1>'
    
    return form.format(username=username, password=password, 
        passwordagain=passwordagain,
        email=email, usernameerror=usernameerror, 
        passworderror=passworderror, emailerror=emailerror,
        passwordagainerror=passwordagainerror)




app.run()
