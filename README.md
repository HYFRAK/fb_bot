# Facebook Automation Bot
***
An automated python bot that can perform the following
tasks: <br />
● Login to a Facebook account given ID and Password. <br />
● Add 1 friend from the same location as the location of the ID. <br />
● Update account status (text based). <br />
● Open timeline of a random friend and comment on the most recent post.
***
## Getting Started
***
Requirements :
Selenium 3.141.0
Chrome or Firefox
Webdriver Manager 3.3.0

Clone the repo using :
>%git clone https://github.com/HYFRAK/fb_bot.git

To install requirements, navigate to the folder and use (in terminal/command line) :
>%pip install -r requirements.txt
***
## Usage
***
#### To Login:
>%python3 bot.py --email-- --password--
#### To Login and Post a Story:
>%python3 bot.py --email-- --password-- -s --content of the story--
#### To Login and Write a Comment on a random friend's post:
>%python3 bot.py --email-- --password-- -c --content of the comment--
#### To Login and send a friend request to a random person of a person in the same location as the account:
>%python3 bot.py --email-- --password-- -f
#### Two or more arguments can also be passed simultaneously:
>%python3 bot.py --email-- --password-- -s --content of the story-- -f
#### Display Help
>%python3 bot.py --email-- --password-- -h
***
## Screenshots
![Login SS](https://drive.google.com/file/d/1gaskjO9I85lnMiISwdjYOdnqCL2LbOFB/view?usp=drivesdk)
![Comment SS](https://drive.google.com/file/d/1gVVAZKuGaXq87CisnXMoUmOYwApVihIH/view?usp=drivesdk)
![Friend Request SS](https://drive.google.com/file/d/1gW0T7tT1Cv-tnnRyJUgHZnrU_pKjnJOm/view?usp=drivesdk)
![Story SS](https://drive.google.com/file/d/1gbAnVQmdCeDsHyyH7O44z5RIqdSqBflw/view?usp=drivesdk)
***
## Authors
Ashish Hegde a.k.a Hyfrak
****
