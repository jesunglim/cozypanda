from tkinter import *
from tkinter import ttk

def domenu():
    print("OK")

root = Tk()
root.title('Tool')
root.geometry("300x500")

menubar = Menu(root)                                # 윈도우에 메뉴바 추가
filemenu = Menu(menubar, tearoff=0)                 # 상위 메뉴 탭 항목 추가
menubar.add_cascade(label="File", menu=filemenu)    # 상위 메뉴 탭 설정
filemenu.add_command(label="New", command=domenu)   # 항목 추가
filemenu.add_command(label="Open", command=domenu)
filemenu.add_command(label="Save", command=domenu)
filemenu.add_command(label="Save as...", command=domenu)
filemenu.add_separator()                            # 분리선 추가
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy", command=domenu)
editmenu.add_command(label="Paste", command=domenu)
editmenu.add_separator()
editmenu.add_command(label="Delete", command=domenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=domenu)

root.config(menu=menubar)             # 생성된 객체를 위에서 생성된 메뉴바에 연결    

hierachyFrame = ttk.LabelFrame(root)
hierachyFrame.grid(row=0, column=0)
hierachy = ttk.Label(hierachyFrame, text="Heirachy")
hierachy.grid(row=0, column=0)

inspectorFrame = ttk.LabelFrame(root)
inspectorFrame.grid(row=0, column=1)
inspector = ttk.Label(inspectorFrame, text="Inspector")
inspector.grid(row=0, column=1)

projectFrame = ttk.LabelFrame(root)
projectFrame.grid(row=1)
project = ttk.Label(projectFrame, text="project")
project.grid(row=1)
project.pack()

root.mainloop()