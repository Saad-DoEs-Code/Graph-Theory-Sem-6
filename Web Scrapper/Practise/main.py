import requests

# This function will Retrieve HTML data and Save it to a file
def getDataAndSaveFile(url, filename,):
    # request = requests.get(url, proxies=proxies) In case you want to use proxies
    request = requests.get(url)
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(request.text)


url = "https://www.dawn.com/"

# Save the HTML data to a file
soup= bea

