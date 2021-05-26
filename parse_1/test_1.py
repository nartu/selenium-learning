from time import sleep
from selenium import webdriver

def main():
    chromedriver_path_snap = '/snap/bin/chromium.chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path_snap)
    driver.get('http://ya.ru')
    print(driver.title)
    button = driver.find_elements_by_css_selector(".button_theme_websearch")
    print(button)
    button[0].click()
    sleep(3)


if __name__ == '__main__':
    main()
