from instabot import Bot
from datetime import datetime

def post():
    rob=Bot()
    rob.login(username='_rip._.paul_2002_2021',password=open('password.h','r').read())
    rob.upload_photo("arbre2.jfif",
                     caption="Rip Paul, "+str(datetime.now().timetuple().tm_yday)+"ème jour de l'année"
                     )
    
    #rob.send_message(random.choice(list(Pays.countries)).name,["momoladebrouill","geule_le_breton","nathoun0","florian_mrtr"])
    #rob.reset_cache()
    rob.logout()
post()
