import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('Download', 'Download completed.')
            button1.config(state=tkinter.NORMAL)

    def download():
        # disable download button
        button1.config(state=tkinter.DISABLED)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('Abort', 'Author: Tom.chen(v0.1)')

    top = tkinter.Tk()
    top.title('MutiThread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='Abort', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()