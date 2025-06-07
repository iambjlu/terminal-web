from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        command = request.form.get("command")
        try:
            output = command+("\n\n")+subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            output = e.output
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)