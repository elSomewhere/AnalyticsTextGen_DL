# AnalyticsTextGen_DL

Raw analytics data & simple crawler and parser for financial research data from ex Swiss SKA finaancial services.
RawDat:
https://drive.google.com/open?id=13HYJy5I0FLyhtf-aF3V_E4N_CFMnqx7o

Inspiration..:
THIS: https://www.analyticsvidhya.com/blog/2018/04/solving-an-image-captioning-task-using-deep-learning/


IDEAS / TODO:
1. smart sorting of available rawDat (sort the text files into asset / research classes using available metadata).
2. Get more data. Broker accounts for JPM & crawl it, maybe even UBS research data etc etc.
3. Data cleaning
4. Build a generative language model to test language modeling & learning architecture approaches (word vs char vs sentence level granularity of generation, embeddings etc.). (currently doing this on character level)
5. Build a generative model for time series (need to capture features of data & not necessarely forecasts of data - that can be a separate model in itself and may just as well use classical statistical forecasting approaches)
6. Use above model (Encoder /Decoder) or come up with improvements (GAN appraoch)
CURRENT script:

crawl_ska.py - crawls the public research database. NO NEED TO EXECUTE, SEE GOOGLE DRIVE LINK
parse_ska.py - parses the crawled text files. Change the directory it points to to the above text files. CAN BE IMPROVED, ESPECIALLY SHOULD ALSO SORT THE TEXT FILES IN ASSET CLASSES. 




