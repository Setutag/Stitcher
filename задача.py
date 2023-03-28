import tkinter
import cv2
from tkinter import *
import tkinter.filedialog as fd
from PIL import Image, ImageTk

imgs_paths = []
images = {}


def choose_file1():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/users/lenovo/Desktop",
                                  filetypes=filetypes)
    images['filename1'] = filename
    image = Image.open(filename)
    resize_image = image.resize((540, 360))
    img = ImageTk.PhotoImage(resize_image)
    images['img1'] = img
    label1 = Label(frame1, image=images['img1'])
    label1.pack()


def choose_file2():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/users/lenovo/Desktop",
                                  filetypes=filetypes)
    images['filename2'] = filename
    image = Image.open(filename)
    resize_image = image.resize((540, 360))
    img = ImageTk.PhotoImage(resize_image)
    images['img2'] = img

    label2 = Label(frame2, image=images['img2'])
    label2.pack()


def stitcher():
    imgs = [cv2.imread(images['filename1']), cv2.imread(images['filename2'])]
    stitchy = cv2.Stitcher.create()
    (dummy, output) = stitchy.stitch(imgs)
    images['output'] = output
    if dummy != cv2.STITCHER_OK:
        print("stitching ain't successful")
    else:
        print('Your Panorama is ready!!!')
    save_file()
    cv2.imwrite(images['save_path'], output)
    image = Image.open(images['save_path'])
    # cv2.imwrite('final result.jpg', output)
    # image = Image.open('C:/Users/Odmen/PycharmProjects/Stitcher/final result.jpg')
    resize_image = image.resize((1080, 360))
    img = ImageTk.PhotoImage(resize_image)
    images['result'] = img
    label0 = Label(frame0, image=images['result'])
    label0.pack()


def save_file():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    save_path = fd.asksaveasfilename(title="Сохранить", initialdir="/",
                                     filetypes=filetypes, defaultextension=".jpeg")
    images['save_path'] = save_path
    cv2.imwrite(images['save_path'], images['output'])

window = Tk()
window.title("Stitcher")
window.geometry("1080x720")
frame0 = tkinter.Frame(master=window, height=360, borderwidth=1, relief=SUNKEN)
frame0.pack(fill=tkinter.BOTH, side=tkinter.BOTTOM, expand=True, anchor=CENTER)
frame1 = tkinter.Frame(master=window, width=540, height=360, borderwidth=1, relief=SUNKEN)
frame1.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
frame2 = tkinter.Frame(master=window, width=540, borderwidth=1, relief=SUNKEN)
frame2.pack(fill=tkinter.BOTH, side=tkinter.RIGHT, expand=True)

button1 = tkinter.Button(frame1, text="Выбрать файл", command=choose_file1)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
button2 = tkinter.Button(frame2, text="Выбрать файл", command=choose_file2)
button2.place(relx=0.5, rely=0.5, anchor=CENTER)
button0 = tkinter.Button(frame0, text="Сшить", command=stitcher)
button0.place(relx=0.5, rely=0.5, anchor=CENTER)
save_button = tkinter.Button(window, text="Сохранить", command=save_file)
save_button.place(relx=0.5, rely=0.95, anchor=CENTER)
window.mainloop()
