
d <- function(x){
  y <- seq_len(x)
  sum(y[ x%%y == 0 ]) - x
}

sumAmicable <- 0

for (i in 1:10000){
  if(d(d(i)) == i && d(i) != i){
    sumAmicable <- sumAmicable + i
  }
}

