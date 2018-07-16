
library(tidyverse)
library(combinat)

nums <- as.character(c(0:9))
allPerm <- permn(nums)

allPermC <- '1'
for (i in 1:length(allPerm)){
  allPermC[i] <- str_c(allPerm[[i]], collapse = '')
}

allPermCS <- sort(allPermC)
allPermCS[1e6]
