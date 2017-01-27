kysely <- read.csv(file.choose(), header = TRUE, sep = ";", fileEncoding = "latin1", stringsAsFactors = FALSE)

age <- kysely$AGE
age

######################
# the age distribution histogram
library(ggvis)
kysely %>%
  ggvis(~AGE) %>%
  layer_histograms(width = 5, boundary = 5, fill := "#E74C3C") %>%
  add_axis("x", title = "Âge") %>%
  add_axis("y", title = "Nombre")