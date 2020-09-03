import requests

def search(wort):

    wort=wort.title()#Der erste Buchstabe des Wortes muss immer groß sein. Falls das nicht der fall ist wird das hier korregiert
    try:
        url='https://de.wiktionary.org/wiki/'+wort
        response=requests.get(url)#Ich lade die ganze Webseite zu dem Thema in Python
        
        
        text=response.text#Die ganze Webseite wird in Text umgewandelt
        gender_index=text.index("Genus:")#Das Genus(Geschlecht) wir auf der Webseite gesucht. Es wird gleich das erste Ergebnis genommen da Genus oft schon im Titel steht
        
        gender=text[gender_index+7:gender_index+8]#Der Anfangsbuchstabe des Geschlechtes wird gespeichert
        #print("Gender=",gender)
        
        if(gender=="N" or gender=="F" or gender=="M"): #Wenn N=Neutral, F=Femal/Weiblich M=Male/Männlich rauskommt wird das zurück gegeben
            return gender
            
        else:#Falls ein Fehler vorkommt wird  E für Error zurückgegeben
            print("Error")
            return "E"
        
    except:
        print("Leider konnte zu dem Wort kein Artikel gefunden werden. Es kann sein das kein Wiktionary-Artikel dazu exestiert oder sie das Wort falsch geschrieben haben")
        return "E" #Bei einem Fehler wird E für Error zurück gegeben
    

