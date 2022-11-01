import webbrowser

work_stacks = ["1. School","2. Work","3. Rap","4. Fun"]
school_stacks = ["1. Comp1406", "2. Comp2804", "3. Arcy1001","4. Cgse1001"]
chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

for option in work_stacks:
    print(option)
stack = int(input("What do you feel like doing today?: \n"))

if stack == 1:
    for option in school_stacks:
        print(option)
    school_stack = int(input("Which subject?: \n"))

    if school_stack == 1:
        webbrowser.get(chrome_path).open('https://brightspace.carleton.ca/d2l/home/161533')
    if school_stack == 2:
        webbrowser.get(chrome_path).open('https://brightspace.carleton.ca/d2l/home/143790')
        webbrowser.get(chrome_path).open("https://cglab.ca/~morin/teaching/2804/")
        webbrowser.get(chrome_path).open('https://www.plough.com/en/subscriptions/daily-prayer')

    if school_stack == 3:
        webbrowser.get(chrome_path).open('https://brightspace.carleton.ca/d2l/home/148032')
    if school_stack == 4:
        webbrowser.get(chrome_path).open('https://brightspace.carleton.ca/d2l/home/164816')

    webbrowser.get(chrome_path).open('https://www.youtube.com/watch?v=jfKfPfyJRdk')
    webbrowser.get(chrome_path).open('google.ca')

if stack == 2:
    webbrowser.get(chrome_path).open('https://www.edx.org/')
    webbrowser.get(chrome_path).open('google.ca')
    webbrowser.get(chrome_path).open('https://automatetheboringstuff.com/2e/')
    webbrowser.get(chrome_path).open('https://www.hackerrank.com/dashboard')
    webbrowser.get(chrome_path).open('https://outlook.office365.com/mail/')


if stack == 3:
    webbrowser.get(chrome_path).open('https://docs.google.com/document/u/0/')
    webbrowser.get(chrome_path).open('chrome://bookmarks/?id=202')
    webbrowser.get(chrome_path).open('rhymezone.com')

if stack == 4:
    webbrowser.get(chrome_path).open('https://www.merriam-webster.com/dictionary/no')







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
