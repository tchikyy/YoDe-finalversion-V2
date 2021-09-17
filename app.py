from flask import Flask, render_template, request, url_for
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


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

uploads_dir = os.path.join(app.instance_path, 'uploads')

get_direct = "static/"

os.makedirs(uploads_dir, exist_ok=True)
app.secret_key = "webApp"

@app.route("/", methods=['GET','POST'])
def predict():
    if not request.method == "POST":
        return render_template("index.html", check="checked")
    formid = request.args.get('formid', 1, type=int)
    if formid == 1:
        tt=""
        video = request.files['file']
        video.save(os.path.join(uploads_dir, secure_filename(video.filename)))

        option = request.form['select']
        print(option)
        
        s=0
        m=0
        l=0
        if option == 'yolov5m':
          m=1
          weight = "bestm.pt"
        elif option =='yolov5l':
          l=1
          weight = "bestl.pt"
        else:
          s=1
          weight = "best.pt"

        subprocess.run(['python3', 'detect.py','--weights', weight,'--source' , os.path.join(uploads_dir, video.filename),'--imgsz', '416','--line-thickness', '3'])
        if video.mimetype == "video/mp4":
          tt = "sorry can't display the video but"
        
        if s == 1:
          Check = 'checked'
          Check2 = ''
          Check3 = ''
        elif m == 1:
          Check = ''
          Check2 = 'checked'
          Check3 = ''
        elif l == 1:
          Check = ''
          Check2 = ''
          Check3 = 'checked'

        return render_template("index.html", scrollToAnchor="seconde", source=url_for('static', filename=video.filename), hreff="static/"+video.filename, download_text="Download", ttt= tt, check=Check, check2=Check2, check3=Check3 )

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
    if formid == 3:
        subprocess.run(['python3', 'detect.py','--weights', 'best.pt','--source' , '0','--imgsz', '416','--line-thickness', '3'])
        return render_template("index.html")

if __name__ == "__main__":
    db.create_all()
    app.run()
