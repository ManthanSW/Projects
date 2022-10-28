from pytube import YouTube
YouTube('https://youtu.be/CCSGelSCPGE').streams.first().download()