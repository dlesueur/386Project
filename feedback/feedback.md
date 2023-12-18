# Peer Feedback and Revision Descriptions For 386 Project

## Research Topic
I considered doing many topics for my project. The top three that I was the most interested in were studying where people take the most outdoor runs, what music I listen to the most often at different times of day or different times of the year, and the correlation between wins and player heights in the NBA.

When I talked to TAs, my classmates, and others the general consensus was that any of the projects would be interesting. I decided to do the NBA project because I was able to find the best API for that data. After talking to my group, I decided to expand my research to also compare in-season and post-season performances for each team and see what variables affect those outcomes. 

## Data Collection Blog Post Feedback
Initial commit SHA number: eded9641289a1ea17568c77abd1f840ec4c89fa3

Ty commented that he liked the casual language I used throughout my post and that it made the data collection process seem less intimidating. He pointed out a few typos to me that I was able to fix. He also recommended I use the full word parameters instead of params for clarity. I changed a few of the typos he mentioned and changed that word params. After his comments, I decided to try to use pretty colloquial language in my EDA blog post as well. 

Nate said the blog post was easy to read. He said he wished it was centered on the page which I am looking into fixing but I'm not exactly sure how to change the css for that yet.

William said he thought my data collection blog post was super clear. He said he is "confident he could follow the tutorial with ease" which made me feel good about how I presented my process. 

I believe that my blog post was enhanced by this feedback by making the post more professional by fixing typos and making a few words more clear. After recieving the feedback, I went back and read the whole blog post myself too and was able to change a few formatting things to make the post more cohesive. I think that allowed me to make a better post!

## EDA Blog Post Feedback
Initial commit SHA number: b953d2c0aa59ce86ad3248babd3e7da0d2ea62a0

Ty recommended a few things for my EDA graphs to change the looks of the graphs so they are more readable. Specifically with the histograms, he mentioned that the way my bins were set up, they weren't landing on an integer which doesn't make sense with the data I chose. He also recommended I add a trend line on the scatterplots. I changed the bins and added the trend line. He mentioned it might be nice to have a correlation coefficient listed as well, which I agree is very useful from a stats perspective, but my target audience is less stats-pilled so I decided not to include that.  

Sfolkman4 said it would be interesting to see some kind of a time series for this data. I agree with this, and will consider adding this in the future when I modify this as a personal project. For this project assignment though, I'm happy with how I concluded. 

Isaac said he liked how I concluded my EDA post. He said his project was using similar data and he felt the same as what I explained in my post, that you can explore this data forever. He thought the amount of exploration I included was sufficient. 

I agreed with all of the above comments that I should add a trendline to each of the plots. After going through and adding these, it made the graphs more interesting and made my overall post more interesting as well. I also changed the bins for some of the histograms. 

## Streamlit Application Feedback

William suggested that instead of having the team abbreviations listed, I include the entire team name to make it more accessible to those who aren't familiar with the abbreviations. He also said some of the graphs were missing titles, so I made sure to go check where the titles were missing from my code and include those. 

Sfolkman4 on discord agreed that it would be nice to have the entire team name to make the plot more readable. He also suggested maybe making each dot the team's color to be able to distinguish. For the time being, I am going to keep all the dots the same color but I am looking into how to give them each a specific color like I did for the histogram on the team data page. 

My husband said he thought the dashboard was pretty interesting and easy to use. He said it would be nice to have more user inputs, so I am going to add one for position to see each box plot for a specific position. He also talked about finding more information to put on the teams page which I am going to look into. 

Based on all of this feedback, I did another look through of my code and made sure everything had titles. I also decided to add explanations for some of the graphs, to mix up some description and words between each of the visuals. I added another user input for position. I also added the same trend lines and changed the bin widths just as I did with my EDA blog post.

A challenge I faced when making this dashboard was that all the graphs I had made in my EDA were incompatible with streamlit. After changing one to the synax of another package, it got pretty easy to change  them all considering most of my visualizations were scatterplots. I wished that I had done my EDA and the dashboard side-by-side because I felt like I was doing a lot of work twice when I could have just done it once in my EDA and then immediately put it on my dashboard. I also had a hard time making the dashboard as complete as I wanted to. There were some more trend lines that I wanted to add that I ran out of time to include. 