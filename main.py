from flask import Flask, render_template, url_for, jsonify, request
from youtube import Youtube

app = Flask(__name__)

youtube = Youtube()

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_results = []
    video_name = request.args.get('video_name')
    location = request.args.get('location')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    location_tuple = (lat, lng)
    min_subsCount = int(request.args.get('min'))
    max_subsCount = int(request.args.get('max'))

    print('\nMax SubsCount: ', max_subsCount)
    max_subsCount = 10**10 if max_subsCount > 9999 else max_subsCount

    results = youtube.search(video_name, location_tuple, min_subsCount, max_subsCount)

    return render_template('results.html', results=results, search=video_name,
    min_subs=min_subsCount, max_subs=max_subsCount, location=location)
    




if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=9000)