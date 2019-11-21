import os
import json


def write_json(dic, file):
    with open(file, 'w') as outfile:
        json.dump(dic, outfile)


def read_json(file):
    with open(file) as file_:
        config = json.load(file_)
    return config


if __name__ == "__main__":
    cfg = read_json(os.path.dirname(__file__) + "/config/config.json")
    dic = {'other': {'food': ['Sweet', 'Spicym', 'Sour']}}
    write_json(dic, os.path.dirname(__file__) + "/config/write.json")
    print(cfg)