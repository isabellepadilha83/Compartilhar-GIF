from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = "P0yGJjhEGAq4dHtt0BbPvFSPtMUPck2T"

@app.route("/", methods=["GET", "POST"])
def index():
    gifs = []
    if request.method == "POST":
        query = request.form.get("query")
        url = "https://api.giphy.com/v1/gifs/search"
        params = {
            "api_key": GIPHY_API_KEY,
            "q": query,
            "limit": 5,
            "rating": "g"
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            gifs = [item["images"]["downsized_medium"]["url"] for item in data["data"]]
        else:
            print("Erro na API do Giphy:", response.status_code)

    return render_template("index.html", gifs=gifs)

if __name__ == "__main__":
    app.run(debug=True)
