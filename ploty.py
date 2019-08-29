import pandas as pd 
import matplotlib.pyplot as plt

fileName = "./convertcsv.xlsx" 

sheet = "Sheet 1"

df = pd.read_excel(io=fileName, sheet_name=sheet)

goalTimes = ["0-15", "16-30", "31-45", "46-60", "61-75", "76-90"]
goalsEachSection = [] 

for col in df.columns[1:7]:
	df[col] = df[col].str.split('-').str.get(0)
	num = df[col].astype(int).sum()
	goalsEachSection.append(num)
	print(num)

plt.plot(goalTimes, goalsEachSection, color='grey')
plt.xlabel('Time interval in game')
frame1 = plt.gca()
frame1.axes.get_yaxis().set_visible(False)
frame1.spines['top'].set_visible(False)
frame1.spines['right'].set_visible(False)
frame1.spines['left'].set_visible(False)

plt.title('# of goals scored in specific interval')


for i,j in zip(goalTimes,goalsEachSection):
	if i == '31-45':
		plt.annotate(str(j), xy=(i,j), verticalalignment='top', horizontalalignment='left', xytext=(i, (j + 25)))
	else:
		plt.annotate(str(j), xy=(i,j), verticalalignment='top', horizontalalignment='left', xytext=(i, (j)))

plt.show()

fig1, ax1 = plt.subplots() 
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#b0e0e6', '#f08080']
ax1.pie(goalsEachSection, colors=colors, labels=goalTimes, pctdistance= float(.57), autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})


centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.tight_layout()
plt.show()


