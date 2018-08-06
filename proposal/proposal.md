# CSCI S-33a: Project Proposal
## Due: Friday, July 27 at 6pm

#### Your name

Jonathon O'Reilly

#### Your teaching fellow's name

Rodrigo Daboin Sanchez

#### Which language(s) will you use for your project?

Python and Javascript and SQL

#### What will (likely) be the title of your project?

What's Next TV

#### In just a sentence or two, summarize your project. (e.g. "A website that lets you check the weather in different cities.")

A website that lets you find and follow your favorite TV shows and movies.
Plus adding a collaborative where you and your friends can talk about the shows and movies.

#### Where will your project ultimately live? (e.g. within CS50 IDE, Heroku, AWS, some commerical web host...)

I plan on hosting this on Heroku.

#### In a paragraph or more, detail your project. What will it do? What features will it have?

  I plan on creating a project that interacts with the MovieDB API. A user will be able to browse
and search movies and TV shows through the application, having a search results page.
On the individual movie and show pages, a user will be able view comments
that other users make in the local application and view recommendations, which are generated
from a MovieDB endpoint. If the user creates an account and logs in, sign in and sign out functionality,
then the user with be able to leave a comment and a rating for a movie or tv show.
In the comment you can also tag another user. Plus you can favorite a tv show or movie to follow it.
  In the account portion of the site a user will be notified of the tag, via socketio,
and provided a link to that area. In addition, in the account the user will be able
to see all the posts that they have created. The users will also be able to update their password,
and track all the tv shows and movies that they have favorited. Both the comment and
the favorites section will able to be searched and viewed.

<hr>

- In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

#### In a sentence or list, define a GOOD outcome for your project. What WILL you accomplish no matter what?

Home Page
    - Trending Movies/movies in theaters (MovieDB endpoint) - Done
    - Trending TV Shows (MovieDB endpoint) - Done
Search Results
    - Searching for a movie or tv Show (MovieDB endpoint) - DONE
TV/Movie Detail Page
    - Details about a movie you selected (MovieDB endpoint) - WIP
    - Recommendations (MovieDB endpoint) - Done
    - Comments will go here and star review (Application comments DB table) - WIP
      - Add one comment for a logged in user
Account (Application User DB table)
    - Sign in - DONE
    - Sign up - DONE


#### In a sentence or list, define a BETTER outcome for your project. What do you THINK you will accomplish in time?
Home Page
  - If logged in (Application favorites DB table)
      - Your upcoming shows/ favorites
TV/Movie Detail Page
  - Ability to favorite/follow a movie or show (Application favorites DB table)
Account
    - List of your favorites
    - List of your comments


#### In a sentence or list, define a BEST outcome for your project. What do you HOPE you will accomplish in time?
TV/Movie Detail Page
  - Ability to tag a user (get users endpoint)
Account
  - Notifications from tags (Application notifications DB table)


#### In a paragraph or more, outline your next steps. What new skills do you need to acquire? What topics will you need to research?

  I will need to research the MovieDB API and acquire an API key. I will need to also research how other
applications generally do and store notifications and whether a notification has been acknowledge or not.
I would like to become a little more familiar to using travisci to deploy to Heroku.
I will need to start researching the most. In addition to the research above, I should be able
to get started with creating a home page and individual detail page templates,
plus the account template and search results area. I am still unsure at this point if
I will use flask or django.
