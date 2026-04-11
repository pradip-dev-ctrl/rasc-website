from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb+srv://pradipmahato8389045671_db_user:yk7Ihvp1q4oWZhzt@cluster0.jpoxryo.mongodb.net/")
db = client["rasc_db"]

# ================= CONTACT =================

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json

    db["contacts"].insert_one({
        "name": data.get("name"),
        "email": data.get("email"),
        "message": data.get("message")
    })

    return jsonify({"message": "Message saved successfully!"})


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = list(db["contacts"].find({}, {"_id": 0}))
    return jsonify(messages)


# ================= EVENTS =================

@app.route('/add-event', methods=['POST'])
def add_event():
    data = request.json

    db["events"].insert_one({
        "title": data.get("title"),
        "date": data.get("date"),
        "video": data.get("video")   # NEW
    })

    return jsonify({"message": "Event added successfully"})








# ================= DEBATES =================

@app.route('/add-debate', methods=['POST'])
def add_debate():
    data = request.json

    db["debates"].insert_one({
        "title": data.get("title"),
        "date": data.get("date"),
        "video":data.get("video")
    })

    return jsonify({"message": "Debate added successfully"})


@app.route('/get-debates', methods=['GET'])
def get_debates():
    debates = list(db["debates"].find({}, {"_id": 0}))
    return jsonify(debates)
# ================= ARTICLES =================

@app.route('/add-article', methods=['POST'])
def add_article():
    data = request.json

    db["articles"].insert_one({
        "title": data.get("title"),
        "content": data.get("content")
    })

    return jsonify({"message": "Article added successfully"})


@app.route('/get-articles', methods=['GET'])
def get_articles():
    articles = list(db["articles"].find({}, {"_id": 0}))
    return jsonify(articles)


# ================= PODCAST =================

@app.route('/add-podcast', methods=['POST'])
def add_podcast():
    data = request.json

    db["podcasts"].insert_one({
        "title": data.get("title"),
        "link": data.get("link")
    })

    return jsonify({"message": "Podcast added successfully"})


@app.route('/get-podcasts', methods=['GET'])
def get_podcasts():
    podcasts = list(db["podcasts"].find({}, {"_id": 0}))
    return jsonify(podcasts)
# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True)
