# ReCaptcha
import undetected_chromedriver as webdriver
import os, time, json

def RunProfile(type):
    # chrome://version/
    profile = 'C:\\Users\\abdul\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 16'
    options = webdriver.ChromeOptions()
    if type == 'hcaptcha':
        options.add_argument(f'--load-extension={os.path.abspath("hekt")}')
    else:
        options.add_argument(f'--load-extension={os.path.abspath("hekt2")}')
    options.add_argument(f"--user-data-dir={profile}")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def ReCaptcha(key, url):
    script = """
    const newBody = document.createElement('body');
    const recaptchaDiv = document.createElement('div');
    recaptchaDiv.classList.add('g-recaptcha');
    recaptchaDiv.dataset.sitekey = '{}';
    const script = document.createElement('script');
    script.src = 'https://www.google.com/recaptcha/api.js';
    newBody.appendChild(recaptchaDiv);
    newBody.appendChild(script);
    document.documentElement.replaceChild(newBody, document.body);
    """.format(key)

    driver = RunProfile('recaptcha')
    # driver.execute_script("window.open('" +url+ "')")
    driver.get(url)

    while True:
        try:
            res = driver.execute_script("return document.querySelector('.g-recaptcha').dataset['sitekey']")
            if res == key:
                break
        except:
            driver.get(url)
            time.sleep(5)
            driver.execute_script(script)
            time.sleep(3)
    
    while True:
        try:
            user_agent = driver.execute_script("return navigator.userAgent")
            res = driver.execute_script("return document.getElementById('g-recaptcha-response').value")
            data = {
                'Solution': res,
                'User-Agent': user_agent
            }
            if res != '':
                driver.quit()
                return {'status': True, 'data': json.dumps(data)}
            else:
                time.sleep(3)
        except:
            time.sleep(3)
            continue

def HCaptcha(key, url):
    script = """
    const hcaptchaSiteKey = '{}';
    const newBody = document.createElement('body');
    const hcaptchaDiv = document.createElement('div');
    hcaptchaDiv.classList.add('h-captcha');
    hcaptchaDiv.dataset.sitekey = hcaptchaSiteKey;
    const script = document.createElement('script');
    script.src = 'https://hcaptcha.com/1/api.js';
    newBody.appendChild(hcaptchaDiv);
    newBody.appendChild(script);
    document.documentElement.replaceChild(newBody, document.body);
    """.format(key)
    driver = RunProfile('hcaptcha')
    # driver.execute_script("window.open('" +url+ "')")
    driver.get(url)


    while True:
        try:
            res = driver.execute_script("return document.querySelector('.h-captcha').dataset['sitekey']")
            if res == key:
                break
        except:
            driver.get(url)
            time.sleep(3)
            driver.execute_script(script)
            time.sleep(5)

    while True:
        try:
            user_agent = driver.execute_script("return navigator.userAgent")
            res = driver.execute_script("return document.getElementById(document.getElementsByName('g-recaptcha-response')[0].id).value")
            data = {
                'Solution': res,
                'User-Agent': user_agent
            }
            if res != '':
                driver.quit()
                return {'status': True, 'data': json.dumps(data)}
            else:
                time.sleep(5)
        except:
            time.sleep(3)