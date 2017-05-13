#oggpnosn
#hkhr
import os
import requests
from subprocess import call
from time import sleep
import progressbar


API_URL = "https://newsapi.org/v1/articles?source=%s&sortBy=top&apiKey=%s"
SOURCES_OF_INTEREST = ["the-times-of-india", "the-hindu", "bbc-news", "cnn",
                       "google-news", "the-economist", "financial-times",
                       "business-insider", "national-geographic", "hacker-news",
                       "ars-technica", "techcrunch", "the-verge"]



def say(text):
    """it converts text to speech."""
    call(["say", "-v", "Veena", '"%s"'%(text)])


def speakItOut(news):
    """it speaks out news section wise using mac specific "say"."""
    for source_of_interest in SOURCES_OF_INTEREST[::-1]:
        say("News from " + source_of_interest)
        headlines = news[source_of_interest]
        for headline in headlines[::-1]:
            say(headline)
            sleep(1)


def getAPIContent(api_key):
    """it pings all the sources of interest and gets the news."""
    news = {}
    bar = progressbar.ProgressBar()
    for source_of_interest in bar(SOURCES_OF_INTEREST):
        url = API_URL%(source_of_interest, api_key)
        resp = requests.get(url)
        requestContent = resp.json()
        articles = requestContent["articles"]
        news[source_of_interest] = articles
    return news


def getHeadlines(news):
    """it return headlines given the articles in news."""
    headlines = {}
    for source_of_interest in SOURCES_OF_INTEREST:
        articles = news[source_of_interest]
        headlinesOfSource = [article["title"] for article in articles]
        headlines[source_of_interest] = headlinesOfSource
    return headlines


def showNewsOnTerminal(news):
    """it shows headline and link on terminal for user to click."""
    for source_of_interest in SOURCES_OF_INTEREST:
        print "-----------------------------------" + source_of_interest + "\n"
        articles = news[source_of_interest]
        for article in articles:
            print "------"
            print "\033[1m" + article["title"] + "\033[0m"
            print article["url"]
            print article["description"]



if __name__ == "__main__":
    if len(os.sys.argv) == 2:
        api_key = os.sys.argv[1]
        news = getAPIContent(api_key)
        showNewsOnTerminal(news)
        headlines = getHeadlines(news)
        speakItOut(headlines)
