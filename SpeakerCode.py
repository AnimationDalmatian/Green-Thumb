import pyttsx3
engine = pyttsx3.init() # object creation

def LowWater():
    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)                        
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

    engine.say("Please water me, ive gone without water for too long.")
    engine.runAndWait()
    engine.stop()



