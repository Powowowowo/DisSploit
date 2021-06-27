# DisSploit
A python3 library for abusing discords api
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
  Mask Message ✔️<br>
  Edited Tag Position Changer ✔️<br>
<br>
URI:<br>
  Windows DoS ❌<br>
<br>
Misc:<br>
  Glitched Mention ❌<br>
  Unverify Email ❌<br>
  Custom Gif URL ❌<br>
  2000 Char Bypass ❌<br>
  Guild VC DoS ❌<br>
<br>
# Documentation
Delete Webhook
```python
from DisSploit import Exploits

# Setting up library
DisSploit = Exploits.apiabuse()

# Main code
DisSploit.DeleteWebhook('webhook_url').execute()
```
