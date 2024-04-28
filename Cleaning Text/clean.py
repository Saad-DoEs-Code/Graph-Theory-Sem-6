import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (if not already downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


def read_files(topic, file_count):
    
    text_from_files=[]

    for i in range(1, file_count+1):
        with open(f'../Web Scrapper/Work Folder/{topic}/page_{i}.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            text_from_files.append(text)

    print(len(text_from_files))
    return text_from_files

def scroll_through_topic():

    
    topics = ['Health and Fitness', 'Sports', 'Science and Education']
    for topic in topics:
        if topic == 'Health and Fitness':
            return "Health and Fitness", 15
        elif topic == 'Sports':
            return "Sports", 15
        elif topic == 'Science and Education':
            return "Science and Education", 16
        else:
            return None

def main():

    topic,size = scroll_through_topic()
    # Example text
    print(topic)
    text = read_files(topic, size)

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

    print(cleaned_text)


if __name__=='__main__':
    main()
