import pandas as pd
import matplotlib.pyplot as plt

##edit the reading to skip blanks, and warn of errors
failed_banks = pd.read_csv('banklist.csv', warn_bad_lines=True,error_bad_lines=True,skip_blank_lines=True)
failed_banks["Closing Year"] = 0

for i in range(len(failed_banks)):
    year = failed_banks.loc[i, "Closing Date"]
    year = int(year[-2:]) + 2000
    failed_banks.loc[i, "Closing Year"] = year

##print loco and snowfall?? for rows 35 to 40
print(failed_banks.iloc[35:41,0:2])

##figure name
plt.figure("Bank Information")

##subplot 1
plt.subplot(212)
plt.xlabel("Year")
plt.ylabel("Failures")
plt.title("FDIC Failed Banks")

failed_banks["Closing Year"].value_counts(sort=False).plot(kind="bar", color="violet")

##subplot 2
plt.subplot(211)
plt.xlabel('States')
plt.ylabel('Failures')
plt.title("FDIC Failed Banks")

failed_banks["ST"].value_counts(sort=True).plot(kind='bar', color = 'blue', width=.5, )

##fix the layout
plt.tight_layout()

##show
plt.show()
