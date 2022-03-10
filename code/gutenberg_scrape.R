install.packages('gutenbergr')
library(tidyverse)
library(dplyr)
library(gutenbergr)
setwd("C:/Users/lenovo/Documents/GitHub/text_mining_termpaper/data")
fairy_id = read.csv("fairy_id.csv")
fairy_id = fairy_id[-1]
names(fairy_id)[1] <- 'gutenberg_id' 

gutenberg_metadata %>%
  filter(gutenberg_bookshelf == "Children's Myths, Fairy Tales, etc.",
         language == 'en')
# we could use that but it only returns 14 titles where as there are more than 50 
# on the webpage but maybe helpful and very straighforward for the others 
df <- gutenberg_download(as.numeric(fairy_id$gutenberg_id), meta_fields = c("author", "title", "language"))

df <- df %>% filter(language == 'en')
df <- left_join(df, fairy_id)

write.csv(df, "fairy_tales_en.csv")

