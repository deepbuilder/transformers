data_url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"

import requests

response = requests.get(data_url)

with open("data/input.txt", "w") as file:
    file.write(response.text)