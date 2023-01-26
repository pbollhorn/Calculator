from flask import Flask,redirect,url_for,render_template,request
import calculator

app=Flask(__name__)









calculator.reset(True)





# Base URL
@app.route("/",methods=["GET","POST"])
def index():

    button=""
    
    # Find out which button was pressed
    if request.method == "POST":
        for b in calculator.button_set:
            if request.form.get("button_"+b):
                button=b

    # Update display according to this button press
    calculator.update_display(button)
    calculator.prev_button=button

    # Re-render html page
    return render_template("index.html",display_string=calculator.display)
        






# Run the app, Debug=True should be changed before deployment
if __name__=="__main__":
    app.run(debug=True)