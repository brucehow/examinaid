import json

dictionary = {
  "unitCode" : "placeholder",
  "prompt" : "placeholder",
  "answer" : "placeholder",
  "questionType": "placeholder",
  "totalOptions": ["1","2"]
}

#serialising json
json_object = json.dumps(dictionary, indent = 4)

with open("sample.json", "w") as outfile:
  outfile.write(json_object)