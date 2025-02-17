import json
with open("score.json") as json_file:
    data = json.load(json_file)
    for p in data["people"]:
        print("name:" + p["name"])
        print("website:" + p["website"])
        print("from:" + p["from"])
        print("")