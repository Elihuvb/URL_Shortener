import pyshorteners

def run():
    inp = str(input("Please, enter your url: "))
    
    tp = pyshorteners.Shortener()
    short_url = tp.tinyurl.short(inp)
    
    print("Your URL is " + short_url)

if __name__ == '__main__':
    run()