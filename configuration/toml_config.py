import os
import toml


def write_toml(dic, file):
    with open(file, 'w') as outfile:
        toml.dump(dic, outfile)


def read_toml(file):
    with open(file) as file_:
        config = toml.load(file_)
    return config


if __name__ == "__main__":
    cfg = read_toml(os.path.dirname(__file__) + "/config/config.toml")
    dic = {'other': {'food': ['Sweet', 'Spicym', 'Sour']}}
    write_toml(dic, os.path.dirname(__file__) + "/config/write.toml")
    print(cfg)