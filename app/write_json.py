import json
import os.path

dirname = os.path.dirname(__file__)

##OutDated
##basepath = os.path.abspath(".")

dictionary = {
  "unitCode" : "placeholder",
  "unitName" : "placeoholder",
  "testNumber" : "placeholder",
  "questionNumber" : "placeholder",
  "prompt" : "placeholder",
  "answer" : "placeholder",
  "questionType": "placeholder",
  "totalOptions": ["1","2"]
}

#serialising json
json_object = json.dumps(dictionary, indent = 4)

with open(os.path.join(dirname,"questions/testing.json"), "w") as outfile:
  outfile.write(json_object)