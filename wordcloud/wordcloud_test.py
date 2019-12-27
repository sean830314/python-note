from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
from PIL import Image


def generate_wordcloud(data_str, stopwords, mask):
    wordcloud = WordCloud(width = 800, height = 800, max_font_size=100, min_font_size=10, max_words=200,
                          background_color='white', colormap="Oranges_r", contour_width=3, contour_color='steelblue',
                          stopwords=stopwords, mask=mask).generate(data_str)
    return wordcloud

if __name__ == "__main__":
    # read csv
    df = pd.read_csv(r"data/data.csv", encoding ="latin-1") 
    comment_words = ' '
    stopwords = set(STOPWORDS) 
    for val in df.CONTENT: 
        val = str(val) 
        tokens = val.split() 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
        for words in tokens: 
            comment_words = comment_words + words + ' '
    mask = np.array(Image.open("pic/mask.jpg"))
    wordcloud = generate_wordcloud(comment_words, stopwords, mask)
                  
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show() 

