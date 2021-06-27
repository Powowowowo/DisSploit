# DisSploit
A python3 library for abusing discords api
Discord Server: <a href="https://discord.gg/ZcNcJQvgB3">DisSploit</a>
# Progress
Project is currently still in development
# ToDo
Complete   - ✔️<br>
Incomplete - ❌<br>
<br>
API Abuse:<br>
  Delete Webhook ✔️<br>
  Block Bypass ❌<br>
<br>
Render:<br>
  Mask Message ✔️ [PATCHED]<br>
  Edited Tag Position Changer ✔️<br>
<br>
URI:<br>
  Windows DoS ✔️<br>
<br>
Misc:<br>
  Glitched Mention ❌<br>
  Unverify Email ✔️<br>
  Custom Gif URL ❌<br>
  2000 Char Bypass ❌<br>
  Guild VC DoS ✔️<br>
<br>
# Documentation

Setting up exploits
```python
from DisSploit import Exploits

APISploits = Exploits.apiabuse()
RenderSploits = Exploits.render()
URISploits = Exploits.URI()
MiscSploits = Exploits.Misc()


```

API Abuse
```python
from DisSploit import Exploits

# Setting up library
APISploits = Exploits.apiabuse()

# Main code
APISploits.DeleteWebhook('webhook_url').execute()
```
Render Exploits
```python
from DisSploit import Exploits

# Setting up library
RenderSploits = Exploits.render()

# Main code
RenderSploits.editTagChange(token, channel_id, message)
```
URI Exploits
```python
from DisSploit import Exploits

# Setting up library
URISploits = Exploits.URI()

# Main code
URISploits.WDoS(token, channel_id)
```
Misc Exploits
```python
from DisSploit import Exploits

# Setting up library
MiscSploits = Exploits.Misc()

# Main code
MiscSploits.GuildVCDoS(token, guild_id)
MiscSploits.UnverifyEmail(token, channel_id)
```
