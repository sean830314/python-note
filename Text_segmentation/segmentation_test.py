import jieba
import jieba.analyse
import jieba.posseg as pseg
jieba.set_dictionary('dict/dict.txt.big.txt')
Text = "我驕傲的破壞 我痛恨的平凡 才想起那些是我最愛\
讓盛夏去貪玩 把殘酷的未來 狂放到光年外 而現在\
放棄規則 放縱去愛 放肆自己 放空未來\
我不轉彎 我不轉彎 我不轉彎 我不轉彎\
讓定律更簡單 讓秩序更混亂 這樣的青春我才喜歡\
讓盛夏去貪玩 把殘酷的未來 狂放到光年外 而現在\
放棄規則 放縱去愛 放肆自己 放空未來\
我不轉彎 我不轉彎 我不轉彎 我不轉彎\
我要 我瘋 我要 我愛 就是 我要 我瘋 我要 我愛 現在\
一萬首的mp3 一萬次瘋狂的愛 滅不了一個渺小的孤單\
我要 我瘋 我要 我愛 就是 我要 我瘋 我要 我愛 現在\
盛夏的一場狂歡 來到了光年之外 長大難道是人必經的潰爛\
放棄規則 放縱去愛 放肆自己 放空未來\
我不轉彎 我不轉彎 我不轉彎 我不轉彎"
def remove_stop_words(file_name,seg_list):
    with open(file_name,'r', encoding="utf-8") as f:
        stop_words = f.readlines()
    stop_words = [stop_word.rstrip() for stop_word in stop_words]
    new_list = []
    
    for seg in seg_list:
        if seg not in stop_words:
            new_list.append(seg)
    return new_list
seg_list = jieba.lcut(Text, cut_all=True)    # Full Mode
print('Full Mode: ',seg_list)
seg_list = jieba.lcut(Text, cut_all=False)
print("Default Mode: ",seg_list) # Default Mode
seg_list = remove_stop_words('dict/stopword.txt',seg_list) # remove stop words
print("remove stop words: ",seg_list)

words = pseg.cut(Text) # word tagging
print("word tagging")
for word, flag in words:
    print('%s %s' % (word, flag))

print("jieba tf-idf")
for x, w in jieba.analyse.extract_tags(Text, withWeight=True):
    print('%s %s' % (x, w))
print("jieba text rank")
for x, w in jieba.analyse.textrank(Text, withWeight=True):
    print('%s %s' % (x, w))