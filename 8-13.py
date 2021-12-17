from pytube import YouTube

url = 'https://www.youtube.com/watch?v=yZIummTz9mM&list=LL&index=5&ab_channel=LinkinPark'
yt = YouTube(url)
print("開始下載")
yt.streams.first().download()
print("下載完成")