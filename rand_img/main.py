from instabot import Bot
from wikifinder import*
from tele import dwnld

import os
os.chdir("C:\\Users\\momol\\Desktop\\pypi\\insta\\rand_img")
f=open('after.randimg','w')
f.write("rien")
f.close()
psted=False
try:
    def post(img:str,sub):
        rob=Bot()
        rob.login(username='the_internet_off',password=open('password.h','r').read())
        psted=rob.upload_photo(img,caption=sub)
        if rob.api.last_response.status_code==200:
            print("---psted = 1 py: ",rob.api.last_response)
            psted=True
        else:
            print("---psted = 0 py: ",rob.api.last_response)
            psted=False
                

        rob.logout()
    def wiki():
        page='https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
        text=extract_text(page)
        return extract_titre(text)
    nom=wiki()
    dwnld(nom)
    fomat=""
    for i in nom:
        if i==" ":
            fomat=fomat+"_"
        else:
            fomat=fomat+i
    lieu="C:\\Users\\momol\\Desktop\\pypi\\insta\\rand_img\\simple_images"+"\\"+fomat
    os.chdir(lieu)
    image=os.listdir()[0]
    post(lieu+"\\"+image,nom)
except:
    psted=False
os.chdir("C:\\Users\\momol\\Desktop\\pypi\\insta\\rand_img")
f=open('after.randimg','w')
if psted:
    f.write("good")
else:
    f.write("no")
f.close()

    
