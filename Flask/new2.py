from flask import Flask, render_template
import os

# Interaction
app = Flask(__name__)

picfolder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = picfolder

# Mapping
@app.route('/')
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'waterfall.webp')
    return render_template("home.html", user_image=pic)

# Mapping
@app.route('/second')
def second():
    return render_template("second.html")

# Main
if __name__ == '__main__':
    app.run(debug=True)