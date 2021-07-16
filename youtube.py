from googleapiclient.discovery import build
api_key = 'AIzaSyAtHJLGKxFHUxv1iZ1cHUS9UvBdqEt0zBA'


class Youtube:
    def __init__(self, api_name='youtube', api_version='v3', api_key=api_key):
        self.api_name = api_name
        self.api_version = api_version
        self.api_key = api_key
        self.youtube = build(serviceName=self.api_name, version=self.api_version, developerKey=self.api_key)


    def search(self, param):
        result_list = []
        request = self.youtube.search().list(
            part='snippet',
            maxResults=1,
            q=param
        )
        response = request.execute()
        # results = response['items']
        print('NEXT PAGE TOKEN: ', response['nextPageToken'])
        return response
        # return self.gen_response(results)



    def response_obj(self, video_data, channel_data):
        d = {}
        d['title'] = video_data['title']
        d['channel'] = video_data['channel']
        d['thumbnail'] = video_data['thumbnail']
        d['subscribers'] = channel_data[0]['statistics']['subscriberCount']
        return d


    def gen_response(self, data):
        response_list = []
        for result in data:
            id = result['id']['videoId']
            video = self.video(id)[0]
            video_data = self.get_data(video)
            channel_id = video_data['channelId']
            channel_data = self.channel(channel_id)
            response_list.append(self.response_obj(video_data, channel_data))
        return response_list 


    def video(self, video_id):
        request = self.youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=video_id
        )
        response = request.execute()
        return response['items']


    def channel(self, id):
        request = self.youtube.channels().list(
            part='statistics',
            id=id
        )
        response = request.execute()
        return response['items']


    def get_data(self, video_obj):
        _d = {}
        stats = video_obj['statistics']
        snippet = video_obj['snippet']
        _d['id'] = video_obj['id']
        _d['likes'] = stats['likeCount']
        _d['views'] = stats['viewCount']
        _d['comments'] = stats['commentCount']
        _d['title'] = snippet['title']
        _d['description'] = snippet['description']
        _d['channel'] = snippet['channelTitle']
        _d['channelId'] = snippet['channelId']
        _d['thumbnail'] = snippet['thumbnails']['high']['url']
        return _d

    
    def gen_video_link(self, video_id):
        return f"https://www.youtube.com/watch?v={video_id}"


    def gen_channel_link(self, channel_id):
        return f"https://www.youtube.com/channel/{channel_id}"

    
    def display_dict(self, d):
        for key, value in d.items():
            print(type(value))
            if type(value) == 'dict':
                self.display_dict(value)
            print(key, ' : ',  value, '\n')


youtube = Youtube()
result = youtube.search('girls')

print(result)