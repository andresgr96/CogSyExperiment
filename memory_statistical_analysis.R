library(ggplot2) # these libraries allow us to use the functions with which
library(plyr) 

setwd('/Users/filip')

memory_data <- read.csv('memory_merged_results.csv')

memory_data$Correct <- ifelse(memory_data$Correct, 1, 0)

memory_data <- memory_data %>%
  mutate(
    Red = as.numeric(str_extract(Color, "(?<=\\()[^,]+")),
    Green = as.numeric(str_extract(Color, "(?<=,)[^,]+")),
    Blue = as.numeric(str_extract(Color, "(?<=,)[^,]+(?=\\))")),
    Dominant_Color = case_when(
      Red >= Green & Red >= Blue ~ "Red",
      Green >= Red & Green >= Blue ~ "Green",
      Blue >= Red & Blue >= Green ~ "Blue",
      TRUE ~ "Other"
    )
  )

memory_data <- memory_data %>%
  filter(Correct == 1)

outlier1 <- mean(memory_data$Dominant_Color) + 2.5 * sd(memory_data$Dominant_Colo)
outlier2 <- mean(memory_data$Dominant_Color) - 2.5 * sd(memory_data$Dominant_Colo)

oneShown <- memory_data[memory_data$Number_Shown == 1,]
twoShown <- memory_data[memory_data$Number_Shown == 2,]
threeShown <- memory_data[memory_data$Number_Shown == 3,]
fourShown <- memory_data[memory_data$Number_Shown == 4,]
oneShown <- 'whatever'
mean(oneShown)

numberDecisions <- rbind(oneShown,twoShown)

ggplot(numberDecisions, aes(x = )) + geom_density(alpha = 0.2)

ggplot(numberDecisions, aes(x = Dominant_Color)) +
  geom_density(alpha = 0.5) +
  labs(
    title = "Density Plot of memory by Dominant Color",
    x = "Reaction Time",
    y = "Density"
  )
