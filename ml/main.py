from flask import Flask, request
import nlp_search as nl

app = Flask(__name__)


@app.route("/get_nlp_search", methods=['POST'])
def nlp_search():
    if request.method == 'POST':
        text = request.json["text"]
        a = nl.NLP_Search(text).search_all()
        return a


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
