import openai
from webex_bot.models.command import Command
from webex_bot.models.response import Response

class gpt(Command):
    messages=[]
    messages.append({"role": "system", "content": ""})

    def __init__(self):
        super().__init__()
    
    def execute(self, message, attachment_actions, activity):
        
        openai.api_key = ("YOUR_API_KEY")

        self.messages.append({"role": "user", "content": message})
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.messages)

        gpt_response=completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": message})
        return(gpt_response)