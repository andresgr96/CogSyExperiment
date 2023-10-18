library(ggplot2) # these libraries allow us to use the functions with which
library(plyr) 
library(dplyr)
library(stringr)
# Install the stringr package

setwd('/Users/filip')

attention_data <- read.csv('attention_merged_results.csv')

mean(attention_data$Reaction_Time)

outlier1 <- mean(attention_data$Reaction_Time) + 2.5 * sd(attention_data$Reaction_Time)
outlier2 <- mean(attention_data$Reaction_Time) - 2.5 * sd(attention_data$Reaction_Time)

attention_data <- attention_data[attention_data$Reaction_Time > outlier2,]
attention_data <- attention_data[attention_data$Reaction_Time < outlier1,]

mean(attention_data$Reaction_Time)

color_categories <- c("Red", "Green", "Blue")

attention_data <- attention_data %>%
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

ggplot(attention_data, aes(x = Reaction_Time, fill = Dominant_Color)) +
  geom_density(alpha = 0.5) +
  labs(
    title = "Density Plot of Reaction Time by Dominant Color",
    x = "Reaction Time",
    y = "Density"
  )
