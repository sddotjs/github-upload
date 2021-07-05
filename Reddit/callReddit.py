# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:35:17 2021

@author: sachi
"""

from myReddit2 import Reddit
import spacy

SUB = 'wallstreetbets'
#SUB = 'investing'
client_id = '0Dr0yv8JxUNwkg'
secret_token = '-63wewAiP6_4nonn7KBMtZz6oiqo-g'
User = 'ssd579'
PWD = 'Reddit@579'
    
reddit=Reddit(client_id,secret_token,User,PWD)
    
data = reddit.get_new(SUB,20)
    
data = data.replace({'|': ''}, regex=True)
    
data.to_csv(f'./data/reddit_{SUB}.csv', sep='|', index=False)


textdata = data.to_string()

n=900000

chunks = [textdata[i:i+n] for i in range(0, len(textdata), n)]

nlp = spacy.load("en_core_web_sm")

text_file = open(f"./data/myEntities.txt","w",encoding="utf-8")

print("Processing....")

for i in range(len(chunks)):   
    doc = nlp(chunks[i])
    for ent in doc.ents:
        #print(f"{ent.label_}: {ent.text}")
        text_file.write(f"{ent.label_}, {ent.text}")
        text_file.write("\n")
#       #print(ent.text, ent.start_char, ent.end_char, ent.label_)
text_file.close()
print("Complete!")

