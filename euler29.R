

i <- 1
res <- 0
for(a in 2:100){
  for (b in 2:100){
    res[i] <- a^b
    i <- i + 1
  }
}

length(unique(res))