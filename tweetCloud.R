library(tm)
library(wordcloud)

require(tm)
require(wordcloud)


tweets <- read.csv("xboxreveal.csv")

tweetCorpus <- Corpus(DataframeSource(data.frame(tweets)))
tweetCorpus <- tm_map(tweetCorpus, removePunctuation)
tweetCorpus <- tm_map(tweetCorpus, tolower)
tweetCorpus <- tm_map(tweetCorpus, function(x) removeWords(x, stopwords("english")))

png("tweetCloud.png", width=12,height=8, units='in', res=300)
wordcloud(tweetCorpus, max.words=350, rot.per=.15, vfont=c("sans serif","plain"), min.freq=3, scale=c(45,.8), colors=brewer.pal(3, "Dark2"))
dev.off()
