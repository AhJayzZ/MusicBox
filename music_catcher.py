import os
import pygame                            
from tkinter import *       
from pytube import YouTube
from moviepy.editor import VideoFileClip

#創建目錄與音樂資料夾
download_path = os.path.join(os.path.dirname(__file__),'mp4_downloads')
if not os.path.isdir(download_path):
    os.mkdir(download_path)
print("MP4 download path:",download_path)

#抓取目錄下所有歌曲
def music_list_update() :
    allFileList=os.listdir(download_path)
    listbox.delete('0','end')
    for musicFile in allFileList :
        listbox.insert('end',musicFile)

#播放歌曲
def music_play() :
    music_name=str(listbox.get(listbox.curselection()))
    music_path= str(download_path) + "\\" + str(music_name)
    music_playing_label=Label(root,text="正在播放:"+music_name,font=('標楷體',14),bg='red')
    music_playing_label.grid(row=8,column=0,sticky=W)
    music_playing_label.update()
    music_list_update()
    #print(music_path)
    #print('正在播放:',music_name)

    pygame.display.set_caption(music_name)
    clip=VideoFileClip(music_path)
    clip.preview()
    clip.close()
    pygame.quit()

    music_playing_label.grid_forget()
    music_list_update()

#刪除歌曲
def music_delete() : 
    music_name=str(listbox.get(listbox.curselection()))
    music_path= str(download_path) + "\\" + str(music_name)
    os.remove(music_path)
    music_list_update()

#下載進度條
def download_progress_bar(stream,chunk,bytes_remaining) :
    label_download=Label(root,text="0% downloaded",font=('標楷體',16),bg='red')
    #size = videoSize - bytes_remaining
    #download_bar=('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size*20/videoSize), ' '*(20-int(size*20/videoSize)), float(size/videoSize*100)))
    percent = 100*(videoSize - bytes_remaining) / videoSize
    label_download['text']=("{:00.0f}% downloaded".format(percent))
    label_download.grid(row=6,column=0,sticky=W)
    label_download.update()


#------------------------------------------------------
#Youtube下載影音
def get_music_name() :
    input_url=str(entry.get())
    label_warning=Label(root,text=("正在下載中..."),font=('標楷體',14),bg='red')
    label_warning.grid(row=5,column=0,sticky=W,pady=10)
    try  :
        video = YouTube(input_url,on_progress_callback=download_progress_bar)
        video_type = video.streams.filter(progressive=True,file_extension="mp4").first()
            
        global videoSize 
        videoSize = video_type.filesize
        video_type.download(download_path)  

        listbox.insert('end',video.title)
        label_warning['text']=("下載完成,影片長度:" + str(video.length) + "秒,歌曲:" + str(video.title))
    except :
        label_warning['text']="發生錯誤!"

    music_list_update()   
    label_warning.update()
    entry.delete('0',END)


#------------------------------------------------------

#創建GUI介面
root = Tk()                                             #創建根介面
root.title("MP4 Downloader ")                     #設定標題名稱
root_width,root_height=(600,650)                        #初始視窗大小
fix_width,fix_height=(50,20)                           #修正視窗初始位置
root.geometry(str(root_width)+'x'+str(root_height)+'+'+str(fix_width)+'+'+str(fix_height))     #設定視窗大小(可以補增+x+y調整初始位置)

#顯示背景圖片
root.configure(bg='pink')

#------------------------------------------------------

#字元標籤設置
label=Label(root,text="請輸入要下載的Youtube網址:",font=('標楷體',14),bg='pink')           #設定顯示字元與字體             
label.grid(row=0,column=0,sticky=W)                                                  #定位label 


#輸入框設置
entry=Entry(root,font=('標楷體',12),width=60)        #新增輸入框
entry.grid(row=1,column=0,sticky=W)         #定位輸入框 
button_clear=Button(root,text="清除",font=('標楷體',14),command=lambda:entry.delete('0',END))  
button_clear.grid(row=1,column=0,sticky=W,padx=500) 

#列表框設置
scrollbar=Scrollbar(root)
scrollbar.grid(row=2,column=0,sticky=N,padx=570)                #位置不好調,不要亂動
listbox=Listbox(root,font=('標楷體',12),width=70,height=20)     #設定Listbox
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar['command']=listbox.yview
listbox.grid(row=2,column=0,columnspan=3,sticky=W)                       #  columnspan表示要橫跨幾行

#下載按鈕設置
button_download=Button(root,text="下載",font=('標楷體',16),command=lambda:get_music_name())  #設定下載按鈕的屬性
button_download.grid(row=3,column=0,sticky=W,pady=10)                   #sticky表示黏住:N表北方,S表南方,E表東方,W表西方

#播放按鈕設置
button_play=Button(root,text="播放",font=('標楷體',16),command=lambda:music_play())          #設定播放按鈕的屬性
button_play.grid(row=3,column=0,sticky=W,padx=80,pady=10)                       #sticky表示黏住:N表北方,S表南方,E表東方,W表西

#刪除按鈕設置
button_play=Button(root,text="刪除",font=('標楷體',16),command=lambda:music_delete())          #設定刪除按鈕的屬性
button_play.grid(row=3,column=0,sticky=W,padx=160,pady=10)                       #sticky表示黏住:N表北方,S表南方,E表東方,W表西

#離開按鈕設置
button_exit=Button(root,text="離開",font=('標楷體',16),command=lambda:exit(0))          #設定離開按鈕的屬性
button_exit.grid(row=3,column=0,sticky=W,padx=240,pady=10)                       #sticky表示黏住:N表北方,S表南方,E表東方,W表西

#------------------------------------------------------

#顯示GUI
if __name__ == '__main__' :
    entry.focus()
    music_list_update()
    root.mainloop()

