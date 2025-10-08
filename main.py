from flask import Flask, render_template, request, redirect, session
import requests
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET'])
def home():
    try:
        return render_template("index.html")

    except requests.exceptions.RequestException as e:
        return f"<p>халепа з апі: {str(e)}</p>"

@app.route("/facts", methods=["GET"])
def facts_():
    try:
        with open("C:/Users/Максим/OneDrive/Dokumenty/python/Flask/Fin pojeckt/json_files/facts.json", "r", encoding="utf-8") as f:
            facts_list = json.load(f)
        return render_template("facts.html", fact_list=facts_list)
    except requests.exceptions.RequestException as e:
        return f"<p>Помилка: {str(e)}</p>"


@app.route("/contacts", methods=["GET"])
def contacts():

    return render_template("contacts.html")

@app.route("/info", methods=["GET"])
def info():

    return render_template("info.html")



if __name__ == '__main__':

    app.run(debug=True, port=5002)
