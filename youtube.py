from googleapiclient.discovery import build
api_key = 'AIzaSyAtHJLGKxFHUxv1iZ1cHUS9UvBdqEt0zBA'
# api_key = 'AIzaSyDVRjlPcJiSscO7KxkkfOmAAS1Ksoy6YrY'


class Youtube:
    min_results = 15
    max_results = 500

    def __init__(self, api_name='youtube', api_version='v3', api_key=api_key):
        self.api_name = api_name
        self.api_version = api_version
        self.api_key = api_key
        self.youtube = build(serviceName=self.api_name, version=self.api_version, developerKey=self.api_key)


    def get_search_data(self, response_items):
        results = []
        if not response_items:
            return []
        for res in response_items:
            video_id = res['id'].get('videoId', None)
            if video_id is None:
                continue
            video_link = self.gen_video_link(video_id)
            video_item = self.video(video_id)
            channel_id = video_item['snippet']['channelId']
            channel_link = self.gen_channel_link(channel_id)
            channel = self.channel(channel_id)

            data = {}
            snippet = res['snippet']
            
            data['title'] = snippet['title']
            data['thumbnail'] = snippet['thumbnails']['high']['url']
            data['channel'] = snippet['channelTitle']
            data['channel_link'] = channel_link
            data['video_link'] = video_link
            data['subscribers'] = int(channel['statistics'].get('subscriberCount', 0))

            results.append(data)
        return results


    def filter_search_results(self, results, min, max):
        return list(filter(lambda x: x['subscribers'] > min and x['subscribers'] <= max, results))
    

    def search(self, param, location, min=0, max=10**10):
        result_list = []
        search_args = dict(part="snippet", maxResults=self.max_results, q=param, type="video",
            location=f"{str(location[0])},{str(location[1])}", locationRadius="10mi")
        if not all(location):

            print('\n\n Removed locations \n\n')
            search_args.pop('location')
            search_args.pop('locationRadius')
        request = self.youtube.search().list(**search_args)
        response = request.execute()
        video_data = self.get_search_data(response['items'])
        result_list = self.filter_search_results(video_data, min, max)
        return result_list
    

    def search_example(self, param):
        results = []
        counter = 0
        token = None                
        while len(results) < 7:
            request = self.youtube.search().list(
                part='snippet',
                maxResults = 2,
                q=param,
                type="video",
                pageToken=token
            )
            response = request.execute()
            token = response['nextPageToken']
            results.extend(self.run_details(response['items']))
            counter += 1
            print('Counter: ', counter)

        for i in results:
            print(i, '\n')


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
        return response['items'][0]


    def channel(self, id):
        request = self.youtube.channels().list(
            part='statistics',
            id=id
        )
        response = request.execute()
        return response['items'][0]


    def get_data(self, video_obj):
        _d = {}
        stats = video_obj['statistics']
        snippet = video_obj['snippet']
        _d['id'] = video_obj['id']
        _d['views'] = stats['viewCount']
        _d['title'] = snippet['title']
        _d['channel'] = snippet['channelTitle']
        _d['channelId'] = snippet['channelId']
        _d['thumbnail'] = snippet['thumbnails']['high']['url']
        return _d

    
    def gen_video_link(self, video_id):
        return f"https://www.youtube.com/watch?v={video_id}"


    def gen_channel_link(self, channel_id):
        return f"https://www.youtube.com/channel/{channel_id}"

