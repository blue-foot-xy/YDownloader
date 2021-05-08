import os

import youtube_dl
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse


def download_media(links, save_path, quality,
                   writesubtitles, dl_format, single_download):

    # creating a download folder if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if 'audio' in dl_format:
        dl_format = 'bestaudio/best'
    else:
        dl_format = 'bestvideo[ext=mp4][height<=' + quality[:-1] + ']+bestaudio[ext=m4a]/best'

    # Splitting down playlist links
    links = get_rid_of_playlist(links, single_download)

    download_count = 1
    
    for link in links:
        try:         
            ydl = youtube_dl.YoutubeDL()
            file_name = ydl.extract_info(link, download=False)['title']
            
            if not single_download: 
                file_name = str(download_count) + '_' + file_name
                download_count+=1

            options = {
                'outtmpl'       : file_name,
                'format'        : dl_format,
                'writesubtitles': writesubtitles,
                'noplaylist'    : True
            }

            ydl = youtube_dl.YoutubeDL(options)
            ydl.download([link])

            # moving the media file to the download path
            try:
                move_to_downloads_folder(save_path, file_name, '.mp4')
            except:
                move_to_downloads_folder(save_path, file_name)

            # moving the caption to the download path
            if writesubtitles:
                move_to_downloads_folder(save_path, file_name,
                                         '.en.vtt')
        except Exception:
            print("Error downloading video")


def move_to_downloads_folder(save_path, file_name, extension=''):
    try:
        current_path = os.path.realpath(file_name + extension)
        file_path = os.path.join(save_path, file_name + extension)
        os.rename(current_path, file_path)
    except Exception:
            print("Problem while moving to the downloads path.")


def get_rid_of_playlist(links, single_download):
        for link in links:
            try:
                if 'list' in link:
                    links = links + break_playlist(link,
                        single_download=single_download)
                    links.remove(link)
            except Exception:
                print('Problem while processing the playlist.')

        return links


def break_playlist(url, single_download=False):
        brokendown_links = []
        query = parse_qs(urlparse(url).query, keep_blank_values=True)
        playlist_id = query["list"][0]
        youtube = googleapiclient.discovery.build("youtube", "v3",
                                                   developerKey=get_api_key())
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50
        )
        response = request.execute()
        playlist_items = []
        while request is not None:
            response = request.execute()
            playlist_items += response["items"]
            request = youtube.playlistItems().list_next(request, response)
        brokendown_links.append([
            f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}'
            for t in playlist_items
        ])
        brokendown_links = brokendown_links[0]

        if single_download == False:
            return brokendown_links
        else:
            return [brokendown_links[int(query['index'][0]) - 1]]
            
            
def get_api_key():
    with open('key.txt') as f:
        key = [line.rstrip() for line in f]
    return key[0]
