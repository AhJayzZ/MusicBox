# Youtube影片下載器 Youtube Downloader

## 簡介 Introduction
每當遇到Youtube有好聽的音樂或者是影片時，總會想把音樂或者是影片下載下來保存，但是又不想每次重複打開Youtube搜尋或是翻找，此時便可透過本程式進行Youtube影片的下載，只需**輸入YT的影片網址，按下載即可轉換成.mp4並存放在本地電腦內**，同時支援撥放、刪除功能。

----------------------------------------

## 環境設定 Environment
- 1.本系統由**Python 3.7.8開發**
- 2.在終端機執行 ```pip install -r requirements.txt``` 安裝會使用到的套件
- 3.使用工具:
    - 簡易撥放套件:```moviepy==1.0.3```
    - 簡易顯示套件:```pygame==2.0.1```
    - YT影片轉mp4套件:```pytube==11.0.1```

----------------------------------------

## 功能介紹 Functions
- ### 更新清單:```music_list_update()``` 
- ### 撥放影片:```music_play()```
- ### 刪除影片:```music_delete()```
- ### 下載條更新:```download_progress_bar()```
- ### 下載影片與名稱:```get_music_name()```

----------------------------------------

## 成果 Result
- ### 使用說明:
    **輸入Youtube網址按下載即可進行.mp4檔案的下載**
    
- ### 使用步驟
    ![](https://i.imgur.com/gwDfKXC.png)

- ### 下載成功
    ![](https://i.imgur.com/wwHEs7L.png)
    
- ### 下載失敗
    ![](https://i.imgur.com/ucLKLIU.png)

