class Article:
    def __init__(self, aid, title):
        self.__aid = aid
        self.__title = title

    @property
    def aid(self):
        return self.__aid

    @aid.setter
    def aid(self, aid):
        self.__aid = aid

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title


if __name__ == "__main__":
    article = Article(1, "title1")
    print('aid: {}, title: {}'.format(article.aid, article.title))
    article.aid = 2
    article.title = 'title2'
    print('modirfy aid: {}, title: {}'.format(article.aid, article.title))