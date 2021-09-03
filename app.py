from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename
import os
import subprocess
from flask_ngrok import run_with_ngrok
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
run_with_ngrok(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedBack.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class feedBack(db.Model):
  id = db.Column(db.Integer,  primary_key=True)
  text = db.Column(db.Text)
  name = db.Column(db.Text)
  email = db.Column(db.Text)

  def __init(self, text, name, mail):
    self.text = text
    self.name = name
    self.mail = mail

uploads_dir = os.path.join(app.instance_path, 'uploads')

get_direct = "static/"

os.makedirs(uploads_dir, exist_ok=True)

''' @app.route("/")
def predict():
    return render_template('index.html')
 '''

@app.route("/", methods=['GET','POST'])
def predict():
    if not request.method == "POST":
        return render_template("index.html")
    formid = request.args.get('formid', 1, type=int)
    if formid == 1:
        video = request.files['file']
        video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
        print(video)
        subprocess.run("ls")
        subprocess.run(['python3', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    #obj = secure_filename(video.filename)
    #return obj
        return render_template("index.html", source=url_for(os.path.join(get_direct, secure_filename(video.filename))) )

    if formid == 2:
        name = request.form.get("y")
        email = request.form.get("x")
        text = request.form.get("z")

        if name == '': 
          return render_template("index.html", text="you forgot your name :(", color="red", scrollToAnchor="feed-back");
        elif text == '':
          return render_template("index.html", text="you forgot your opinion :(", color="red", scrollToAnchor="feed-back");
        elif email == '':
          return render_template("index.html", text="you forgot your email :(", color="red", scrollToAnchor="feed-back");
        else:
          feed_back = feedBack(name=name, email=email, text=text)
          db.session.add(feed_back)
          db.session.commit()

          t="thnx for the feed-back :)"
          return render_template("index.html", text=t, color="lime", scrollToAnchor="feed-back");    
#@app.route('/return-files', methods=['GET'])
#def return_file():
#    obj = request.args.get('obj')
#    loc = os.path.join("runs/detect", obj)
#    print(loc)
#    try:
#        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
#        # return send_from_directory(loc, obj)
#    except Exception as e:
#        return str(e)

# @app.route('/display/<filename>')
# def display_video(filename):
# 	#print('display_video filename: ' + filename)
# 	return redirect(url_for('static/video_1.mp4', code=200))

if __name__ == "__main__":
    db.create_all()
    app.run()
