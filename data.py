import requests

params = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean"
}
res = requests.get("https://opentdb.com/api.php", params)
res.raise_for_status()

res_json = res.json()


question_data = res_json["results"]
