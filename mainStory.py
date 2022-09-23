from unicodedata import name
import characters
import locations

def prolog():
    print("Prolog: " + "\n" + "In einer Welt, in der eine Kutsche mit als höchste technische Investiton gilt. Lebt unser Held in einem kleinen Unterschlupf \n\
inmitten eines Waldes. Er ist ein einfacher Jäger, der sich mit dem was er hat zufrieden gibt. Die meiste Zeit versucht er sich von den anderen zu distanzieren,\n\
dass stört eigentlich aber auch sonst niemanden. Die Menschen im Dorf sind froh wenn er an das Dorf Tor kommt und ihnen sein gejagtes verkauft.\n\
Meist verkauft er das Fleisch nichtmal sondern tauscht es gegen andere Nahrungsmittel oder notwendigkeiten ein. Die Dorfbewohner sind dennoch froh \n\
sonst nicht mit dem sonderling herumschlagen müssen. \n\
Eines Tages jedoch, es regnete bereits seit Wochen ohne Pause, ist unser Held gezwungen sich in das Dorf zu begeben und dort nach Unterkunft zu suchen." +"\n" + "\n")

def player_name_question():
    print("Wie heißt du?")

def start_main_storyline():
    print("\n" + "Na dann...", characters.MainCharacter.player_name(name),", Willkommen in", locations.brachsee_firstcity_name)