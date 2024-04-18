import youtube_manager as yt
from pytube import YouTube, Stream

# Create a new instance of the YouTubeManager class
manager = yt.YouTubeManager()

# Search for youtube videos
youtube = manager.search('Charlie Chaplin - Boxing Match')

for video in youtube:
    print(video.title)
    manager.path = 'Videos'
    manager.create_path()
    manager.download_video(manager.get_lowest_resolution(video))
    break

# if you encounter an error like Unexpected renderer encountered, you can fix it by adding the following lines to the search.py file
"""
under this line
# Skip "recommended" type videos e.g. "people also watched" and "popular X"
#  that break up the search results

put the following lines

if 'reelShelfRenderer' in video_details:
    continue
    
"""
