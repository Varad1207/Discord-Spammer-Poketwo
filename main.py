from webserver import keep_alive
import requests

channelID = 1078908602758213653
headers = {
    "MTAyNjE4ODgzMjY0OTAwMzAxOA.G7sDSS.hoVptq2uMLjMFyj-ro3uiQt08IOMpsscbadVOg":
    "MTAyNjE4ODgzMjY0OTAwMzAxOA.G7sDSS.hoVptq2uMLjMFyj-ro3uiQt08IOMpsscbadVOg"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
