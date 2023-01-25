import math
from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)

display = "0"
operation = ""
prevbutton = "zero"
numberA = float(0)
numberB = float(0)
digit_set = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
operation_set = set(["plus", "minus", "multiply", "divide"])

# Build button_set which includes digit_set and operation_set
button_set = set(["sign","point","clear","backspace","equals"])
button_set.update(digit_set)
button_set.update(operation_set)


# Base URL
@app.route("/",methods=["GET","POST"])
def index():
    global prevbutton
    button=""
    
    # Find out which button was pressed
    if request.method == "POST":
        for b in button_set:
            if request.form.get("button_"+b):
                button=b

    # Update display according to this button press
    update_display(button)
    prevbutton=button

    # Re-render html page
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
        if prevbutton=="equals" or prevbutton in operation_set:
            display="-0"
        else:
            if display!="NAN":
                display = "-" + display
            elif display[0] == "-":
                display = display[1:]
        
    
    elif button=="point":
        if prevbutton=="equals" or prevbutton in operation_set:
            display="0."
        else:
            if not "." in display and display!="NAN":
                display += "."

    elif button in operation_set:
        if prevbutton!="equals" and prevbutton not in operation_set:
            calculate()
        operation=button
        numberA=float(display)

    elif button=="clear":
        display = "0"
        operation = ""
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

    # If previous button is not "equals" get new numberB from display,
    # otherwise keep old numberB
    if prevbutton!="equals":
        numberB=float(display)

    # Perform operation to get new numberA
    if operation=="":
        numberA = float(display)
    elif operation == "plus":
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

    # Write new numberA to display
    display = format_number(numberA)



# Function for converting number to string to be written to display
def format_number(number: float) -> str:
    
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

    if display=="0" or prevbutton=="equals" or prevbutton in operation_set:
        display=digit
    elif display=="-0":
        display="-"+digit
    else:
        digit_count=0
        for d in range(0, 10):
            digit_count += display.count(str(d))   
        if digit_count<10:
            display+=digit



# Run the app, Debug=True should be changed before deployment
if __name__=="__main__":
    app.run(debug=True)