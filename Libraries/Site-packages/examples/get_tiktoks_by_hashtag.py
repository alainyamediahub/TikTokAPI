from TikTokApi import TikTokApi
verifyFp = "verify_dafb618cd65aabd26384f05f9e60b287"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

count = 10

tiktoks = api.by_hashtag("funny", count=count)

for tiktok in tiktoks:
    print(tiktok)
