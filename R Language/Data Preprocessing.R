data <- data.frame(
  Name=c("Ram","Sita","Kamlesh"),
  Age=c(20,30,15),
  Score=c(80,NA,94)
)
print(data)

# Chcking Missing Value
colSums(is.na(data))

#Remove null value
clear_data <- na.omit(data)
print(clear_data)

#Data Imputation : Fill the NA value with mean
data$Score[is.na(data$Score)]<-mean(data$Score, na.rm = TRUE)
print(data)

#Sorting
sort<-data[order(data$Age, decreasing = TRUE)]
print(sort)