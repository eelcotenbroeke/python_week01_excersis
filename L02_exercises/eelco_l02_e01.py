import datetime

try:
    f = open("C:\\Users\\eelco\\Desktop\\ITC\\week0708_myPortfolio\\L02_exercises\\log_files\\my_log.txt", "a")
except Exception as e:
    print(e)
    x = datetime.datetime.now()
    f.write(x.strftime("%d/%m/%Y, %H:%M:%S") + " general error\n")


