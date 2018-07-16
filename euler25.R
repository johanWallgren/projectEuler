
library('Rmpfr')

options(scipen=9999)


fib <- function(n){
  f1 <- 1
  f2 <- 1
  for(i in 2:n){
    temp <- f2
    f2 <- f2 + f1  
    f1 <- temp
  }
  return(nchar(f1))
}

lenRet <- 4
n <- 50
while(lenRet < 1000 && lenRet > 3){
  lenRet <- fib(n)
  n <- n + 1
  print(lenRet)
}

# 4782