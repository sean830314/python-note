
class Article:
    def __init__(self, aid, title):
        self.__aid = aid
        self.__title = title

    def get_aid(self):
        return self.__aid

    def set_aid(self, aid):
        self.__aid = aid

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title


if __name__ == "__main__":
    article = Article(1, "title1")
    print('aid: {}, title: {}'.format(article.get_aid(), article.get_title()))
    article.set_aid(2)
    article.set_title('title2')
    print('modirfy aid: {}, title: {}'.format(article.get_aid(), article.get_title()))