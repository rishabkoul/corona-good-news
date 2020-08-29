import streamlit as st
from newsapi import NewsApiClient
from textblob import TextBlob
import os


# Init
newsapi = NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))

# /v2/top-headlines
all_articles = newsapi.get_everything(q='covid',language='en',page_size=100)
top = newsapi.get_top_headlines(q='covid',language='en',page_size=100)

def main():
    st.write("""
# Covid Good News App

This app shows top good news headlines abput Covid-19.
""")

    for i in range(0,len(top["articles"])):
        edu=TextBlob(str(top["articles"][i]["content"]))
        x=edu.sentiment.polarity
        if x>=0.3 and x<=1:
            st.write(x)
            st.header(top["articles"][i]["title"])
            st.markdown("<img src='"+top["articles"][i]["urlToImage"]+"' style='width:100%;height:auto;'/>", unsafe_allow_html=True)
            st.markdown("<p style='margin-top:20px;'><a href='"+top["articles"][i]["url"]+"' style='font-size:1.3rem;'>"+top["articles"][i]["description"]+"</a></p>", unsafe_allow_html=True)

    for i in range(0,len(all_articles["articles"])):
        edu=TextBlob(str(all_articles["articles"][i]["content"]))
        x=edu.sentiment.polarity
        if x>=0.3 and x<=1:
            st.write(x)
            st.header(all_articles["articles"][i]["title"])
            st.markdown("<img src='"+all_articles["articles"][i]["urlToImage"]+"' style='width:100%;height:auto;'/>", unsafe_allow_html=True)
            st.markdown("<p style='margin-top:20px;'><a href='"+all_articles["articles"][i]["url"]+"' style='font-size:1.3rem;'>"+all_articles["articles"][i]["description"]+"</a></p>", unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()