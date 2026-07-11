# importing

from flask import Flask,render_template

# interaction
app =Flask(__name__)


# mapping
@app.route('/')

# inputs
def home():
    return render_template('index.html')

# main

if __name__=='__main__':
    app.run(debug=True)



