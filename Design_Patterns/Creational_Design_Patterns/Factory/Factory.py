import json
import yaml
import toml
import os


class Writter:
    def write():
        pass


class JsonWritter(Writter):
    def __init__(self, file):
        self._file = file

    def write(self, data):
        with open(self._file, 'w') as fp:
            d = json.dumps(data)
            fp.write(d)


class YamlWritter(Writter):
    def __init__(self, file):
        self._file = file

    def write(self, data):
        with open(self._file, 'w') as fp:
            d = yaml.dump(data)
            fp.write(d)


class TomlWritter(Writter):
    def __init__(self, file):
        self._file = file

    def write(self, data):
        with open(self._file, 'w') as f:
            r = toml.dump(data, f)
            print(r)


class Reader:
    def read():
        pass


class JsonReader(Reader):
    def __init__(self, file):
        self._file = file

    def read(self):
        data = None
        with open(self._file, 'r') as reader:
            data = json.loads(reader.read())
        return data


class YamlReader(Reader):
    def __init__(self, file):
        self._file = file

    def read(self):
        with open(self._file, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data


class TomlReader(Reader):
    def __init__(self, file):
        self._file = file

    def read(self):
        data = toml.load(self._file)
        return data


class ReaderFactory:
    def new_reader(file):
        if file.find(".json") != -1:
            return JsonReader(file)
        elif file.find(".yaml") != -1:
            return YamlReader(file)
        elif file.find(".toml") != -1:
            return TomlReader(file)


class WritterFactory:
    def new_writter(file):
        if file.find(".json") != -1:
            return JsonWritter(file)
        elif file.find(".yaml") != -1:
            return YamlWritter(file)
        elif file.find(".toml") != -1:
            return TomlWritter(file)

class ReaderAndWritterFactory:
    def create_reader_and_writter(self, read_file, write_file):
        self.reader = ReaderFactory.new_reader(read_file)
        self.writter = WritterFactory.new_writter(write_file)
    def setting(self, key):
        data = self.reader.read()
        data['write'] = key
        self.writter.write(data)
def main():
    read_file_name = os.path.dirname(os.path.abspath(__file__))+"/config/config.yaml"
    write_file_name = os.path.dirname(os.path.abspath(__file__))+"/config/write.yaml"
    f = ReaderAndWritterFactory()
    f.create_reader_and_writter(read_file_name, write_file_name)
    f.setting("test_key")
if __name__ == '__main__':
    main()
"""
file_name = os.path.dirname(os.path.abspath(__file__))+"/config/config.yaml"
reader = ReaderFactory.new_reader(file_name)
data = reader.read()
write_file_name = os.path.dirname(os.path.abspath(__file__))+"/config/write.yaml"
data['write'] = "writter"
writter = WritterFactory.new_writter(write_file_name)
writter.write(data)
"""
