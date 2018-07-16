

library(tidyverse)

squareSize <- 1001

step <- 2
rowNo <- 1

d1 <- 1
d2 <- 1
d3 <- 1
d4 <- 1

dSum <- 1

for(i in 1:((squareSize - 1)/2)){
  d1 <- d4 + step
  d2 <- d1 + step
  d3 <- d2 + step
  d4 <- d3 + step
  
  dSum <- dSum + d1 + d2 + d3 + d4

    rowNo <- rowNo + 1
  step <- step + 2
}

print(dSum)
  




