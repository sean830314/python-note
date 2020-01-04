class Boy:
    def __init__(self, name):
        self.name = name

    def goout(self):
        return '{} go out'.format(self.name)

class Girl:
    def __init__(self, name):
        self.name = name

    def makeup(self):
        return '{} makeup'.format(self.name)

    def shower(self):
        return '{} taking a shower'.format(self.name)

    def goout(self):
        return '{} go out'.format(self.name)

class Adapter(object):
 
    def __init__(self, human):
        self.human = human
 
    def goout(self):
        return '{} , {}, {}'.format(self.human.makeup(), self.human.shower(), self.human.goout())

def main():
    objects = [Boy('Tom')]
    adapter = Adapter(Girl('Lisa'))
    objects.append(adapter)
    print(objects)
    for i in objects:
        print(i.goout())


if __name__ == "__main__":
    main()