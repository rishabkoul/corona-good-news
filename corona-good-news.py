import streamlit as st
from newsapi import NewsApiClient
from textblob import TextBlob


# Init
newsapi = NewsApiClient(api_key='2fab1663f88044baa813218a1b9189da')

# /v2/top-headlines
all_articles = newsapi.get_top_headlines(language='en',country='in')

def main():
    st.write("""
# Good News App

This app shows top good news headlines in india.
""")
    for i in range(0,len(all_articles["articles"])):
        edu=TextBlob(str(all_articles["articles"][i]["content"]))
        x=edu.sentiment.polarity
        if x>0 and x<=1:
            st.write(x)
            st.header(all_articles["articles"][i]["title"])
            st.markdown("<img src='"+all_articles["articles"][i]["urlToImage"]+"' style='width:100%;height:auto;'/>", unsafe_allow_html=True)
            st.markdown("<p style='margin-top:20px;'><a href='"+all_articles["articles"][i]["url"]+"' style='font-size:1.3rem;'>"+all_articles["articles"][i]["description"]+"</a></p>", unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()