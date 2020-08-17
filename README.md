# Spotify-Song-Recommender
Song Recommendations using Spotify API

### To Run the Application:

There are three ways this application can be run.

1. Use the Dockerfile:
Ensure you have Docker installed in your system. Then run the following commands after cloning this repository onto your local machine:

   * docker build -t spotifyrecapp:latest .

   * docker images (check if the image has been created)

   * [Optional step] docker run -it spotifyrecapp /bin/sh
 
     /# python3 (checks if installation was done correctly)
 
     /# pip (checks if installation was done correctly)
 
   * docker run -d -p 5000:5000 --name track-recommender spotifyrecapp:latest
 
   * docker ps (check if container is now created)

2. Run the application directly from the code:

   * Run webapp.py

 _To start using the application by using either of the two methods, go to http://0.0.0.0:5000/_
   
   
3. Docker pull:

   * docker push palsmadhu/spotify-song-recommender:tagname

