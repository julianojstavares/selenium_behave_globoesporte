from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.web = webdriver.Chrome(ChromeDriverManager().install())


def after_step(context, step):
    print()


def after_all(context):
    context.web.quit()
