# opens the message file
messages <- read.csv(file.choose())

# opens the questionnaire file
kysely <- read.csv(file.choose(), header = TRUE, sep = ";", fileEncoding = "latin1", stringsAsFactors = FALSE)


age <- kysely$AGE
age
typeof(age)

######################
# the age distribution histogram
library(ggvis)
kysely %>%
  ggvis(~AGE) %>%
  layer_histograms(width = 5, boundary = 5, fill := "#E74C3C") %>%
  add_axis("x", title = "Âge") %>%
  add_axis("y", title = "Nombre")

######################
# ages and ids together
age_ids <- data.frame(age, kysely$ID_NUMERO_TEL)

from30to55 <- (age_ids$age >= 30) & (age_ids$age <= 55)
from30to55
summary(from30to55)
