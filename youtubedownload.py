#1.建立主視窗（設定主視窗大小、縮放和主視窗標題）。
#2.將元件（如：圖片、文字方塊、按鈕、下載清單等）放入主視窗中，實作事件處理函式，例如：點擊按鈕時會觸發什麼。
#3.啟動主視窗。

#from tkinter import * #import 之後星號表示所有名稱，這使我們在程式中可以直接使用 tkinter 中的名稱，不需要連帶寫出 tkinter
import tkinter as tk #上一段等開發經驗熟練之後再嘗試
from PIL import Image
from PIL import ImageTk


#建立主視窗
window = tk.Tk() #創建視窗
window.title("下載youtube影片")  #視窗標題
window.geometry('1024x768')  #視窗大小
window.configure() #視窗背景顏色，可用顏色名or sRGB值  語法為background="yellow"
window.iconbitmap('YouTube.ico') #設定主視窗的icon,圖片需跟程式碼所在的資料夾放在一起

#顯示youtube圖片 元件
img=Image.open("youtube.png") # image打開圖片檔 *.png,*.jpg
new_width  = 300 #調整圖片檔的寬
new_height = 300 #調整圖片檔的高
img = img.resize((new_width, new_height), Image.ANTIALIAS) #ANTIALIAS：平滑濾波。對所有可以影響輸出像素的輸入像素進行高質量的重採樣濾波，以計算輸出像素值。這個濾波器只用於改變尺寸和縮略圖時適用。 注意：ANTIALIAS濾波器是下採樣（例如，將一個大的圖像轉換為小圖）時唯一正確的濾波器。BILIEAR和BICUBIC濾波器使用固定的輸入模板，用於固定比例的幾何變換和上採樣是最好的。
img=ImageTk.PhotoImage(img) #建立一個Tkinter相容的照片影象（photo image），它可在Tkinter期望一個影象物件的任何地方使用。
imLabel=tk.Label(window,image=img) #若是用from tkinter import * 就可以不用寫出tk
imLabel.pack() #pack() 函數就是一個版面管理員, 它會由上而下擺放元件，也可以呼叫 grid() 函數使用網格版面來管理元件 ：Label.grid(column=0,row=0)


#網址輸入區域＆下載清單 元件
#設定"提示文字"要顯示的區域
input_frm=tk.Frame(window,width=640,height=60) #建立一個寬640,高60的表格 
input_frm.pack() #擺放Frame

#設定提示文字內容
lb=tk.Label(input_frm,text="請輸入欲下載的youtube網址",fg="black")  #將input_frm放入標籤內，並輸入提示文字內容
lb.place(rely=0.2,relx=0.5,anchor="center") #tkinter有三種排版方式 pack()、grid()、place()。place()通常是用來製作客製化的版面管理員之用，詳細可以看http://yhhuang1966.blogspot.com/2018/10/python-gui-tkinter_12.html








#啟動主視窗
window.mainloop() #loop因為是迴圈的意思，window.mainloop就會讓window不斷的重新整理，如果沒有mainloop,就是一個靜態的window,傳入進去的值就不會有迴圈，mainloop就相當於一個很大的while迴圈，每點選一次就會更新一次，所以我們必須要有迴圈，視窗檔案都必須有類似的mainloop 