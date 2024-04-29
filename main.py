# Flask App
import datetime
import os
import smtplib

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

today = datetime.datetime.now()
year = today.year


@app.route('/')
def index():
    with open("Python Projects Portfolio Details.csv", 'r') as file:
        content = file.readlines()

    new_list = []
    for i in content:
        i = i.replace("\n", "")
        i = i.split(", ")
        new_list.append(i)

    new_list2 = []
    for i in new_list:
        for j in i:
            j = j.split(",")
            new_list2.append(j)

    return render_template("index.html", data=new_list2,year= year)


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html",year= year)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        datas = request.form
        send_email(datas["name"], datas["email"], datas["phone"], datas["message"])
        return render_template("contact.html", msg="Form submission successful!", msg_sent=True,year= year)
    return render_template("contact.html", msg_sent=False,year= year)


def send_email(name, email, phone, message):
    username = os.environ.get('email')
    password = os.environ.get('password')
    email_message = f"Subject:Form Data Message\n\nHi Ej,\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    print(email_message)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=email, to_addrs=username,
                            msg=email_message.encode('utf-8'))
        print("Mail sent")


@app.route('/resume', methods=["GET", "POST"])
def resume():
    return render_template("resume.html",year= year)


if __name__ == "__main__":
    app.run(debug=True)


