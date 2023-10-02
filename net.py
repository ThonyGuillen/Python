from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return 'Hola mundo'

@app.route('/nom')
def nom():
    return 'Anthony'

__name__=='__name__'
app.run()