from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import json
import base64
import argparse
import time

parser = argparse.ArgumentParser(description='네이버 스마트스토어 매크로 for Mac M1 도움말')
parser.add_argument('--target', required=True, help='해당 상품 링크')
args = parser.parse_args()

def main():
    try:
        driver = get_driver()
        driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        config = get_config()
        id = base64.b64decode(config['userId'])
        id = id.decode("UTF-8")
        pw = base64.b64decode(config['userPw'])
        pw = pw.decode("UTF-8")
        login_naver(driver, id, pw)
        time.sleep(1)
        driver.get(args.target)
        print('Message: 상품 링크로 접속하였습니다.')
        macro_count = 1
        while(check_order(driver, macro_count)):
            macro_count += 1
            time.sleep(1)
            if macro_count > 9999:
                print("Message: 매크로 작동 가능 횟수를 넘어 프로그램이 종료됩니다.")
                break
    except Exception as e:
        print('Error: %s' % (str(e)))
    finally:
        driver.quit()

def get_config():
	try:
		with open('config.json') as json_file:
			json_data = json.load(json_file)
	except Exception as e:
		print('Error: in config file, {}'.format(e))
		return None
	else:
		return json_data

def login_naver(driver, id, pw):
    script = "                                      \
    (function execute(){                            \
        document.querySelector('#id').value = '" + id + "'; \
        document.querySelector('#pw').value = '" + pw + "'; \
    })();"
    driver.execute_script(script)
    driver.find_element_by_id("log.login").click()
    print("Message: 로그인 완료하였습니다.")
    return False

def get_driver():
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(3)
    return driver

def check_order(driver, macro_count):
    driver.refresh()
    try:
        driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/fieldset/div[9]/div[1]/div/a").click()
        print("Message: 현재 상품은 재고가 있습니다. 구매를 시도합니다.")
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/div[1]/form[1]/div/div[7]/button").click()
        time.sleep(20)
        print("Message: 성공적으로 구매하였습니다. 프로그램을 종료합니다.")
    except NoSuchElementException:
        print('Message: [%d][%s]%s' % (macro_count, driver.title, '현재 상품은 재고가 없습니다. 나중에 다시 시도해 주세요.'))
        return True

if __name__ == '__main__':
    main()