import webbrowser

# webbrowser.open("https://www.python.org/")
# help(webbrowser)

windows = webbrowser.get(using='windows-default')
windows.open_new_tab("https://www.python.org/")
