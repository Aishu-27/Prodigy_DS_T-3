import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load your dataset
data = pd.read_csv('your_data.csv')  # Replace with your file

# Quick function to get sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment analysis
data['Sentiment'] = data['text'].apply(get_sentiment)

# Visualization: Pie chart
data['Sentiment'].value_counts().plot.pie(autopct='%1.0f%%', colors=['green', 'blue', 'red'])
plt.title('Sentiment Distribution')
plt.ylabel('')
plt.show()

# WordCloud for Positive Sentiment
positive_words = ' '.join(data[data['Sentiment'] == 'Positive']['text'])
wordcloud = WordCloud(background_color='white').generate(positive_words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Words WordCloud')
plt.show()
