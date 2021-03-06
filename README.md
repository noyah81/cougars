# Welcome to the P5Cougars Repository
# Website Guide
Our website is a New York attractions website for tourists who need transportation information and details on where they might want to go.

Our website starts off with the home page displaying 6 key New York locations. Under the array of photos there is an input location for comments. In the comments input section there is a field for the user's name, a dropdown with a selection of locations, and a large text box for comments. Under the input section, there is a section where the comments are recorded. At the very top, the navigation bar has sections linked to each location information page. Each location page has a picture of the attraction and a button linked to the directions. The comments from the home page are sorted onto each attraction page. Each attraction page only has the comments inputted for that single, specific location from the home page wheras the home page has all comments. Under the comments on the attraction page, there is a list of subway stations that are around that specified location. If the user types in "/stations" in the search bar, a list of subway stations pops up with all New York stations used with the website.  
 
### Groups Table

| Trio 1 Calvin Ni, Megan Corrigan, Noya Hafiz  | 
| ------------- | 
| Calvin Github User : statsprojectlol |
| Megan  Github User : MeganCorrigan |  | 
| Noya Github User : noyah81| 

Week of 2/17
# AP requirements in our code 
-Inputs (form to insert name and comment) : https://github.com/noyah81/cougars/blob/main/templates/home.html#L40

-Outputs (comments section) : https://github.com/noyah81/cougars/blob/main/templates/home.html#L70

-Lists (nav bar): https://github.com/noyah81/cougars/blob/main/templates/base.html#L35n

-Procedures (database): https://github.com/noyah81/cougars/blob/main/main.py#L72

-Algorithms (if then statements) : https://github.com/noyah81/cougars/blob/main/main.py#L148

## Crossover suggestions and implentation
-Team Candy suggested we organize our code so we have implemented more comments to distinguish parts of code, especially to home.html: https://github.com/noyah81/cougars/blob/main/templates/home.html

-Another suggestion made was to add a dropdown menu for the CRUD locations input so that the user can't enter whatever location they want. There is now a dropdown for all the locations featured on our website to limit the inputs: https://github.com/noyah81/cougars/blob/main/templates/home.html#L44

-orgnanization of the home page images was fixed (previously, the pictures were different sizes): https://github.com/noyah81/cougars/blob/main/templates/home.html#L14

-The inputs are only submitted and outputted once (previosly, the input would come out twice if the page was refreshed): https://github.com/noyah81/cougars/blob/main/templates/home.html#L83

# Current tickets and code review
#### [Project Plan Link](https://docs.google.com/document/d/12MikN6erqEzmTGDvZh2lsmTSRd4t44Dd1UiFS7VQ7ao/edit?usp=sharing)
#### [Easter Egg Link](http://76.176.49.121/easter)
#### [Backlog Link](https://github.com/noyah81/cougars/projects/1)
#Changes Log

Week 8 
- linked the easter egg on README 
- web server is able to be accessed remotely 
- Calvin's Tickets [Ticket 1](https://github.com/noyah81/cougars/projects/1#card-53783399) 
- [Calvin's other Ticket ](https://github.com/noyah81/cougars/projects/1#card-53719223)
- Noya's Tickets[Ticket](https://github.com/noyah81/cougars/projects/1#card-53719212)
- Megans Tickets[Ticket](https://github.com/noyah81/cougars/projects/1#card-53870814)



## A. Completed Tickets & Scrumboard
-Data Stuff: Calvin collected sample data that will be implemented on website through integration. This data will be extracted and used to provide information for the user on when it's extracted.

-Flask Installation: Basic format of a website created for collaborative work. This was done by Megan and Noya. 

-Interface Building: Planning on what the website will look like is apart of interface building. The interface was built by Noya. Calvin initally helped with establishing the routes.

-nstall Gunicorn: Gunicorn is used to run python; it stores files. This was installed and implented within our project. Calvin installed Gunicorn. 

-Templating: Templating includes files under the "templates" folder. Within this folder is multiple html files with code from pages that were initally made as static webpages for each interest point. This templates folders holds information on each interest point and contains the code for the navigation bar. Noya worked on templating. 

-Install Jinja & Bootstrap: Bootstrap was implemented on to our website to make the interface more freindly. We added aspects of bootstrap within the code (used in home.html, madisonsquare.html...). This was done by Megan and Noya

-RPi: Worked on deploying the website, done by Megan

-In progress:

   -Webpage Art: The styling of the webpage is not yet finished. We will continue to work on this in the future by adding login information, pictures on the home page, and links to stations tops under the dropdown. 

   -New York Bus Timetable and New York Subway Timetable: Calvin continues to find exact timings for transportation routes for different stations. He's still collecitng some data to add to our website that the user can search for the nearest station and the website can provide route information for each station.
   
   -Website Name: Getting the website to have a name rather than just an IP address. Being worked on by Megan.

## B. Link to Code
https://github.com/noyah81/cougars.git

## C. Instruction on how to evaluate
#### How to run: 
-Running through IntelliJ, click on link to website

-The link takes the user to the home page where the site is introduced. 

-Up top there is a nav where with interest points linked

-When the user clicks on the interest point they want, the website leads to a page with information on each of the interest points

-On each infromation page there is a picture of the site, a button linking to directions to the location, and a short description of the site

## D. Deployment
-In Progress
-Currently only able to run on a local network. Once public IP is achieved, just need to switch out the IP address then it will be finsihed.

#### About the code:
-empire.html, time.html, liberty.html, madisonsqaure.html, museum.html, statue.html: establish the informational pages

   -bootstrap for Jumbotron photos centered 
   
   -bootstrap for button linking to directions
   
-home.html: runs the main page ("welcome" page for users upon clicking link)

   -form for users (Bootstrap) to input emails and sites they visited
   
-base.html: established navigation bar

   -dropdown menu coded here for stations
   
-main.py: establishes routes

   -takes user to the page they want to access (html pages under "templates") from navigation bar 

### Group Accomplishents (Week of 1/11)
-Established nav bar

-Routes fixed

-Sample Data acquired

-Rasberry Pi set up

### Things in Progress
- API creation

- Directory




### Assignments

Noya :
README
Create website template to add data 

Wenshi: looking for errors in code throughout project


Megan :
Scrum board updates
Updating assignments and completed tasks
Embed link for backlog
Deployment of website

Calvin:
Data scraping
Implementing scraped data into a usable form for our goal
Create API



### Backlog of Git

[Backlog](https://github.com/noyah81/cougars/projects/1)


### **College Board Requirements**


#### CB Big Idea #1 Creative Development:

Work on a database where you can insert an input and get an output. For this group specifically, we are aiming to create a query that allows people in New York to get information on the subways. 

#### CB Big Idea #2 Data: 

To get the data we need for this webapp, we will need to first get points of intrest in New York that can be reached through a subway. Then we will use a New York subway database to get variables such as departure and arrival times so that the user can reach the point of interest at given time. This allows for the user to plan out their day easier

#### CB Big Idea #3 Algorithms and Programming:
 
Using HTML, CSS and JavaScript, an appealing website will be made. This will attract clients to want to come to our website and explore it a bit. Using what we learned last trimester, we will be able to apply that to our new website.

#### CB Big Idea #4 Computer Systems and Networks:
Using a Raspberry Pi, this group will create a server to run the website, then use HTTP to allow for someone to request data.

####  CB Big Idea #5 Impact of Computing:

Some impacts our project will have on society is knowledge on transportation, especially to those foreign on the use of subways. Travelers will be able to look up times and plan their trips. An impact on the locals is that it helps them plan for attending important events and jobs.
