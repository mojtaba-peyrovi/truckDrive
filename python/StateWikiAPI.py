# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:20:50 2020

@author: hero144
"""
from subprocess import run
run('pip install Wikipedia-API==0.3.5')

import wikipediaapi
import pandas as pd

states = pd.read_csv('../data/states/states.csv', encoding='utf-8')
states_lst = states.title.tolist()




print(states_lst)


def WikiAPIHtml(lst):
    for item in lst:
        wiki_html = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.HTML
            )
        p_html = wiki_html.page(item)
        filename = str("../storage/app/public/states/fulltext/") + str(item) + ".txt"
        with open(filename, "w+", encoding='utf-8') as f:
            f.write(p_html.text)
        # print(p_html.text)

    
WikiAPIHtml(states_lst)


def WikiAPISUmmary(lst,states):
    for item in lst:
        ## add summary to states table
        item_index = states.index[states['title'] == item][0]
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(item)
        states.iloc[item_index,states.columns.get_loc('summary')] = page_py.summary
        ## write the summary per state to storage
        filename = str("../storage/app/public/states/summary/") + str(item) + ".txt"
        with open(filename, "w+", encoding='utf-8') as f:
            f.write(page_py.summary)
                

WikiAPISUmmary(states_lst,states)


states.to_csv('../data/states/states_with_summary.csv', encoding='utf-8')

import csv
import pymysql
import pandas as pd



def ConnectMysql():
    mydb = pymysql.connect(
      host="localhost",
      user="root",
      passwd="",
      database="truckdrive"
    )
    cursor = mydb.cursor()
    return cursor,mydb

cursor,db = ConnectMysql()

query = 'INSERT INTO states(title,abbreviation,code,summary) VALUES(%s,%s,%s,%s)'
def WriteOnDB(cursor,db,data,query):
      for row in data.values.tolist():
           q = query
           cursor.execute(q,row)
          # print(row)
      db.commit()
      cursor.close()   

WriteOnDB(cursor, db, states,query)
      
      


# csv_data = pd.read_csv('../data/states/states.csv', encoding='utf-8')
# csv_data_list = csv_data.values.tolist()
# for row in csv_data_list:
#     query = 'INSERT INTO states(title,abbreviation,code,summary) VALUES(%s,%s,%s,%s)'
#     cursor.execute(query,row)
#     print(row)

# mydb.commit()
# cursor.close()                           



# for row in csv_data.iterrows():
#     print(row)



