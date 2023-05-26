# questions database: https://opentdb.com/ (click API to get the URL and then get data in that URL)
# question_data = [
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
#     {
#         "category": "General Knowledge",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "Coca-Cola&#039;s original colour was green.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
# ]

# ------------------------
import requests

parameters = {"amount": 10, "category": 18, "type": "boolean"}
response = requests.get("https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()  # raise an HTTPError if the HTTP request returned an unsuccessful status code.

data = response.json()  # get the json data
question_data = data["results"]  # this will give list of question dicts
print(question_data)
