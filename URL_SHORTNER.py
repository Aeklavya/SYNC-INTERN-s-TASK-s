import pyshorteners
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)
url = "https://www.linkedin.com/company/syncinterns/"
shorten_url = shorten_url(url)
print(f"Shortened URL: {shorten_url}")
