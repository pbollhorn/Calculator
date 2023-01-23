from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

display = "0"

# Base URL
@app.route("/",methods=["GET","POST"])
def index():
    button=""
    if request.method == "POST":
        if request.form.get("zero"):
            button="zero"
        if request.form.get("one"):
            button="one"
        if request.form.get("two"):
            button="two"
        if request.form.get("three"):
            button="three"
        if request.form.get("four"):
            button="four"
        if request.form.get("five"):
            button="five"
        if request.form.get("six"):
            button="six"
        if request.form.get("seven"):
            button="seven"
        if request.form.get("eight"):
            button="eight"
        if request.form.get("nine"):
            button="nine"
        if request.form.get("sign"):
            button="sign"
        if request.form.get("point"):
            button="point"
        if request.form.get("plus"):
            button="plus"
        if request.form.get("minus"):
            button="minus"
        if request.form.get("multiply"):
            button="multiply"
        if request.form.get("divide"):
            button="divide"
        if request.form.get("exponent"):
            button="exponent"
        if request.form.get("root"):
            button="root"
        if request.form.get("equals"):
            button="equals"
        if request.form.get("clear"):
            button="clear"
        if request.form.get("backspace"):
            button="backspace"
    update_display(button)
    return render_template("index.html",display=display)
        


def update_display(button):
    global display

    # Convert 0 to empty string
    if display=="0":
        display=""

    # Do action depending on button
    if button=="zero":
        display += "0"
    
    elif button=="one":
        display += "1"
    
    elif button=="two":
        display += "2"
    
    elif button=="three":
        display += "3"
    
    elif button=="four":
        display += "4"
    
    elif button=="five":
        display += "5"
    
    elif button=="six":
        display += "6"
    
    elif button=="seven":
        display += "7"
    
    elif button=="eight":
        display += "8"
    
    elif button=="nine":
        display += "9"
    
    elif button=="sign":
        if len(display)>0:
            if display[0] == "-":
                display = display[1:]
            else:
                display = "-" + display
    
    elif button=="point":
        if not "." in display:
            display += "."

    elif button=="clear":
        display=""
    
    elif button=="backspace":
        display = display[:-1]

    # Convert empty string to 0
    if display=="":
        display="0"


if __name__=="__main__":
    app.run(debug=True) # Debug=True should be changed before deployment




