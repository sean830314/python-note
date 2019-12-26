import time
import tkinter
import tkinter.messagebox


def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('Download', 'Download completed.')


def show_about():
    tkinter.messagebox.showinfo('Abort', 'Author: Tom.chen(v0.1)')


def main():
    top = tkinter.Tk()
    top.title('Single')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='Abort', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()