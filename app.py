# Mini version of a real fraud detection system
# using flask because it is beginner friendly and easy to use

from flask import Flask, render_template, request

app = Flask(__name__)           #flask app object (creates a local web server)

@app.route('/')                 #decorator (a function that shows the home page)
def home():                     #home function (displays the home page)
    return render_template('index.html')

@app.route('/check', methods=['POST'])   #when 'check' is pressed, data is sent here
def check_fraud():                       #checks if the transaction is fraudulent
    amount = float(request.form['amount'])
    user_id = request.form['user_id']

    if amount > 1000000:
        result = "FRAUD DETECTED"
    else:
        result = "SAFE TRANSACTION"
    return render_template('index.html', result=result) #displays the result on the home page

if __name__ == '__main__':
    app.run(debug=True)