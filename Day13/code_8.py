import time
import tkinter
import tkinter.messagebox

def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')

# 显示信息
def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

def main():
    # 建议一个页面
    top = tkinter.Tk()
    # 标题
    top.title('单线程')
    # 窗口大小
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    # 面板
    panel = tkinter.Frame(top)
    # 下载 按钮
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    # 关于 按钮
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()