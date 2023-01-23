from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

# Base URL
@app.route("/",methods=["POST","GET"])
def index():
    display="0"
    if request.method == "POST":
        if "five" in request.form:
            display="5"        
    return render_template("index.html",display=display)
        

if __name__=="__main__":
    app.run(debug=True) # Debug=True should be changed before deployment