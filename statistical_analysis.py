import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from ggplot import ggplot, aes, geom_boxplot

data = pd.read_csv("attention_merged_results.csv")

model = smf.mixedlm("Reaction_Time ~ C(Color)", data, groups=data["Participant_ID"])
results = model.fit()

# Display the results
print(results.summary())

p = ggplot(data, aes(x='attention', y='reactionTime')) + geom_boxplot()
print(p)
