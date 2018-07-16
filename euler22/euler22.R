
library(tidyverse)

names <- scan('https://projecteuler.net/project/resources/p022_names.txt', what = "", sep = ",")
names[is.na(names)] <- "NA"
names <- sort(names)

totNameVal <- 0

for(i in 1:length(names)){
  
  splitName <- strsplit(names[i],"")
  nameVal <- 0
  
  for(j in 1:length(splitName[[1]])){
    
    nameVal <- nameVal + match(splitName[[1]][j], LETTERS)
  }
  
  totNameVal <- totNameVal + nameVal * i

}

print(totNameVal)

# 871198282