<!-- ![GitHub Contributors Image](https://contrib.rocks/image?repo=ervoramihir/social-media-app) -->


<h1 align="center"><b>Social Media App</b></h1>

<p align="center">
  <img src="media/logo/websiter-logo.png" alt="socail-media-app">
</p>
<h5 align="center">
  <b>Live Demo</b>
</h5>
<h1 align="">
  <b>Introduction</b>
  <br/>
</h1>

<p align="justify"
  social media application is a 'microblogging(It allows you to send posts known as ‘tweepy’. We can share photos, videos, and Caption(up to 1000 characters in length. ) on The Mumble with our followers)'.


After the online sign-up or Login process, users can sharing photos and videos with Type your caption(Get creative and write a nice, interesting caption to go with your photo and Video.) called "tweepy". Then your followers can see your post then your followers can Like(Clicking Like Button below a post on Mumble way to let people know that you enjoy it without leaving a comment. Just like a comment, anyone who can see the post can see that you liked it and The person who posted the video will get a notification that you liked it.When you like something, this lets us know to show you other content that we think you’d also like to see) or DisLike(If you dislike your post, it means that the user did not like your post - image or video and caption) and Comment(Below every posts there are “Comment” buttons. If the image has any recent comments they will appear below those posts. Comments allow your followers to write a comment on your post. Users are notified if you “Comment” their post.) on your post.



You can search for User accounts using the search bar. then tap Search then choose whether you're looking for Users. You can search people by their Name or Username.



Followers (When you tap the follow button, the person will receive a notification that you followed them and Followers on Mumble are the users that follow you; these followers can see your posts on both your profile. ... Following refers to the list of users that you follow on The Mumble; these users' posts appear on your feed).

UnFollow When you follow someone on The Mumble, that user's Tweepy appear in your feed and, if you want to remove them from your feed, you must unfollow them. If you have multiple users that you wish to unfollow, this means seeking out each user individually and clicking the "Unfollow" button next to their username

Following(Following refers to the list of users that you follow on The Mumble; these users' posts appear on your feed, and you have access to view their profile if you want).



At the top of the your profile page, you should see three numbers. One indicates how many posts you have ("posts"), another indicates how many people are following you ("followers"), and another indicates how many people you're following ("following"). Tap the "followers" number, and it should open to a list of the accounts that are following you.
</p>

<h1>
  <b>Technology Stack</b>
</h1>

* Frontend Tech : HTML, BOOSTRAP, CSS, JS
* Web FrameWorkd : Django
* Database : SQLite3
* API : RESTful API

<h1>
  Functionality
</h1>

1. Create New Account 
    - Username
    - Email
    - Password
    - Password confirmation

2. User Profile
    - indicates how many  posts you have ("posts")
    - indicates how many people are following you ("followers")
    - indicates how many people you're following ("following")
    - Other User Able To see Your Profile and Show the your Follower and Following People and  Posts in Your Account
    - You Can Follow Another User Account and also You can Unfollow to User Account 
3. User Edit  Your Profile Account
    - Add  Header(Background Image) Avatar
    - Add Profile Pic
    - Add Account Bio
    - Change Email Id
    - Change Username
    - Delete Account

4. User Can Tweepy(POSTS)
    - User Can Do  Add Either Image or Video with caption or without Caption can do
    - User Can Do Updating Posts
    - User Can Also Do Delete Posts
   
5. User Can Like, Dislike, Comments On Posts
    - User Can Do Likes On Posts  and Remove Like On Posts
    - User Can Do Dislikes On Posts and Remove dislike On Posts
    - User Can Do Comment On Posts
    - Other User See The Total Like and Dislike 
    - Other User Read The Comments on Posts

6. Search User Account
    - You can search people by their name or username

7. Creating API(Using REST APIs)
    - Creating public API  Meaning, third-party apps can  access the API from Mumble without permission.
 
## Setup

1. Git Clone the project with: ```git clone https://github.com/ervoramihir/social-media-app.git```.

2. Move to the base directory: ```cd social-media-app```

3. Create a new python enveronment with: ```python3 -m venv env```.

4. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python3 manage.py migrate```.

7. Run app localy with: ```python3 manage.py runserver```.

