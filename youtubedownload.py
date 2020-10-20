from tkinter import * #import 之後星號表示所有名稱，這使我們在程式中可以直接使用 tkinter 中的名稱，不需要連帶寫出 tkinter
from PIL import Image
from PIL import ImageTk

#主視窗建立
window = Tk() #創建視窗
window.title("下載youtube影片")  #視窗標題
window.geometry('1024x768')  #視窗大小
window.configure(background="white") #視窗背景顏色，可用顏色名or sRGB值
window.iconbitmap('YouTube.ico') #設定主視窗的icon,圖片需跟程式碼所在的資料夾放在一起

#顯示youtube圖片
img=Image.open("youtube.png") # image打開圖片檔 *.png,*.jpg
new_width  = 300 #調整圖片檔的寬
new_height = 300 #調整圖片檔的高
img = img.resize((new_width, new_height), Image.ANTIALIAS) #ANTIALIAS：平滑濾波。對所有可以影響輸出像素的輸入像素進行高質量的重採樣濾波，以計算輸出像素值。這個濾波器只用於改變尺寸和縮略圖時適用。 注意：ANTIALIAS濾波器是下採樣（例如，將一個大的圖像轉換為小圖）時唯一正確的濾波器。BILIEAR和BICUBIC濾波器使用固定的輸入模板，用於固定比例的幾何變換和上採樣是最好的。
img=ImageTk.PhotoImage(img) #建立一個Tkinter相容的照片影象（photo image），它可在Tkinter期望一個影象物件的任何地方使用。
imLabel=Label(window,image=img) #Label原本是要加tkinter模組的名稱，但因為前面import時用了＊，所以可以不用寫出來
imLabel.pack() #pack() 函數就是一個版面管理員, 它會由上而下擺放元件，也可以呼叫 grid() 函數使用網格版面來管理元件 ：Label.grid(column=0,row=0)


window.mainloop() #loop因為是迴圈的意思，window.mainloop就會讓window不斷的重新整理，如果沒有mainloop,就是一個靜態的window,傳入進去的值就不會有迴圈，mainloop就相當於一個很大的while迴圈，每點選一次就會更新一次，所以我們必須要有迴圈，視窗檔案都必須有類似的mainloop 