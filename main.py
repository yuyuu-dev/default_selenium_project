import os
import sys
import time
from selenium import webdriver

# APP実行パス
base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# ドライバパス
driver_path = os.path.join(base_path, "browser/chromedriver")

 # Headless Chromeをあらゆる環境で起動させるオプション
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-extensions')
# chrome_options.add_argument('--proxy-server="direct://"')
# chrome_options.add_argument('--proxy-bypass-list=*')
# chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('--headless')

# ブラウザ起動
driver = webdriver.Chrome(driver_path, options=chrome_options)
driver.implicitly_wait(10)


# サイトにアクセス
driver.get("")
time.sleep(3)


# いろんな処理をここに書く


# ブラウザを終了する
driver.quit()
