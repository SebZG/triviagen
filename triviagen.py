import csv
import html

import requests

amount = input("Please enter the number of trivia questions you'd like to see: ")
difficulty = input(
    "Please specify how difficult you'd like the questions to be (easy/medium/hard): "
)
category = 18

url = "https://opentdb.com/api.php"

request_params = {"amount": amount, "difficulty": difficulty, "category": category}

response = requests.get(
    url, headers={"Accept": "application/json"}, params=request_params
)

data = response.json()["results"]

qna = [["Question", "Answer"]]

for item in data:
    q = html.unescape(item["question"])

    if item["type"] == "boolean":
        q = "True or False? " + q

    a = html.unescape(item["correct_answer"])

    qna.append([q, a])

with open("tech trivia.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(qna)
