# Soccer Goal Time Visualization

## Project Description
I and started getting curious how goals were distributed during the game. Essentially, I thought of this as a "If I'm watching soccer, what time periods do I absolutely have to put my phone down and watch the game" guide.

Here's how the project broke down: 
* Take every goal scored in the English Premiere League between 2012-2019 and the minute interval it was scored during
..* Minute intervals were: 1-15, 26-30, 30-45, 45-60, 61-75, 76 - 90
* Export that data into a spreadsheet 
* Read the spreadsheet with a Python script running Pandas, make the data all nice
* Feed the data into a matplotlib visualization that visually shows when the most goals are being scored

## Project Analysis
From the data, it clearly shows that the most goals are scored during the last interval of the game. Nearly a quarter of all EPL goals are scored during that final interval + second half stoppage time. 

![image](https://user-images.githubusercontent.com/18202690/63980858-b0edcb00-ca71-11e9-86f7-216f81b59f38.png)

## Project Issues and Challenges
* One issue was only getting to use the last 7 years worth of data. I would've loved to get more data to experiment with.
* The 31-45 and 76-90 intervals also account for stoppage time, which absolutely pads the data in their favor. The EPL is notorious for stoppage time goals. Apparently, 6.3% of EPL goals in the 2016-17 season were made during second half stoppage time (via [ESPN](http://www.espn.com/soccer/blog/tactics-and-analysis/67/post/3170967/why-premier-league-has-more-stoppage-time-goals-than-other-top-leagues)). EPL games have an average 8 minutes of stoppage time per game. That's wild. 
* If I could do this project over again, I wish I could get the exact time stamp for each goal and do a visualization by minute instead of time intervals. It would greatly help in separating regulation and stoppage time numbers for a clearer picture of what's going on. 
* Side note: From a design standpoint, I really did not like the default colors matplotlib assigned for each section of the pie chart. They were super dark and made the chart look like a mess. After reading some design blogs, I learned that lighter colors that compliment each other are the way to go for a more pleasing pie chart. Good to know. 
## Built with:
* Python
* matplotlib
* pandas 
* Data provided by: [soccerstats.com](http://www.soccerstats.com) 🙏🏽




