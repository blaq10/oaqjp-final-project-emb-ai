'''
This is the server file that prcesses requests sent in 
by the usuer
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    '''
    This returns the calculation of the emotion detector
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f'For the given statement, the system response is \'anger\': \
{emotions["anger"]}, \'disgust\': {emotions["disgust"]},\
 \'fear\': {emotions["fear"]}, \'joy\': {emotions["joy"]} \
 and \'sadness\': {emotions["sadness"]}. The dominant emotion is {emotions["dominant_emotion"]}.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
