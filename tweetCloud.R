library(tm)
library(wordcloud)

require(tm)
require(wordcloud)


tweets <- read.csv("xboxreveal.csv")

tweetCorpus <- Corpus(DataframeSource(data.frame(tweets)))
tweetCorpus <- tm_map(tweetCorpus, removePunctuation)
tweetCorpus <- tm_map(tweetCorpus, tolower)
tweetCorpus <- tm_map(tweetCorpus, function(x) removeWords(x, stopwords("english")))

png("tweetCloud3.png", width=1280,height=800)
wordcloud(tweetCorpus, max.words=350, vfont=c("sans serif","plain"), min.freq=3, scale=c(25,4), colors=brewer.pal(3, "Spectral"))
dev.off()