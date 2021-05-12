#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


pip install SpeechRecognition


# In[ ]:


pip install pyaudio


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


conda install -c anaconda pyaudio


# In[ ]:





# In[ ]:


def stt():
    import speech_recognition as sr 
    import time

    r = sr.Recognizer()


    with sr.Microphone() as source:
    
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 50
        r.dynamic_energy_threshold = False
        print('talk to translate to german:')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            
            return(text)
        except:
            return('Sorry i could not hear you')


# In[ ]:


pip install googletrans==3.1.0a0


# In[ ]:


from googletrans import Translator
sentence=stt()
translator=Translator()
translated_sentence=translator.translate(sentence,src='en',dest='de')
print (sentence)
print (translated_sentence.text)


# In[ ]:





# In[ ]:





# In[ ]:




