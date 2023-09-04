import openai
import json
import os
import sys



class Prompter:


    def __init__(self, OPENAI_API_KEY):
        self.OPENAI_API_KEY = OPENAI_API_KEY
        openai.api_key=self.OPENAI_API_KEY

    def generate_prompt(self, textRecieved):
        return """I am yacqub, a 23 year old first generation somali boy who lives in the city of phoenix. 
            I am an entreprenuer who works specifically  in digital marketing. I am someone who is genuine 
            and very funny but brief in the way I speak. I usually speak in phrases or one sentence responses, 
            and I also do not like using emojies or specific details of what I am doing. After answering a question 
            I usually ask the person a question about themselves or something regarding the conversation depending 
            on the situation. With that information, respond to this following text message as you think I would: 
            
            Text Message: {}
            """.format(
                    textRecieved.capitalize()
                )
    
    def generateResponse(self, textRecieved):
        openai.api_key=self.OPENAI_API_KEY
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.generate_prompt(textRecieved),
            temperature=0.6,
        )
        result=response.choices[0].text

        print(result)

