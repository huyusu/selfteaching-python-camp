def stats_text_en(string):
   """
      1/ Counts the number of occurrences of each word in the parameter;
      2/ Returns an array in descending order of word frequency.
   """
   symbol_deleting_en = [',','.','!','-','*']
   for x in symbol_deleting_en:
      string = string.replace(x,'')
   string = string.lower()
   string = string.split()
   stats = dict([(word,string.count(word)) for word in string])
   stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
   return stats

# 1.2 封装统计中文汉字字频的函数
def stats_text_cn(string):
   """
      1/ Counts the number of occurrences of each character in the parameter;
      2/ Returns an array in descending order of character frequency.
   """
   symbol_deleting_cn = ['~','！',"?","…",'，','。','：',"—","”","“"," ","「","」","\n"]
   for x in symbol_deleting_cn:
      string = string.replace(x,'')
   string = [character for character in string]
   stats = dict([(character,string.count(character)) for character in string])
   stats = sorted(stats.items(),key=lambda item:item[1],reverse=1)
   return stats

# 1.3 对中英文混杂的字符串进行再分类
def Reclassify_cn(string):
   """ Pick out Chinese characters in the string ”text“. """
   string_cn = string[:string.find("How")]
   return string_cn

def Reclassify_en(string):
   """ Pick out English words in the string ”text“. """
   string_en = string[string.find("How"):]
   return string_en


# 1.4 将统计中文字频和英文词频的函数封装为一个函数
def stats_text(string):
   """
      1/ Reclassify the string that mix Chinese characters and English words;
      2/ Counts the number of occurrences of each English word and each Chinese character in the parameter;
      3/ Returns an array in descending order of their frequency.
   """
   string_cn = Reclassify_cn(string)
   string_en = Reclassify_en(string)
   result_cn = stats_text_cn(string_cn)
   result_en = stats_text_en(string_en)
   print(result_en,"\n","\n","\n",result_cn)