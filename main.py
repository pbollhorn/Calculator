from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

display = "0"
numberA = float(0)
numberB = float(0)
operation = ""

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
    return render_template("index.html",display_string=display)
        


def update_display(button):
    global display

    # Do action depending on button
    if button=="zero":
        insert_digit("0")
    
    elif button=="one":
        insert_digit("1")
    
    elif button=="two":
        insert_digit("2")
    
    elif button=="three":
        insert_digit("3")
    
    elif button=="four":
        insert_digit("4")
    
    elif button=="five":
        insert_digit("5")
    
    elif button=="six":
        insert_digit("6")
    
    elif button=="seven":
        insert_digit("7")
    
    elif button=="eight":
        insert_digit("8")
    
    elif button=="nine":
        insert_digit("9")
    
    elif button=="sign":
        if display[0] == "-":
            display = display[1:]
        elif display!="0":
            display = "-" + display
    
    elif button=="point":
        if not "." in display:
            display += "."

    elif button=="plus":
        numberA=float(display)
        display="0"
        print(numberA)

    elif button=="clear":
        display="0"
    
    elif button=="backspace":
        display = display[:-1]
        if len(display)==0 or display=="-0" or display=="-":
            display="0"



def insert_digit(digit):
    global display
    if display=="0":
        display=digit
    else:
        digit_count=0
        for d in range(0, 9):
            digit_count += display.count(str(d))    
        if digit_count<10:
            display+=digit


if __name__=="__main__":
    app.run(debug=True) # Debug=True should be changed before deployment




