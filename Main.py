
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

# function to process calculation


def Calculate():

    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    choice = str(request.form["choice"])
    
    if(choice == '+'):
        return str(num1 + num2)
    elif(choice == '-'):
        return str(num1 - num2)
    elif(choice == '*'):
        return str(num1 * num2)
    elif(choice == '/'):

        try:
            return str(num1 / num2)
        except Exception as e:
            return str(e)

    elif(choice == '%'):
        try:
            return str(num1 / num2)
        except Exception as e:
            return str(e)

    else:
        pass


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":

        return render_template("Output.html", Solution = Calculate())

    return render_template("Input Form.html")
