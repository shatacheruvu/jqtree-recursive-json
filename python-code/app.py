import json

def createNamedDict(parent, key,val):
    rtmp = {}
    if type(val) is dict:
        rtmp["name"] = key
        rtmp["children"] = []
    else:
        rtmp["name"] = key+"---"+val
    parent.append(rtmp)
    return parent

def handle_dictionary(parent, data):
    counter = 0
    for keys, vals in data.items():
        parent = createNamedDict(parent, keys, vals)
        if type(vals) is dict:
            parent_n = parent[counter]["children"]
            tmp_parent = handle_dictionary(parent_n,vals)
            parent[counter]["children"] = tmp_parent
        counter = counter + 1
    return parent

def read_base_json():
    with open("samples/sample.json","r+") as f:
        data = json.load(f)
    parent = []
    res = handle_dictionary(parent, data)
    print(json.dumps(res))

read_base_json()
