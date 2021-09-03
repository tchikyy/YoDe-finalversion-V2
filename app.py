from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename
import os
import subprocess
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return
    formid = request.args.get('formid', 1, type=int)
    if formid == 1:
        video = request.files['video']
        video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
        print(video)
        subprocess.run("ls")
        subprocess.run(['python3', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    #obj = secure_filename(video.filename)
    #return obj
        return render_template("index.html", source=os.path.join(uploads_dir, secure_filename(video.filename)))

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
    app.run()
