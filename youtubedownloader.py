from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=LhwHYWHS46s") #想下載的影片連結
yt.streams.first().download() #下載影片  youtube的每部影片可能有多種不同格式供使用者下載，通常選第一種下載即可。download()方法默認會將影片下載至跟你的程式同一個資料夾中。



