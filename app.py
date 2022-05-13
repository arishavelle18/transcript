from flask import Flask, redirect , render_template , request,redirect,jsonify
import speech_recognition as sr
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
    transcript=""
    if request.method == "POST":
        print("Data Recieve")
        # check the file
        if "file" not in request.files:
            return redirect(request.url)
        
        # hold the file value 
        file = request.files["file"]
        
        # check if is not wav file format
        if file.content_type != "audio/wav":
                return redirect(request.url)

        # check if the filename is empty
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data,key=None)
        

    return render_template("home.html",transcript=transcript)

@app.route("/realtime")
def realtime():
    return render_template("realtime.html")

@app.route('/process', methods=['POST'])
def process():
    print("hello")
    email = request.form['name']

    recognizer = sr.Recognizer()
    audioFile = sr.AudioFile(email)
    with audioFile as source:
        data = recognizer.record(source)
    transcript = recognizer.recognize_google(data,key=None)
    print(transcript)
    return jsonify({'data':'Missing data!'})



if __name__ == "__main__":
    app.run(debug=True,threaded=True)