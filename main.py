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
    print(f'\n{request.args}\n')
    if request.method == 'POST':
        search_params = request.get_json()
        search_results = youtube.search(search_params['search'])    
        return jsonify({'results': search_results})
    return jsonify({'data': 'received'})
    




if __name__ == '__main__':
    app.run(debug=True, port=9000)