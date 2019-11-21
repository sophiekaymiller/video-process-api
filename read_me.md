## Instructions
- Create a REST api using a language and framework of your choice
- This API should have an endpoint to POST a message to process a video

### The message should contain info about the video:

-   title
-   source
-   file name

Process the video using **ffmpeg (ffprobe)** to get the following information, the video's:
-   duration  
-   frame rate

## Implementation
- Language: Python 3,
- Dependencies:
  - flask
  - ffmpeg
  - argparse
-


  ### **Test** success with POST to http://127.0.0.1:5000/videos:

    {
      "filename": "./video-test/fall.mp4",
      "source": "source of video",
      "title": "title goes here"
    }

Create a GET endpoint to retrieve the data
GET http://127.0.0.1:5000/
all videos with duration and fps:

  #### Output:

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
