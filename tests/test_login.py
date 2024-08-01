import time
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

def test_login():
    # Load environment variables from .env file
    load_dotenv()
    
    # Retrieve credentials from environment variables
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        main_page = MainPage(page)
        login_page = LoginPage(page)

        page.goto("https://www.hackerrank.com/")  # Navigate to HackerRank
        
        main_page.go_to_login()                   # Perform actions using page objects
        page.wait_for_load_state('networkidle')
        
        main_page.click_developer_login()
        page.wait_for_load_state('networkidle')

        login_page.fill_credentials(email, password)   # Fill credentials and submit login form
        login_page.submit_login()

        # Print status message
        print("Login Button clicked")
        time.sleep(10)
        browser.close()
