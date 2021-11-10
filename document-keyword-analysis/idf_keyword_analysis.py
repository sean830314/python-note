from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import json 
from os import walk
from os.path import join
import numpy as np
import nltk
nltk.download('stopwords')


def read_webtool_contents(data_path="data"):
    documents = list()
    documents_name = list()
    for root, dirs, files in walk(data_path):
        for f in files:
            fullpath = join(root, f)
            print("loading", fullpath)
            with open(fullpath,encoding="utf-8") as file:
                document = json.load(file)
                documents.append(" ".join(document["data"]).replace("\r\n", " "))
                documents_name.append(fullpath)
    return documents, documents_name

def calculate_BKStatement_socre(corpus, documents_name):
    bank_account_keywords = ["customer", "periods", "account", "statement", "balance", "bank", "description", "deposit", "deposits", "payment", "branch", "amount", "transaction", "transactions", "credit", "details", "total"]
    for document, document_name in zip(corpus, documents_name):
        matche_words = [x for x in document.lower().split() if x in bank_account_keywords]
        score = len(list(set(matche_words)))*3
        print("document name: {} , and score: {}".format(document_name, score))

if __name__ == "__main__":
    corpus, documents_name = read_webtool_contents("data/bank_statement_document")
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    words = vectorizer.get_feature_names()
    weight = tfidf.toarray() # element a[i][j] indicates the tf-idf weight of j word in i document
    for i in range(len(weight)):
        print(u"-------document",i,u"tf-idf score------")
        print([words[index] for index in np.array(weight[i].argsort()[-3:][::-1])])
    data = pd.DataFrame([transformer.idf_]).values.tolist()
    nltk_stopwords = nltk.corpus.stopwords.words('english')
    print("pick idf keywords: \n",[words[index] for index in np.array(np.array(data[0]).argsort()[:100][::-1]) if not words[index].isdigit() and words[index] not in nltk_stopwords])
    calculate_BKStatement_socre(corpus, documents_name)