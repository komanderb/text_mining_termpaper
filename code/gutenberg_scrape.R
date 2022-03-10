#install.packages('gutenbergr')
library(tidyverse)
library(dplyr)
library(gutenbergr)
setwd("C:/Users/lenovo/Documents/GitHub/text_mining_termpaper/data")
fairy_id = read.csv("fairy_id.csv")
fairy_id = fairy_id[-1]
names(fairy_id)[1] <- 'gutenberg_id' 

df <- gutenberg_download(as.numeric(fairy_id$gutenberg_id), meta_fields = c("author", "title", "language"))

df <- df %>% filter(language == 'en')
df <- left_join(df, fairy_id)

write.csv(df, "fairy_tales_en.csv")

df <- gutenberg_metadata %>% 
  filter(gutenberg_bookshelf == "Children's Literature", language == "en")
df <- df %>% filter(!(duplicated(title)))

df_big <- gutenberg_download(df$gutenberg_id, meta_fields =  c("author", "title"))

# sometimes books are zipped and thus not downloaded - within the 
# gutenberg-downloads there are functions that can play around that. 


write.csv(df_big, "all_children_en.csv")
