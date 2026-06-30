from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("result",username=username))
    return render_template("index.html")

@app.route("/result")
def result():
    username = request.args.get("username")
    return render_template("result.html",username=username)

@app.errorhandler(404)
def page_mot_found(e):
    return "このページは存在しません。",404


if __name__ == "__main__":
    app.run(debug=True)