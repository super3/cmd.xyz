#!/usr/bin/env python
import sys
import openai
from config import *
openai.api_key = api_key

prompt = """
Q: list files in a directory
> ls

Q: delete a file named bar.txt
> rm bar.txt

Q: create a new directory named foo
> mkdir foo

Q: create a file named test.txt with the colors of the rainbow
> echo "red orange yellow green blue indigo violet" > test.txt

"""

from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    usr_prompt = prompt + "Q: " + request.args.get("input", "")
    response = openai.Completion.create(engine="davinci", prompt=usr_prompt, temperature=0, stop="\n\n")
    print(usr_prompt, response.choices[0].text)

    res = jsonify({"output": response.choices[0].text})
    res.headers.add('Access-Control-Allow-Origin', '*')

    return res
