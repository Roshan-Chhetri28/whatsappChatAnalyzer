import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Whatsapp Chat Analyzer', page_icon='😘', layout='wide', initial_sidebar_state='auto')
st.sidebar.title('Whatsapp Chat Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocess(data)

    # st.dataframe(df.head())

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    user_selected = st.sidebar.selectbox('Select a user', user_list)

    if st.sidebar.button('Show User Stats'):
        st.title("User Stats")

        num_message, words, num_media_messages, num_links = helper.fetch_stats(user_selected, df)
        col1, col2, col3, col4 =st.columns(4)
        with col1:
            st.header('Total Messages')
            st.write(f'{num_message}')
        with col2:
            st.header('Total Words')
            st.write(f'{words}')
        with col3:
            st.header('Media Messages')
            st.write(f'{num_media_messages}')
        with col4:
            st.header('Links')
            st.write(f'{num_links}')
        
        

        if user_selected == "Overall":
            st.title("Most Active User")
            x, total_percent = helper.fetch_most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation=90)
                st.pyplot(fig)
            with col2:
                st.dataframe(total_percent)

        st.header('Monthly Timeline')
        montly_timeline = helper.montly_timeline(user_selected, df)

        fig, ax = plt.subplots()
        ax.plot(montly_timeline['time'], montly_timeline['message'])
        plt.xticks(rotation=90)
        st.pyplot(fig)

        st.header("Daily Timeline")

        daily_timeline = helper.daily_timeline(user_selected, df)

        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'])
        plt.xticks(rotation=90)
        st.pyplot(fig)

        
        #activity map
        st.title('Activity map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Weekely Activity")
            busy_day = helper.week_activity_map(user_selected, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation=90)
            st.pyplot(fig)
        
        with col2:
            st.header("Montly Activity")
            busy_day = helper.month_activity_map(user_selected, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation=90)
            st.pyplot(fig)
    

        #heat_map
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(user_selected,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        #word cloud
        st.header('Word Cloud')
        df_wc = helper.create_word_cloud(user_selected, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc, interpolation='bilinear')
        st.pyplot(fig)

       


        #emoji
        emoji_df = helper.emoji_helper(selected_user=user_selected, df= df)

        col1, col2 = st.columns(2)

        st.header('Emoji Analysis')
        with col1:
            st.dataframe(emoji_df)
        
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(5), labels=emoji_df[0].head(5), autopct='%0.2f%%')
            st.pyplot(fig)