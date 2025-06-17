from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    player = request.json["choice"]
    options = ["Schere", "Stein", "Papier"]
    computer = random.choice(options)

    if player == computer:
        result = "Unentschieden!"
    elif (player == "Schere" and computer == "Papier") or \
         (player == "Stein" and computer == "Schere") or \
         (player == "Papier" and computer == "Stein"):
        result = f"Du gewinnst mit {player} gegen {computer}!"
    else:
        result = f"Der Computer gewinnt mit {computer} gegen {player}."

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
