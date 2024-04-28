import sys

# Set default encoding to UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# Define the base directory where data will be saved
base_dir = './Processed Data'




# These list will store original text data from different categories
text_data_HaF=[]
text_data_Sports=[]
text_data_SaE=[]

# These lists will store processed text from different categories
processed_text_HaF=[]
processed_text_Sports=[]
processed_text_SaE=[]


def open_files(topic, file_count):

    file_name = f'../Web Scrapper/Work Folder/{topic}/page_{file_count}.txt'
    with open(file_name, 'r', encoding='utf-8') as file:  # Specify encoding
        text = file.read()
        if topic == 'Health and Fitness':
            text_data_HaF.append(text)
        elif topic == 'Sports':
            text_data_Sports.append(text)
        elif topic == 'Science and Education':
            text_data_SaE.append(text)


def scroll_through_topics():

    for i in range(1, 16):
        open_files('Health and Fitness', i)
        open_files('Sports', i)
        open_files('Science and Education', i)


def process_data(list_of_text):

    topic = ""
    if list_of_text == text_data_HaF:
        topic = "Health and Fitness"
    elif list_of_text == text_data_Sports:
        topic = "Sports"
    elif list_of_text == text_data_SaE:
        topic = "Science and Education"

    # Clean the text
    
    for text in list_of_text:
        # Tokenize the text
        tokens = word_tokenize(text)

        # Remove punctuation
        tokens = [word for word in tokens if word not in string.punctuation]

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word.lower() not in stop_words]

        # Stemming (optional)
        # porter = PorterStemmer()
        # tokens = [porter.stem(word) for word in tokens]

        # Lemmatization (optional)
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

        # Reconstruct the cleaned text
        cleaned_text = ' '.join(tokens)

        # print(cleaned_text)
        if topic == "Health and Fitness":
            processed_text_HaF.append(cleaned_text)
        elif topic == "Sports":
            processed_text_Sports.append(cleaned_text)
        elif topic == "Science and Education":
            processed_text_SaE.append(cleaned_text)

import os



def save_data(data, category):
    # Create a directory for the category if it doesn't exist
    category_dir = os.path.join(base_dir, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)

    # Write each processed text to a separate file
    for i, text in enumerate(data):
        file_name = f'page_{i + 1}.txt'
        file_path = os.path.join(category_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)




def main():

    scroll_through_topics()
    
    process_data(text_data_HaF)
    process_data(text_data_Sports)
    process_data(text_data_SaE)

    print(len(processed_text_HaF))
    print(len(processed_text_Sports))
    print(len(processed_text_SaE))

    # Save processed data for each category
    save_data(processed_text_HaF, "Health and Fitness")
    save_data(processed_text_Sports, "Sports")
    save_data(processed_text_SaE, "Science and Education")

    

if __name__=='__main__':
    main()