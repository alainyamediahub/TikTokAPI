from TikTokApi import TikTokApi

verifyFp = "verify_dafb618cd65aabd26384f05f9e60b287"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

count = 50000

tiktoks = api.by_hashtag("pinterest", count= count)

for tiktok in tiktoks:
    # will print all info on a tiktok
     print (tiktok)
    # prints specified keys of a tiktok, added new lines to make output cleaner imo
    # print (tiktok ['desc'],"\n",tiktok['author'],"\n",tiktok['video']['id'], "\t",tiktok['createTime'], "\n")
