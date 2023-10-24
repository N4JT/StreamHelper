import eel 
from handleMongo.handleFunctionsDB import has_user_autologin
    
eel.init('styles')  
has_user_autologin()
eel.start('index.html', size=(800, 600)) 
