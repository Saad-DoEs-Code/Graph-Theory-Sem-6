import requests
from bs4 import BeautifulSoup
import concurrent.futures
import asyncio
import time


url_HaF = ['https://www.who.int/southeastasia/news/detail/12-03-2024-deinstitutionalize-mental-health-care--strengthen-community-based-services--who#',
           'https://www.who.int/southeastasia/news/feature-stories/detail/more-than-4500-children-with-cancer-received-good-quality-management-through-institutional-network-and-shared-care-in-south-east-asia-region',
           'https://www.who.int/news/item/18-04-2024-who-launches-first-ever-patient-safety-rights-charter',
           'https://www.who.int/news/item/18-04-2024-leading-health-agencies-outline-updated-terminology-for-pathogens-that-transmit-through-the-air',
           'https://www.who.int/news/item/15-04-2024-special-programme-on-sexual-and-reproductive-health-reports-on-year-of-progress',
           'https://www.who.int/news/item/12-04-2024-in-world-first--nigeria-introduces-new-5-in-1-vaccine-against-meningitis',
           'https://www.who.int/news/item/12-04-2024-challenging-harmful-masculinities-and-engaging-men-and-boys-in-sexual-and-reproductive-health',
           'https://www.who.int/news/item/09-04-2024-who-sounds-alarm-on-viral-hepatitis-infections-claiming-3500-lives-each-day',
           'https://www.who.int/news/item/08-04-2024-statement-following-the-thirty-eighth-meeting-of-the-ihr-emergency-committee-for-polio',
           'https://www.who.int/news/item/05-04-2024-global-deployment-of-rapid-diagnostic-tests-to-boost-fight-against-cholera',
           'https://www.who.int/news/item/30-03-2024-2023--outbreaks-of-swine-influenza',
           'https://www.who.int/news/item/30-03-2024-2023--outbreaks-of-avian-influenza',
           'https://www.who.int/news/item/29-03-2024-who-publishes-updated-guidelines-on-hepatitis-b',
           'https://www.who.int/news/item/22-03-2024-who-world-tb-day-message',
           'https://www.who.int/news/item/14-03-2024-over-1-in-3-people-affected-by-neurological-conditions--the-leading-cause-of-illness-and-disability-worldwide'
           ]

url_Sports=['https://www.dawn.com/news/1828234/ex-australia-skipper-meg-lanning-says-obsession-caused-retirement',
            'https://www.dawn.com/news/1828243/real-madrid-dig-deep-for-revenge-in-manchester',
            'https://www.dawn.com/news/1828241/al-ains-rahimi-bags-hat-trick-to-end-al-hilals-record-run',
            'https://www.dawn.com/news/1828225/rain-wipes-out-first-pakistan-new-zealand-t20-after-just-two-balls',
            'https://www.dawn.com/news/1828211/indian-captain-rohit-sharma-says-would-love-to-face-pakistan-in-test-cricket',
            'https://www.dawn.com/news/1828215/windies-skippers-century-leads-side-to-victory-in-1st-odi-against-pakistan-women',
            'https://www.dawn.com/news/1828189/azam-khans-participation-in-new-zealand-t20i-series-uncertain',
            'https://www.dawn.com/news/1828056/eyeing-t20-world-cup-pakistan-look-to-overwhelm-depleted-new-zealand',
            'https://www.dawn.com/news/1828233/sharma-would-love-to-play-tests-against-pakistan-at-neutral-venue',
            'https://www.dawn.com/news/1828245/rock-solid-ruud-racks-up-season-leading-victory-in-barcelona',
            'https://www.dawn.com/news/1828055/powell-whispering-in-narines-ears-for-t20-world-cup-return',
            'https://www.dawn.com/news/1828053/lahore-karachi-win-big-on-first-day-quetta-edge-rawalpindi',
            'https://www.dawn.com/news/1828050/nadal-comeback-ends-in-barcelona-open-second-round',
            'https://www.dawn.com/news/1827881/world-athletics-prize-money-at-games-goes-against-olympic-spirit',
            'https://www.dawn.com/news/1827878/manchester-city-dreaming-about-double-treble-as-real-madrid-come-to-town',]


url_SaE=['https://www.dawn.com/news/1828207/google-terminates-28-employees-for-protest-of-israeli-cloud-contract',
         'https://www.dawn.com/news/1828116/tiktok-asked-about-risks-of-its-new-version',
         'https://www.dawn.com/news/1827914/largest-black-hole-discovered-in-milky-way',
         'https://www.dawn.com/news/1827606/openai-comes-to-asia-with-new-office-in-tokyo',
         'https://www.dawn.com/news/1827209/ai-providing-new-tools-to-threat-actors-for-attacks-says-cybersecurity-firm',
         'https://www.dawn.com/news/1826999/us-topples-china-as-taiwans-largest-export-market-due-to-chips-ai-demand',
         'https://www.dawn.com/news/1334700/4-smartphones-you-should-consider-if-you-love-taking-selfies',
         'https://www.dawn.com/news/1206329/a-7-step-guide-for-pakistani-victims-of-hacking-and-blackmail',
         'https://www.dawn.com/news/1827209/ai-providing-new-tools-to-threat-actors-for-attacks-says-cybersecurity-firm',
         'https://www.dawn.com/news/1397168/artificial-intelligences-current-ability-future-prospects-discussed',
         'https://www.dawn.com/news/1434638',
         'https://www.dawn.com/news/1275630/is-pak-truck-driver-the-most-exciting-driving-game-to-come-from-pakistan-we-find-out',
         'https://www.dawn.com/news/1466552/doctor-performs-first-5g-surgery','https://www.dawn.com/news/1585148/countrys-first-bike-sharing-service-launched','https://www.dawn.com/news/1752630/careem-launches-manual-ride-booking-service-in-karachi-amid-internet-shutdown','https://www.dawn.com/news/1828416/the-ban-on-x-the-national-security-rationale-doesnt-fly-anymore'
         ]


url_list = [url_HaF, url_Sports, url_SaE]








soup_HaF = []
soup_Sports=[]
soup_SaE=[]




def request_url_data(url):

    # It will work for an individual link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if (url in url_HaF):
        soup_HaF.append(soup)
    elif (url in url_Sports):
        soup_Sports.append(soup)
    elif (url in url_SaE):
        soup_SaE.append(soup)
    else:
        print('No data')


def get_response(urls):

    # we will recieve single URL List here => url_HaF, url_Sports
    url_list = urls
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # All the links in single URL list will be passed to request_url_data function 
        executor.map(request_url_data, url_list)


def get_content(url_list):

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_response, url_list)

    # for urls in url_list:
    #     get_response(urls)


# Functions for Health and Fitness
content_list_HaF=[]
async def save_to_file_HaF(content):
    content_list_HaF.append(content)
    # file_count = 1
    file_count_HaF = 1
    
    for c in content_list_HaF:
        # print(c) code is working till here
        if file_count_HaF <= 15:
            
            file_name = f'./Health and Fitness/page_{file_count_HaF}.txt'
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(c)
            print(f"File {file_name} saved successfully!")
            
            file_count_HaF += 1
        else:
            print("Loop Broken")
            break


def get_article_HaF(soup):

    article = soup.find('article')
    # print(article.text)
    asyncio.run(save_to_file_HaF(article.text))

#  Functions for Sports

content_list_Sports=[]
async def save_to_file_Sports(content):
    content_list_Sports.append(content)
    file_count_Sports=1
    # file_count = 1
    
    for c in content_list_Sports:
        if file_count_Sports <= 15:
            
            file_name = f'./Sports/page_{file_count_Sports}.txt'
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(c)
            print(f"File {file_name} saved successfully!")
            # global file_count_Sports
            file_count_Sports += 1
        else:
            print("Loop Broken")
            break

def get_article_Sports(soup):
    #  Not Working Yet
    data= soup.find(class_='story__content')
    # print(data.text)
    asyncio.run(save_to_file_Sports(data.text))

#  Functions for Science and Education

content_list_SaE=[]

async def save_to_file_SaE(content):
    content_list_SaE.append(content)
    file_count_SaE=1

    if(len(content_list_SaE)>=15):
        for c in content_list_SaE:
            if file_count_SaE <= 15:
                file_name = f'./Science and Education/page_{file_count_SaE}.txt'
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(c)
                print(f"File {file_name} saved successfully!")
                # global file_count_SaE
                file_count_SaE += 1
            else:
                print("Loop Broken")
                break

def get_article_SaE(soup):
    #  Not Working Yet
    data= soup.find(class_='story__content')
    # print(data.text)
    # asyncio.run(save_to_file_SaE(data.text))
    asyncio.run(save_to_file_SaE(data.text))





get_content(url_list)

time.sleep(2)


for soup in soup_HaF:

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_article_HaF, soup)

for soup in soup_Sports:

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_article_Sports, soup)

for soup in soup_SaE:

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_article_SaE, soup)

# print(len(url_HaF)) 15-links

time.sleep(5)

# print("Health and Fitness" + str(len(content_list_HaF)))
# print("Science" + str(len(content_list_SaE)))
# print('sports' + str(len(content_list_Sports)))



# Programm is working fine but not saving the files in the folder.

