# from pyvirtualdisplay import Display
from selenium import webdriver

def main():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("disable-infobars")
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    chromedriver_path = '/home/julia/Program/selenium/webdrivers_90/chromedriver'
    chromedriver_path_snap = '/snap/bin/chromium.chromedriver'
    # driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
    driver = webdriver.Chrome(executable_path=chromedriver_path_snap)
    driver.get('http://ya.ru')
    print(driver.title)

if __name__ == '__main__':
    main()
