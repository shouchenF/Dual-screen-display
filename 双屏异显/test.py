# import tkinter as tk
# import threading
# import pygetwindow as gw
# import subprocess
# import cv2
#
# class Window1:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry('200x100+0+0')
#         self.root.title('Window 1')
#
#         # 创建一个文本框和按钮用于输入文字
#         self.entry = tk.Entry(self.root)
#         self.entry.pack()
#
#         self.button = tk.Button(self.root, text="发送", command=self.send_text)
#         self.button.pack()
#
#         # 绑定回车键事件
#         self.entry.bind('<Return>', self.send_text)
#
#         # 添加控制开关的按钮
#         self.switch_button = tk.Button(self.root, text="打开开关", command=self.open_switch)
#         self.switch_button.pack()
#
#     def send_text(self, event=None):
#         text = self.entry.get()
#         # 在窗口2中显示输入的文字
#         global text_label
#         text_label.config(text=text)
#         # 清空文本框内容
#         self.entry.delete(0, tk.END)
#
#     def open_switch(self):
#         # 打开视频
#         try:
#             video_path = "C:/Users/Fengzhen/Videos/全向步态视频/侧向步态.mp4"
#             threading.Thread(target=open_video, args=(video_path,)).start()
#
#             window = gw.getWindowsWithTitle("Video")[0]  # 替换为实际窗口标题
#             # # 设置窗口位置
#             # window.moveTo(2000, 100)
#         except Exception as e:
#             print(e)
#
#         # 在窗口2中显示开关状态
#         global switch_label
#         switch_label.config(text="开关已打开")
#
# class Window2:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry('200x100+2000+0')
#         self.root.title('Window 2')
#
#         # 创建一个标签用于显示文字
#         global text_label
#         text_label = tk.Label(self.root, text="")
#         text_label.pack()
#
#         # # 创建一个标签用于显示开关状态
#         # global switch_label
#         # switch_label = tk.Label(self.root, text="开关已关闭")
#         # switch_label.pack()
#
# def open_video(file_path):
#     try:
#         # 使用cv2读取视频
#         cap = cv2.VideoCapture(file_path)
#
#         # 创建窗口并设置位置
#         cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
#         cv2.moveWindow("Video", 3000, 100)
#
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break
#
#             # 在指定位置显示视频帧
#             cv2.imshow("Video", frame)
#
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#
#         cap.release()
#         cv2.destroyAllWindows()
#
#     except Exception as e:
#         print(e)
#
# def create_windows():
#     window1 = Window1()
#     window2 = Window2()
#     window1.root.mainloop()
#     window2.root.mainloop()
#
# # 创建一个线程用于创建窗口
# thread = threading.Thread(target=create_windows)
#
# # 启动线程
# thread.start()
#
# # 等待线程结束
# thread.join()
#


import subprocess
import threading
import time

def clone_display():
    subprocess.Popen('displayswitch.exe /extend', shell=True)

# 在主线程中启动克隆显示的子线程
clone_thread = threading.Thread(target=clone_display)
clone_thread.start()

# 等待一段时间以确保操作完成
time.sleep(5)
