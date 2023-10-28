from flask import Flask,render_template, request, jsonify
from chat import  get_response 
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")

@app.post("/predict")   
def predict():
    text=request.get_json().get("message")
    response=get_response(text)
    message={"answer": response}
    return jsonify(message)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    return render_template("chatbot.html")

@app.route("/search_recipe")
def search():
    return render_template("search.html")

@app.route("/get_recommendation")
def recommend():
    return render_template("GetRecom3.html")


if __name__ == "__main__":
    app.run(debug=True) 