from TikTokApi import TikTokApi

verifyFp = "verify_dafb618cd65aabd26384f05f9e60b287"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

#Tiktoks liked by a user and outputs a csv

users = api. user_liked_by_username("SonicStarx")

print(users)