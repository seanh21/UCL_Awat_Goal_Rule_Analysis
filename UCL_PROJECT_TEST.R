library(ggplot2)


h_a_goals_comp <- as.data.frame(t(summarized_ecl_data[, c("Total Home goals", "Total Away goals")]))
h_a_goals_comp$goals <- row.names(h_a_goals_comp)

leg_goals_comp <- as.data.frame(t(summarized_ecl_data[, c("Total 1st leg goals", "Total 2nd leg goals")]))
leg_goals_comp$goals <- row.names(leg_goals_comp)

f_leg_home_wins <- as.data.frame(t(summarized_ecl_data[, c("1st leg home wins", "1st leg home loses")]))
f_leg_home_wins$wins <- row.names(f_leg_home_wins)

s_leg_home_wins <- as.data.frame(t(summarized_ecl_data[, c("2nd leg home wins", "2nd leg home loses")]))
s_leg_home_wins$wins <- row.names(s_leg_home_wins)

e_p_wins <- as.data.frame(t(summarized_ecl_data[, c("Extratime and penalties wins", "Extratime and penalties loses")]))
e_p_wins$wins <- row.names(e_p_wins)

a_g_wins <- as.data.frame(t(summarized_ecl_data[, c("Away goals wins", "Away goals loses")]))
a_g_wins$wins <- row.names(a_g_wins)

