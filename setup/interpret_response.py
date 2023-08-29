import fileinput
import json

json_string = ''

for line in fileinput.input():
    json_string = json_string + line

json_obj = json.loads(json_string)

canon_obj = {}

canon_obj["response"] = json_obj["nl_response"]
canon_obj["confidence"] = json_obj["confidence_score"]
canon_obj["sql"] = json_obj["sql_query"]

canon_str = json.dumps(canon_obj)
print(canon_str)