from PIL import Image, ImageTk
import tkinter

root = tkinter.Tk()
img = Image.open('C:\\Users\\QIXQI\\Desktop\\wallpaper\\1.jpg')
img = img.resize((1200, 800), Image.ANTIALIAS)
img_png = ImageTk.PhotoImage(img)
canvas = tkinter.Canvas(root, width=1200, height=800, bg='pink')
canvas.pack()
canvas.create_image(0, 0, anchor='nw', image=img_png)
# label_img = tkinter.Label(root, image=img_png)
# label_img.pack()
root.mainloop()

# root = tkinter.Tk()
# image = Image.open(r"C:\\Users\\QIXQI\\Desktop\\wallpaper\\1.jpg")
# img = ImageTk.PhotoImage(image)
# l = tkinter.Label(root, image=img)
# l.pack()
# root.mainloop()