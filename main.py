from endpoints.ai import AI
from flask import Flask, render_template, jsonify, request

client = Flask(__name__)
ai = AI(api="") # gemini api key . 


@client.route('/', methods=['GET', 'POST'])
def home():
    resp = "Hi!!"  
    if request.method == 'POST':
        text = request.form.get('text')
        resp = ai.generate(text)  
        print(resp)
    return render_template('index.html', response=resp)



if __name__ == '__main__':
    client.run(debug=True)
