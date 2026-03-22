from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

import os
my_api_key_gemini = "AIzaSyDZNvGVtuW2plBTIXZ00vbs-2X9Ips7Azg"

genai.configure(api_key=my_api_key_gemini)

model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

# Define your 404 error handler to redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt

            system_prompt = "You are Heidi AI, a helpful and intelligent assistant created by Aryan Bunkar. Answer all questions helpfully and clearly. "
            response = model.generate_content(system_prompt + question)

            if response.text:
                return response.text
            else:
                return "Sorry, Heidi AI could not answer that. Please try again!"
        except Exception as e:
            return "Sorry, Heidi AI encountered an error. Please try again!"

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
