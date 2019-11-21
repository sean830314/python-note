import os
import yaml


def write_yaml(dic, file):
    with open(file, 'w') as outfile:
        yaml.dump(dic, outfile, default_flow_style=False)


def read_yaml(file):
    with open(file) as file_:
        config = yaml.safe_load(file_)
    return config


if __name__ == "__main__":
    cfg = read_yaml(os.path.dirname(__file__) + "/config/config.yml")
    dic = {'other': {'food': ['Sweet', 'Spicym', 'Sour']}}
    write_yaml(dic, os.path.dirname(__file__) + "/config/write.yml")
    print(cfg)