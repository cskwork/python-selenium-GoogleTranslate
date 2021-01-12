import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
text_box = input
text_box = input_translated

"""

class MyApp:

    def __init__(self, parent):
        def open_file():
            print('opened')
            """Open a file for editing."""
            filepath = askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not filepath:
                return
            self.text_box.delete(1.0, tk.END)
            with open(filepath, "r") as input_file:
                text = input_file.read()
                self.text_box.insert(tk.END, text)
            self.title(f"Text Editor Application - {filepath}")

        def save_file():
            print('saved')
            """Save the current file as a new file."""
            filepath = asksaveasfilename(
                defaultextension="txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )
            if not filepath:
                return
            with open(filepath, "w") as output_file:
                text = self.text_box2.get(1.0, END)
                output_file.write(text)
            print(filepath)
            self.title(f"Text Editor Application - {filepath}")

        #번역 로직
        def translate_file():
            print('번역')
            text = self.text_box.get(1.0, tk.END)

            #구글 번역 실행
            driver = webdriver.Edge('./msedgedriver.exe')
            driver.get("https://translate.google.co.kr/?hl=ko")

            search_input_box = driver.find_elements_by_css_selector("[aria-label='원본 텍스트']")

            print(search_input_box)
            # search_input_box[0].send_keys(text)
            #query = WebDriverWait(self.text_box, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='원본 텍스트']")))
            #search_input_box[0].send_keys(text)
            #WebDriverWait(self.text_box, 5).until(lambda text_box: query.get_attribute('value') == text)
            #self.text_box.find("button")

##--------------------------------------------
            # enter a url inside quotes or any other value to send
            url = text
            # initialize the input field as variable 'textField'
            textField = driver.find_elements_by_css_selector("[aria-label='원본 텍스트']")[0]
            # time to wait
            n = 10
            # equivalent of do while loop in python
            while (True):  # infinite loop
                print("in while loop")
                # clear the input field
                textField.clear()
                textField.send_keys(url)
                # enter the value
                driver.implicitly_wait(n)
                # get the text from input field after send_keys
                typed = textField.get_attribute("value")
                # check whether the send_keys value and text in input field are same, if same quit the loop
                if (typed == url):
                    print(n)
                    break
                # if not same, continue the loop with increased waiting time
                n = n + 5
###------------------------------------------------
            #SET WAIT TIME
            wait = WebDriverWait(driver, 10);
            #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-language-code='en']")))

            obj=driver.find_elements_by_xpath('//button[contains(concat(" ", normalize-space(@data-language-code)," "),"en")][1]')
            #obj[2].click()
            #wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(concat(" ", normalize-space(@data-language-code)," "),"en")][1]'))).click()

            obj = driver.find_elements_by_xpath('//button[contains(concat(" ", normalize-space(@data-language-code)," "),"ja")]//preceding-sibling::button')
            obj[0].click()
            #Header = driver.find_elements_by_xpath("//span[contains(concat(' ', normalize-space(@class), ' '), 'price-amount')]")

            selectLang = driver.find_elements_by_xpath('//div[contains(concat(" ", normalize-space(@data-language-code)," "),"en")]')
            selectLang[1].click()
            for a in selectLang:
                print(a)
            print("TEST SUCCESS")
            #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-language-for-alternatives='en']")))
            # translated_text=driver.find_elements_by_css_selector("[data-language-for-alternatives='en']")#/following-sibling::div
            translated_text = driver.find_elements_by_xpath('//span[@data-language-for-alternatives="en"]/span')
            #print(translated_text)
            for a in translated_text:
                textOnly = a.get_attribute('innerHTML')
                print(a.get_attribute('innerHTML'))
            #engTranslateBtn = driver.find_elements_by_css_selector("[data-language-code='en']")
            #wait=WebDriverWait(driver, 10);
            #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-language-code='en']"))).click()
            #engTranslateBtn[1].click();
            # engTranslateBtn.click()

            #다음 기능-한글 영어로 번역해보자. 구글로 번역해서 grammarly로 문법을 체크해 본다.

            self.text_box2.delete(1.0, tk.END)
            self.text_box2.insert(1.0, textOnly)
            driver.close()

        """--------파이선 자체 텍스트 에디터 사용--------""" 
        #1 MAKE CONTAINER
        self.myParent = parent
        self.main_container = Frame(parent)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.myParent.grid_rowconfigure(0, weight=1)
        self.myParent.grid_columnconfigure(0, weight=1)

        #2 MAKE FRAME
        self.top_frame = Frame(self.main_container)
        self.bottom_frame = Frame(self.main_container)
        self.top_left = Frame(self.top_frame)
        self.top_right = Frame(self.top_frame)

        #3 MAKE LABEL
        self.top_left_label = Label(self.top_left, text="번역할 글을 입력하세요  : ")
        self.top_right_label = Label(self.top_left, text="")

        #4 MAKE TEXT EDITOR
        self.text_box = Text(self.bottom_frame, height=25, width=100)
        self.text_box2 = Text(self.bottom_frame, height=25, width=100)

        #5 MAKE BUTTONS
        fr_buttons = Frame(self.main_container, bd=2)
        self.btn_open = Button(fr_buttons, text="열기", command=open_file)
        self.btn_save = Button(fr_buttons, text="저장하기", command=save_file)
        self.btn_translate = Button(fr_buttons, text="번역하기", command=translate_file)

        #6 SET POSITION
        self.btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.btn_translate.grid(row=0, column=2, sticky="ew", padx=5)

        fr_buttons.grid(row=0, column=0, sticky="ns")

        self.top_frame.grid(row=0, column=0, sticky="ew")
        self.bottom_frame.grid(row=1, column=0, sticky="nsew")
        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.top_left.grid(row=0, column=0, sticky="w")
        self.top_right.grid(row=0, column=2, sticky="e")
        self.top_frame.grid_columnconfigure(1, weight=1)

        self.top_left_label.grid(row=0, column=0, sticky="w")
        self.top_right_label.grid(row=0, column=0, sticky="e")

        self.text_box.grid(row=0, column=0, sticky="nsew")
        self.text_box2.grid(row=1, column=0, sticky="nsew")
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)




root = tk.Tk()
root.title("TEXT EDITOR")

#root.rowconfigure(0, minsize=800, weight=1)
#root.columnconfigure(1, minsize=800, weight=1)
myapp = MyApp(root)
root.mainloop()

"""
참고한 리소스
https://stackoverflow.com/questions/14946963/tkinter-grid-how-to-position-widgets-so-they-are-not-stuck-together
https://www.qafox.com/selenium-locators-using-first-child-in-css-selectors/
https://www.seleniumeasy.com/selenium-tutorials/examples-for-xpath-and-css-selectors
"""
