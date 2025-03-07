import re
from wordcloud import WordCloud
import emoji
from collections import Counter
import pandas as pd
def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    
    num_messages = df.shape[0]
    words = []
    for messages in df['message']:
        words.extend(messages.split()) 

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for messages in df['message']:
        links.extend(re.findall(r'http\S+', messages))
    return num_messages, len(words), num_media_messages, len(links)

def fetch_most_busy_users(data):
    x = data['user'].value_counts().head()
    total_percent = round(data['user'].value_counts()/data.shape[0]*100, 2).reset_index().rename(columns={'index': 'user', 'count': 'percent'})
    return x, total_percent

def montly_timeline(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    
    return  timeline


def daily_timeline(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    timeline = df.groupby(['only_date']).count()['message'].reset_index()
    return timeline

def create_word_cloud(selected_user, df):
    
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    df = df[df['message']!="media omitted\n"]
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    df = df[df['message']!="<Media omitted>\n"]
    df = df[df['message']!="null"]
    
    words = []
    for message in df['message']:
        words.extend(message.lower().split())
    
    common_words = pd.DataFrame(Counter(words).most_common(20), columns=['word', 'count'])
    return common_words
    
def emoji_helper(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
 
    return emoji_df



def week_activity_map(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
     
    return df['day_name'].value_counts().sort_index()

def month_activity_map(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
     
    return df['month'].value_counts().sort_index()


def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap