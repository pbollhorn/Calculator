import math
from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)

display = "0"
operation = "plus"
prevbutton = "zero"
numberA = float(0)
numberB = float(0)
digit_set = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
operations_set = set(["plus", "minus", "multiply", "divide", "exponent", "root"])


# Base URL
@app.route("/",methods=["GET","POST"])
def index():
    global prevbutton
    button=""
    if request.method == "POST":
        if request.form.get("zero"):
            button="0"
        if request.form.get("one"):
            button="1"
        if request.form.get("two"):
            button="2"
        if request.form.get("three"):
            button="3"
        if request.form.get("four"):
            button="4"
        if request.form.get("five"):
            button="5"
        if request.form.get("six"):
            button="6"
        if request.form.get("seven"):
            button="7"
        if request.form.get("eight"):
            button="8"
        if request.form.get("nine"):
            button="9"
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
        if request.form.get("clear"):
            button="clear"
        if request.form.get("backspace"):
            button="backspace"
        if request.form.get("equals"):
            button="equals"
    update_display(button)
    prevbutton=button
    return render_template("index.html",display_string=display)
        


def update_display(button):
    global display
    global operation
    global prevbutton
    global numberA
    global numberB

    # Do action depending on button
    if button in digit_set:
        insert_digit(button)
    
    elif button=="sign":
        if display[0] == "-":
            display = display[1:]
        elif display!="0":
            display = "-" + display
    
    elif button=="point":
        if not "." in display:
            display += "."

    elif button in operations_set:
        if prevbutton!="equals" and prevbutton not in operations_set:
            calculate()
        operation=button
        numberA=float(display)

    elif button=="clear":
        display = "0"
        operation = "plus"
        prevbutton = "zero"
        numberA = float(0)
        numberB = float(0)
    
    elif button=="backspace":
        display = display[:-1]
        if len(display)==0 or display=="-0" or display=="-":
            display="0"

    elif button=="equals":
        calculate()




def calculate():
    global display
    global prevbutton
    global numberA
    global numberB

    # If previous button is "equals" keep old numberB, else get new numberB from display
    if prevbutton=="equals":
        pass
    else:
        numberB=float(display)

    # Perform operation to get new numberA
    if operation == "plus":
        numberA = numberA + numberB
    elif operation == "minus":
        numberA = numberA - numberB
    elif operation == "multiply":
        numberA = numberA * numberB
    elif operation == "divide":
        if numberB==0:
            numberA=float("NAN")
        else:
            numberA = numberA / numberB
    elif operation == "exponent":
        numberA = numberA ** numberB
    elif operation == "root":
        numberA = numberB ** (1/numberA)

    # Write new numberA to display
    display = format_display(numberA)



# Function for converting number to string to be written to display
def format_display(number: float) -> str:
    
    # Return NAN in case of overflow
    if number > 9999999999 or number < -9999999999:
        return "NAN"

    # Number of digits before point
    if abs(number) >= 1:
        digits_before = int(math.log10(abs(number)))+1
    else:
        digits_before = 1

    # Number of digits after point (10 digits allowed in total)
    digits_after = 10 - digits_before

    # Format number as string with fixed number of digits after point
    string = ("{:." + str(digits_after) + "F}").format(number)

    # Remove trailing zeros after point
    if string.find(".")!=-1:
        while string[-1]=="0":
            string = string[:-1]

    # Remove trailing point
    if string[-1]==".":
        string = string[:-1]

    # Convert "-0" to 0
    if string=="-0":
        string="0"

    # Return the string
    return string






def insert_digit(digit):
    global display
    global prevbutton

    if display=="0" or prevbutton in operations_set:
        display=digit
    else:
        digit_count=0
        for d in range(0, 10):
            digit_count += display.count(str(d))   
        if digit_count<10:
            display+=digit



# Run the app, Debug=True should be changed before deployment
if __name__=="__main__":
    app.run(debug=True)