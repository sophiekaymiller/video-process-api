# Video Processing API 
**Sophie Miller**

Nov 20, 2019

## Instructions
- Create a REST api using a language and framework of your choice
- This API should have an endpoint to POST a message to process a video

The POST message should contain info about the video:
-   title
-   source
-   file name

Process the video using **ffmpeg (ffprobe)** to get the following information, the video's:
-   duration  
-   frame rate

Create a GET endpoint to retrieve the data


## Implementation
- Language: Python 3,
- Dependencies:
  - flask
  - ffmpeg

## Setup
1. clone or download .zip repository 
2. open terminal
3. cd /path/to/project-folder
4. python3 app.py
5. GET request to http://127.0.0.1:5000/ to confirm server functioning correctly
6. POST request to http://127.0.0.1:5000/videos with content below, or similar. 
   "filename" must be in ./video-test/ folder as this API is currently using in memory store.

      `{
        "filename": "./video-test/fall.mp4",
        "source": "source of video",
        "title": "title goes here"
      }`

7. GET request to http://127.0.0.1:5000/ to retrieve processed video data. 



  <hr/>
  
  #### Test Results
  
  POST to http://127.0.0.1:5000/videos:

    {
      "filename": "./video-test/fall.mp4",
      "source": "source of video",
      "title": "title goes here"
    }
  
  GET Request http://127.0.0.1:5000/
  
  **Output:**

    {
      "videos": [
          {
              "filename": "./video-test/fall.mp4",
              "meta": {
                  "info": {
                      "duration": 10.143467,
                      "fps": 29.97002997002997
                  }
              },
              "source": "source of video",
              "title": "title goes here"
          },
          {
              "filename": "videofile.mp4",
              "source": "source of video",
              "title": "title goes here"
          }
      ]
    }
