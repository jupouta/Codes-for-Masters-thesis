library(tm)
library(SnowballC)
library(wordcloud)

# 05...csv
tiedosto <- read.csv(file.choose(), quote = "", sep = "\n", header = FALSE)
tiedosto2 <- read.csv(file.choose(), quote = "", sep = "\n", header = FALSE)

full_tiedosto <-  read.csv(file.choose(), quote = "", sep = "\n", header = FALSE)


smsCorpus <- Corpus(VectorSource(full_tiedosto$V1))
smsCorpus <- tm_map(smsCorpus, content_transformer(tolower))
smsCorpus <- tm_map(smsCorpus, removeNumbers)
smsCorpus <- tm_map(smsCorpus, removePunctuation)
#smsCorpus <- tm_map(smsCorpus, removeWords, stopwords('french')) # don't use, if stopwords included
smsCorpus <- tm_map(smsCorpus, stripWhitespace)
pal2 <- brewer.pal(8,"Dark2")
wordcloud(smsCorpus, max.words = 120, random.order = FALSE, colors = pal2)