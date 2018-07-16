library(tidyverse)

startDate = as.Date('1901-01-01')
endDate = as.Date('2000-12-31')
nDays = as.integer(endDate - startDate)
nSundays = 0

for(i in 1:nDays){
  
  if (as.POSIXlt(startDate + i)$mday == 1 && weekdays.Date(startDate + i) == 'söndag'){
    nSundays = nSundays + 1
  }
}