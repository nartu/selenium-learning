from time import sleep
from selenium import webdriver

def main():
    chromedriver_path_snap = '/snap/bin/chromium.chromedriver'
    # chrome://version Parent
    chrome_user_data_dir = '/home/julia/snap/chromium/common/chromium/Default'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir="+chrome_user_data_dir)
    # chrome_options.add_argument("--password-store")
    driver = webdriver.Chrome(executable_path=chromedriver_path_snap, chrome_options=chrome_options)
    driver.get('https://ya.ru/')
    sleep(100)


if __name__ == '__main__':
    main()
