from flask import Flask, jsonify, request, Response
import ffmpeg
import argparse


# parser = argparse.ArgumentParser(description='Get video information')
# parser.add_argument('title', help='Input title')
# parser.add_argument('source', help='Input source')
# parser.add_argument('filename', help='Input filename')

app = Flask(__name__)

# init videos dictionary
videos = [
    {'title':'title goes here',
    'source':'source of video',
    'filename':'videofile.mp4'
    }
    ]

v_info = [
    {
    'duration': 10.143467,
    'fps': 29.97002997002997
    }
]

#GET All video video (title, source, filename, duration and fps)

@app.route('/')
def index():
  return jsonify({'videos': videos[:]})


# Define valid input message object
def validInputMessage(inputMessage):
    if ("title" in inputMessage and "source" in inputMessage and "filename" in inputMessage):
        return True
        print("Video Added")
    else:
        return False

# POST /videos: endpoint to process and store original input, with added duration and frame rate information.

@app.route('/videos', methods=['POST'])
def post_video():
    request_data = request.get_json()
    if(validInputMessage(request_data)):

        video_in = {
            "title": request_data['title'],
            "source": request_data['source'],
            "filename": request_data['filename'],
        }

        process = ffmpeg.probe(video_in["filename"])

        video_stream = next((stream for stream in process['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)

        # temp frames per second (string)
        t_fps = str(video_stream['r_frame_rate'])
        # temp duration (string)
        t_dur = str(video_stream['duration'])

        # convert fps and duration to float
        fps = eval(t_fps)
        dur = eval(t_dur)

        # stage temp video information dictionary for nesting in videos dictionary

        t_v_info = {
            "duration": dur,
            "fps": fps
        }

        video_in["meta"] = {}
        video_in["meta"]["info"] = t_v_info

        videos.insert(0, video_in)


        response = Response("Video Inserted", 201, mimetype='application/json')
        response.headers['Location'] = "/videos/" + )
        return response
    else:
        invalidInputErrorMsg = {
            "error": "Invalid message passed in request",
            "helpString": "Data passed in similar to this {'title': 'video title', 'source':'video source', 'filename':video.mp4}"
        }
        response = Response(json.dumps(invalidInputErrorMsg), status=400, mimetype='application/json')
        return response

app.run(port=5000)
