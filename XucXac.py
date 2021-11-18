import tkinter 
from PIL import Image, ImageTk  
import random  

# tên cửa sổ 
xuc_xac = tkinter.Tk() 
xuc_xac.geometry('400x400') 
xuc_xac.title('Tung Xúc Xắc')

# tên ứng dụng 
BlankLine = tkinter.Label(xuc_xac, text="")
BlankLine.pack() 

# thêm font và format 
HeadingLabel = tkinter.Label(xuc_xac, text="Chào! Tung Xúc Xác đi nè!", fg="light green", bg="dark green", font="Helvetica 16 bold italic")
HeadingLabel.pack()  

# Hình ảnh 
so_nut =['nut1.png', 'nut2.png', 'nut3.png', 'nut4.png', 'nut5.png', 'nut6.png']

# chọn ngẫu nhiên số nút và hình ảnh với số nút 
anh_so_nut = ImageTk.PhotoImage(Image.open(random.choice(so_nut)))

# tạo nhãn widget cho hình ảnh  
ImageLabel = tkinter.Label(xuc_xac, image=anh_so_nut)
ImageLabel.image = anh_so_nut 

# đóng gói widget hình ảnh
ImageLabel.pack(expand=True)

# hàm tung xúc xắc 
def tung(): 
    anh_so_nut = ImageTk.PhotoImage(Image.open(random.choice(so_nut)))
    # cập nhật ảnh 
    ImageLabel.configure(image=anh_so_nut)
    # giữ ảnh mới 
    ImageLabel.image = anh_so_nut 

# tạo nút tung xúc xắc 
nut = tkinter.Button(xuc_xac, text='Tung nè!', fg='blue', command=tung)

# đóng gói widget nút
nut.pack(expand=True)

# gọi vòng lặp chính và giữ cửa sổ
xuc_xac.mainloop() 
