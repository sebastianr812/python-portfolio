
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    with open('./database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        body = data['body']

        file = database.write(f'\n{email},{subject},{body}')


def write_to_csv(data):
    with open('./database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        body = data['body']

        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, body])


@app.route("/")
def hello_world():
    return render_template('./index.html')


@app.route("/<string:page_name>")
def render_html(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank-you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrongooo'
