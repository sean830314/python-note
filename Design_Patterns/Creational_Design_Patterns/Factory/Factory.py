import json
import yaml
import toml
import os

#Product
class Writter:
    def write():
        pass

#ConcreteProduct
class JsonWritter(Writter):
    def __init__(self, file):
        self._file = file

    def write(self, data):
        with open(self._file, 'w') as fp:
            d = json.dumps(data)
            fp.write(d)

#ConcreteProduct
class YamlWritter(Writter):
    def __init__(self, file):
        self._file = file

    def write(self, data):
        with open(self._file, 'w') as fp:
            d = yaml.dump(data)
            fp.write(d)

#ConcreteProduct
class TomlWritter(Writter):
    def __init__(self, file):
        self._file = file

    def write(self, data):
        with open(self._file, 'w') as f:
            r = toml.dump(data, f)
            print(r)

#Product
class Reader:
    def read():
        pass

#ConcreteProduct
class JsonReader(Reader):
    def __init__(self, file):
        self._file = file

    def read(self):
        data = None
        with open(self._file, 'r') as reader:
            data = json.loads(reader.read())
        return data

#ConcreteProduct
class YamlReader(Reader):
    def __init__(self, file):
        self._file = file

    def read(self):
        with open(self._file, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data

#ConcreteProduct
class TomlReader(Reader):
    def __init__(self, file):
        self._file = file

    def read(self):
        data = toml.load(self._file)
        return data

#ConcreteFactory
class ReaderFactory:
    def new_reader(file):
        if file.find(".json") != -1:
            return JsonReader(file)
        elif file.find(".yaml") != -1:
            return YamlReader(file)
        elif file.find(".toml") != -1:
            return TomlReader(file)

#ConcreteFactory
class WritterFactory:
    def new_writter(file):
        if file.find(".json") != -1:
            return JsonWritter(file)
        elif file.find(".yaml") != -1:
            return YamlWritter(file)
        elif file.find(".toml") != -1:
            return TomlWritter(file)
#Factory
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
    """
    工廠模式

        今天要介紹的工廠模式，
        其實概念非常的簡單，
        在其中主要的角色只有兩個商品和工廠，

        真的只有這麼簡單嗎？其實有一些隱藏在背後的東西...

        當我們在使用工廠模式時，
        你跟工廠說你想要的那種規格的商品，
        而工廠負責製造你想要的那種規格的商品，
        當中可能需要某些組裝或是特殊步驟，
        但是作為消費者你不知道這些組裝方式和步驟，
        你還是可以買到你想要的東西。
    
    定義
        工廠方法模式( Factory Method )，定義一個用於建立物品的介面，讓子類決定實體化哪一個類別。工廠方法使一個類別的實例化延遲到其子類別。
    """
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
