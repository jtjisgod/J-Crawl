
from tkinter import *


def main():
    root = Tk()
    root.title('J-Crawl 1.0.0')
    root.resizable(width=False, height=False)

    w = 1000
    h = 530

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    frame1 = Frame()
    frame1.pack(fill=X)

    label_url = Label(frame1, text="Parent URL", width=10)
    label_url.pack(side=LEFT, padx=10, pady=10)

    input_url = Entry(frame1, width=100)
    input_url.insert(0, "http://")
    input_url.pack(side=LEFT, padx=10, pady=10)

    button_crawl = Button(frame1, text="CRAWL", width=50)
    button_crawl.pack(side=LEFT, padx=10, pady=10)

    frame2 = Frame()
    frame2.pack(fill=X)

    listbox = Listbox(frame2, selectmode=EXTENDED, height=23)
    listbox.pack(fill=BOTH, expand=1)

    frame3 = Frame()
    frame3.pack(side=RIGHT, fill=X)

    label_copyright = Label(frame3, text="Copyright (c) 2017 Copyright Holder All Rights Reserved.")
    label_copyright.pack(side=LEFT, padx=10, pady=10)

    WidgetNames = ['Button', 'Canvas',1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2,1,2,3,4,1,1,2]
    for widget in WidgetNames:
        listbox.insert(0, widget)

    root.mainloop()

if __name__ == '__main__':
    main()
