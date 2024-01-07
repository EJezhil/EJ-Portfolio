# Flask App
import os
import smtplib

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


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

    # project_name = []
    # description = []
    # image_url = []
    # type = []
    # based_on = []
    # git_url = []
    # website_url = []
    # difficulty = []
    #
    # for i in new_list2[1:]:
    #     project_name.append(i[0])
    #     description.append(i[1])
    #     image_url.append(i[2])
    #     type.append(i[3])
    #     based_on.append(i[4])
    #     git_url.append(i[5])
    #     website_url.append(i[6])
    #     difficulty.append(i[7])

    # print(project_name)
    # print(description)
    # print(image_url)
    # print(type)
    # print(based_on)
    # print(git_url)
    # print(website_url)
    # print(difficulty)
    return render_template("index.html", data=new_list2)


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        datas = request.form
        send_email(datas["name"], datas["email"], datas["phone"], datas["message"])
        return render_template("contact.html", msg="Form submission successful!", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


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
    return render_template("resume.html")


if __name__ == "__main__":
    app.run(debug=True)
