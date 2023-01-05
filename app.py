import os

import openai
from flask import Flask, redirect, render_template, request, url_for

from pydantic import BaseSettings

from generate_flashcards import get_gpt3_output, output_to_text

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI API key
class Settings(BaseSettings):
    OPENAI_API_KEY: str = 'OPENAI_API_KEY'

    class Config:
        env_file = '.env'

settings = Settings()
openai.api_key = settings.OPENAI_API_KEY


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input = request.form["input"]
        response = get_gpt3_output(input, max_token_relative=False, model_name="text-davinci-003")
        result=output_to_text(response.choices[0].text)
        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    return render_template("index.html", result=result)

