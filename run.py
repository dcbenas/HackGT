from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
 
callers = {
    "+14047172917": "DrBowe",
    "+14049393387": "RiceConsumer",
    "+14438270802": "Nocturneinnine",
    "+17708823775": "Coolest Kid Alive",
}


@app.route("/", methods=['GET', 'POST'])

def hello_test():
    mess = request.values.get('Body', None)
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = mess
    else:
        message = "Unrecognized Number"
    resp = twilio.twiml.Response()
    resp.message(msg=message, to='+14049393387')
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
