from InstaBot import InstagramBot

bot = InstagramBot('', '')
bot.signIn()
f= open("data.txt","w+")
list = bot.getLikesInPost('https://www.instagram.com/p/B5VgD2YpvT02THce2JqXBGMhPmmDYjdfarzlMc0/',f)




f.close()