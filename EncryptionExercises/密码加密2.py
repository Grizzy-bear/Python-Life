from tkinter import *
import tkinter as tk

class MyDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("加密.....")
        self.setup_UI()
    def setup_UI(self):
        row = tk.Frame(self)
        row.pack(fill="x")
        # row.geometry('400x400')
        tk.Label(row, text="密码:", width=15).pack(side=tk.LEFT)
        self.password = tk.StringVar()
        tk.Entry(row, textvariable=self.password, width=20).pack(side=tk.LEFT)
        
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="加密", command=self.cryTo).pack(side=tk.RIGHT)

# 加密部分
    def cryTo(self):
        self.passwordCryTo= self.password.get()
        self.destroy()

    def cancel(self):
        self.passwordCryTo = None
        self.destroy()

# main
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("加密")
        self.name = "请先设置......"
        self.setupUI()
    
    def setupUI(self):
        row = tk.Frame(self)
        row.pack(fill="x")
        tk.Label(row, text="加密后:", width=8).pack(side=tk.LEFT)
        # self.name = tk.StringVar()
        self.l1 = tk.Label(row, text=self.name, width=20)
        self.l1.pack(side=tk.LEFT)
        
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="设置", command=self.setup_config).pack(side=tk.RIGHT)

    def setup_config(self):
        res = self.ask_passwordCryTo()
        if res is None:return
        self.name = res
        self.l1.config(text=self.name)
    
    def ask_passwordCryTo(self):
        inputDialog = MyDialog()
        self.wait_window(inputDialog)
        return inputDialog.passwordCryTo

if __name__ == '__main__':
  app = MyApp()
  app.mainloop()


# root = Tk()
# root.title("密码加密")
# root.geometry('200x400')
# root.resizable(width=True, height=True)

