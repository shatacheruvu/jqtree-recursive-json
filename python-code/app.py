import json
import sys


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

def reverse_read(data):
    ret = {}
    for item_list in data:
        if "children" in item_list:
            ret[item_list["name"]] = reverse_read(item_list["children"])
        else:
            if "---" in item_list["name"]:
                spl = item_list["name"].split("---")
                if len(spl) > 0:
                    ret[spl[0]] = spl[1]
    return ret

def read_base_json():
    with open("../samples/sample.json","r+") as f:
        data = json.load(f)
    parent = []
    args = sys.argv
    if len(args) == 1:
        print("send argument to transform or reverse -- 't' or 'r'")
        return
    if args[1] == "t":
        res = handle_dictionary(parent, data)
        print(json.dumps(res))
    elif args[1] == "r":
        res = reverse_read(data)
        print(json.dumps(res))
    else:
        print("invalid argument passed-- send 't' to transform or 'r' to reverse it")


read_base_json()


