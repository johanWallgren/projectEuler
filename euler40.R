
numStr <- '0.'
tic <- 1
while (nchar(numStr) <= 1e5){
  numStr <- paste0(numStr, as.character(tic))
  tic <- tic + 1
}

num <- 1
res <- 1
for (i in 1:6){
  res <- res * as.integer(substr(numStr, num + 2, num + 2))
  print(res)
  num <- num * 10
}
  
