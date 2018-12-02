# Web-Crawler
This is a simple web crawler that implements [Scrapy](https://scrapy.org/).

## How to use
### Pre-req
It is very simple to use this appication. First, Python 3 is required to run this application. [Anaconda](https://www.anaconda.com/download/#linux) is highly recommended since it has rich packages and easy to use. You can use Mac/Windows/Linux to run it.

Once Python 3 is installed, you will need to install Scrapy as well. Follow the instruction [here](https://anaconda.org/conda-forge/scrapy) and you are good to go. (This instruction is based on Anaconda package)

### How to run
Navigate to the project folder. In this program, navigate to `/Web-Crawler/src/webwithin`

There are several formats that Scrapy supports, for example, CSV, JSON, and etc. There are several crawlers that are available in this simple example. And to get, for example, JSON format of one case in this code, you can run the command:

```
scrapy crawl cnn_news -o cnn_news.json -t json
```

Or as the example in the code, for the output of CSV format

```
scrapy crawl fundrazr -o fundrazr.csv
```

Of course you can check out Scrapy documentation for more usage.
