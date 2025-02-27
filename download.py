

from yt_dlp import YoutubeDL
from pathlib import Path



def Download(urls ,path , is_it_playlist=False ,quality = 1080 ):

    playlist = is_it_playlist
    if path == "":
        path = "./downloads"
    

    if playlist :
        playlist_to_download = urls
    else:

        videos_to_download =[]+urls

    #? now check the quality
    if quality == "best quality":
        quality_format = 'bestvideo+bestaudio/best'
    elif quality in ['144' , '360' , '520' ,'560' , '720' ,'1080' , '1440', '2160' ,'2560', '4320']:
        quality_format = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'
    else:
        quality_format = 'bestvideo+bestaudio/best'
        print("quality not found, downloading the best quality available")


    # playlist_to_download = 'https://www.youtube.com/playlist?list=PLSbJLZl_TVkb7TAZjoJw57kQAuPjNNuJ8'
    # videos_to_download = ['https://www.youtube.com/watch?v=668nUCeBHyY',"https://www.youtube.com/watch?v=cdIs7VujZqs"]
    # # videos_to_download = []




    ydl_opts = {

            # 'ratelimit': 1000000,  # ! Limit to 1 MB/s
            'format': 'bestvideo+bestaudio/best', #? Get the best video and audio    #but u have to have  ffmpeg already installed
            # 'format': 'b',  #? Download the best single-file format (video + audio) , but in lower quality
            # 'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            # 'format':quality_format,


            # 'o
            # uttmpl': './downloads/%(title)s.%(ext)s',  # Output template
            'outtmpl': f'{path}/%(title)s.%(ext)s',  # Output template

            # 'noplaylist': True,  # Only download single video, not playlist
            'ignoreerrors': False,  # ! Skip errors
            # 'nooverwrites': True,  # Don't overwrite existing files

            # 'postprocessors': [{
            # 'key': 'FFmpegVideoConvertor',
            # 'preferedformat': 'mp4',  # Convert to MP4 format
            # }],
                    'format_sort': ['res:2560','res:1440','res:1080', 'res:720', 'res:480', 'res:360', 'res:240'],
            'verbose': True  ,# Show more debug info
            'merge_output_format': 'mp4',  # Merge into MP4 format

    }

    try:
        if playlist:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([playlist_to_download])
        else:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(videos_to_download)

    except Exception as e:
        print(f"Error downloading: {str(e)}")
        print(f"Try checking available formats with yt-dlp --list-formats {urls[0]}")


