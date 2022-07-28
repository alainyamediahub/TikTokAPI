import csv
import pandas as pd
from TikTokApi import TikTokApi

verifyFp = "verify_dafb618cd65aabd26384f05f9e60b287"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

#no. of results to return docs says up to ~2000 can be supported
count = 2000

#first parameter is the hashtag to be searched DO NOT INCLUDE THE HASHTAG IN THE STRING !

tiktoks = api.by_hashtag("littlemoons", count= count)
list_id = []
list_desc = []
list_created = []
list_video_url = []
list_author_id = []
list_author_name = []
list_author_desc = []
for tiktok in tiktoks:
    list_id.append(tiktok["id"])
    list_desc.append(tiktok["desc"])
    list_created.append(tiktok["createTime"])
    list_video_url.append(tiktok["video"]["playAddr"])
    list_author_id.append(tiktok["author"]["id"])
    list_author_name.append(tiktok["author"]["uniqueId"])
    list_author_desc.append(tiktok["author"]["signature"])

df = pd.DataFrame(data={"id":list_id,"desc":list_desc,"createTime":list_created,"url":list_video_url,"author":list_author_id,"author_id":list_author_name,"author_sig":list_author_desc})
df.to_csv("littlemoons2000v2.csv")


#with open('TikTok_Hashtags.csv', mode='w', newline='', encoding="utf-8") as TikTokFile:
   # file_writer = csv.writer(TikTokFile)
    #file_writer.writerow(['Description', 'Author Info', 'Video Info', 'Creation Time'])
    #for tiktok in tiktoks:
     #   file_writer.writerow([tiktok])
       # file_writer.writerow([tiktok['author']])
