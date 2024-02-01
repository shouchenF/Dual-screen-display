import os
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import pygetwindow as gw
import time
import screeninfo


def get_mp4_files(directory):
    mp4_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                mp4_files.append(os.path.join(root, file))
    return mp4_files


def play_video(mp4_file):
    os.startfile(mp4_file)
    # 等待打开的窗口出现
    time.sleep(0.6)
    # 获取所有窗口
    windows = gw.getAllWindows()
    # 获取副屏幕的尺寸
    screen = screeninfo.get_monitors()[1]  # 假设副屏幕是第二个屏幕
    screen_width = screen.width
    screen_height = screen.height
    # 遍历窗口，找到指定的窗口
    for window in windows:
        print(window.title)
        if "迅雷影音" in window.title:  # 替换为你想要找到的窗口标题
            # 将窗口移动到副屏上
            window.moveTo(3000, 10)

            # 设置窗口大小为副屏幕大小
            window.resizeTo(screen_width, screen_height)

            # 最大化窗口
            window.maximize()

            break



def display_mp4_icons(directory):
    mp4_files = get_mp4_files(directory)

    root = tk.Tk()
    root.title("MP4 Files")
    root.attributes("-fullscreen", True)  # 设置为全屏显示

    # 转换图片为PhotoImage格式
    # 加载背景图像
    background_image = tk.PhotoImage(file="photo/background.png")

    photo = background_image.zoom(2, 2)
    # 将PhotoImage对象作为参数传递给Label控件
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(relx=0.5, rely=0.5, anchor="center")  # 将图像居中显示

    # 创建一个具有所需字体大小的字体对象
    font = tkFont.Font(size=18)

    def create_play_video_handler(mp4_file):
        def play_video_handler(event):
            play_video(mp4_file)
        return play_video_handler

    for i, mp4_file in enumerate(mp4_files):
        icon_image = Image.open("photo/video.png")  # 替换为你自己的图标
        icon_image = icon_image.resize((200, 200), Image.ANTIALIAS)  # 修改图标大小
        icon_photo = ImageTk.PhotoImage(icon_image)

        icon_label = tk.Label(root, image=icon_photo)
        icon_label.image = icon_photo
        icon_label.grid(row=i // 4, column=i % 4, padx=10, pady=5, ipady=1)  # 调整图标和字体之间的距离
        icon_label.bind("<Button-1>", create_play_video_handler(mp4_file))

        filename_label = tk.Label(root, text=os.path.basename(mp4_file))
        filename_label.grid(row=i // 4 + 1, column=i % 4, padx=10, pady=2, ipady=1)  # 调整图标和字体之间的距离
        filename_label.bind("<Button-1>", create_play_video_handler(mp4_file))



    root.mainloop()


directory = "C:/Users/Fengzhen/Videos/全向步态视频"  # 替换为你想要遍历的文件夹路径
display_mp4_icons(directory)
