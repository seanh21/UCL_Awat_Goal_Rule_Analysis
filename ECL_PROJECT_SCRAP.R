library("tidyverse")
league_data <- read_csv("ginf.csv")
colnames(league_data)
head(league_data)

hg_sum <- sum(league_data[, "fthg"])
ag_sum <- sum(league_data[, "ftag"])

Venue <- c("Home",  "Away")
Goals <- c((hg_sum+hg_ecl_sum),(ag_sum+ag_ecl_sum))
df_sum_of_lg <- data.frame(Venue,Goals)


ggplot(df_sum_of_lg, aes(x="", y=Percentage, fill=Venue)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0) +
  theme_void()

hg_ecl_sum <- sum(master_ecl_csv_rev2[, "FT Home"])
ag_ecl_sum <- sum(master_ecl_csv_rev2[, "FT Away"])

total_goals <- hg_sum+hg_ecl_sum+ag_sum+ag_ecl_sum

hg_per <- ((hg_sum+hg_ecl_sum)/total_goals)
ag_per <- ((ag_sum+ag_ecl_sum)/total_goals)

df_sum_of_lg$Percentage <- c(hg_per,ag_per)

leg1_hg_ecl_sum <- sum(master_ecl_csv_leg1[, "FT Home"])
leg1_ag_ecl_sum <- sum(master_ecl_csv_leg1[, "FT Away"])
leg2_hg_ecl_sum <- sum(master_ecl_csv_leg2[, "FT Home"])
leg2_ag_ecl_sum <- sum(master_ecl_csv_leg2[, "FT Away"])

leg1_ecl_sum <- leg1_ag_ecl_sum+leg1_hg_ecl_sum
leg2_ecl_sum <- leg2_ag_ecl_sum+leg2_hg_ecl_sum