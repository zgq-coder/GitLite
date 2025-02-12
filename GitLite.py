import git
from git import repo
import easygui
import tkinter
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk
import webbrowser

repo = repo.Repo()


def init_Git():
    Git_path = easygui.diropenbox('open Git path')
    repo.init(Git_path)


def add_file():
    git.Repo(easygui.diropenbox('open Git path'))
    file_path = easygui.fileopenbox('open file path')
    repo.index.add([file_path])
    commit_message = 'Added another file'
    repo.git.commit('-m', commit_message)


def Git_log():
    commits = list(repo.iter_commits('master'))
    for commit in commits:
        print('Commit Hash:', commit.hexsha)
        print('Author:', commit.author)
        print('Author Time:', commit.authored_datetime)
        print('Committer:', commit.committer)
        print('Committer Time:', commit.committed_datetime)
        print('Message:', commit.message)


def showGitinfo():
    messagebox.showinfo('Git Info', 'developer: liuhan\nGit version: 2.47.1.windows.2')


def clone():
    clone_name = easygui.enterbox('clone name:', 'clone Git')

    def check_remote_repo_exists(repo_url):
        try:
            result = subprocess.run(['git', 'ls-remote', repo_url], capture_output=True, text=True)
            if result.returncode == 0 and result.stdout.strip():
                return True
            else:
                return False
        except Exception:
            print(f"An error occurred: {Exception}")
            return False

    if check_remote_repo_exists(clone_name):
        os.system(f'git clone {clone_name}')
    else:
        messagebox.showerror('error', 'clone error\nfatal: repository ' + clone_name + 'does not exist')


def open_web():
    webbrowser.open('https://git-scm.com')


def open_cmd():
    os.system('git')
    open_web()


def UI():
    root = tkinter.Tk()
    root.title('Git')
    root.geometry('600x380')
    root.iconbitmap('favicon.ico')
    Button = tkinter.Button(root, text='init Git', command=init_Git, width=10, height=2)
    Button.pack(anchor=tkinter.W)
    Button = tkinter.Button(root, text='add_file', command=add_file, width=10, height=2)
    Button.pack(anchor=tkinter.W)
    Button = tkinter.Button(root, text='Git log', command=Git_log, width=10, height=2)
    Button.pack(anchor=tkinter.W)
    Button = tkinter.Button(root, text='quit', command=sys.exit, width=10, height=2)
    Button.pack(anchor=tkinter.W)
    Button = tkinter.Button(root, command=showGitinfo, bitmap='info', width=74, height=40)
    Button.pack(anchor=tkinter.W)
    Button = tkinter.Button(root, text='clone', command=clone, bitmap='hourglass', width=512, height=39,
                            compound=tkinter.LEFT)
    Button.pack()
    Button.place(x=80, y=0)
    Button = tkinter.Button(root, text='Git help', command=open_cmd, bitmap='question', width=90, height=120,
                            compound=tkinter.LEFT)
    Button.pack()
    Button.place(x=501.7, y=47)

    image = ImageTk.PhotoImage(Image.open('logo@2x.png'))
    Label = tkinter.Label(root, image=image, width=220, height=92)
    Label.pack()
    Label.place(x=150, y=80)

    def populate_tree(parent, directory):
        for p in os.listdir(directory):
            path = os.path.join(directory, p)
            if os.path.isdir(path):
                iid = tree.insert(parent, 'end', text=p, open=False)
                populate_tree(iid, path)
            else:
                tree.insert(parent, 'end', text=p)
    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill=tkinter.BOTH)
    path = easygui.diropenbox('open Git path')
    populate_tree('', path)
    Label = tkinter.Label(root, text='path: ' + path, width=0, height=0)
    Label.pack()
    Label.place(x=80, y=210)
    root.mainloop()
if __name__ == '__main__':
    UI()