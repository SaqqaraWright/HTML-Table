from flask import Flask, render_template, redirect, request
app = Flask(__name__)


users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]



@app.route('/')                           
def htmlTable():
    
    return render_template('index.html',x=users)

    











if __name__=="__main__":
    app.run(debug=True)