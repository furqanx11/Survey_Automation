import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def prompt_user():
    enrollment = input("Enter your enrollment number: ")
    password = input("Enter your password: ")
    return enrollment, password


def courseForm(enrollment, password):
    options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    driver.get("https://cms.bahria.edu.pk/Logins/Student/Login.aspx")

    enrollment_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_tbEnrollment"]')))
    enrollment_field.send_keys(enrollment)

    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_tbPassword"]')))
    password_field.send_keys(password)

    campus_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_ddlInstituteID"]')))
    campus_dropdown.click()

    karachi_campus_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Karachi Campus")]')))
    karachi_campus_option.click()

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_btnLogin"]')))
    login_button.click()

    for _ in range(7):
        survey_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_gvSurveyConducts"]/tbody/tr[1]/td[8]/a')))
        survey_link.click()

        for question_number in range(9):
            if question_number in (0, 1, 4, 5, 7):
                radio_button_range = range(3)
            elif question_number in (2, 3, 6):
                radio_button_range = range(4)
            elif question_number == 8:
                radio_button_range = range(2)

            for i in radio_button_range:
                radio_button_xpath = f'//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_{question_number}_rbl_{i}_0_{i}"]'
                radio_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, radio_button_xpath)))
                radio_button.click()

        radio_button_xpath_list = [
            '//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_11_rbl_0_1_0"]',
            '//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_11_rbl_1_1_1"]',
            '//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_11_rbl_3_0_3"]',
            '//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_11_rbl_4_0_4"]',
            '//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_11_rbl_5_1_5"]'
        ]

        for radio_button_xpath in radio_button_xpath_list:
            radio_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, radio_button_xpath)))
            radio_button.click()

        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_surveyUserControl_btnSubmit"]')))
        submit_button.click()

        time.sleep(5)

    driver.quit()


def teacherForm(enrollment, password):
    options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    driver.get("https://cms.bahria.edu.pk/Logins/Student/Login.aspx")

    enrollment_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_tbEnrollment"]')))
    enrollment_field.send_keys(enrollment)

    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_tbPassword"]')))
    password_field.send_keys(password)

    campus_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_ddlInstituteID"]')))
    campus_dropdown.click()

    karachi_campus_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Karachi Campus")]')))
    karachi_campus_option.click()

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_btnLogin"]')))
    login_button.click()

    for _ in range(7):
        survey_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_gvSurveyConducts"]/tbody/tr[1]/td[8]/a')))
        survey_link.click()

        for question_number in range(2):
            if question_number == 0:
                radio_button_range = range(13)
            elif question_number == 1:
                radio_button_range = range(5)

            for i in radio_button_range:
                radio_button_xpath = f'//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_{question_number}_rbl_{i}_0_{i}"]'
                radio_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, radio_button_xpath)))
                radio_button.click()

        submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_surveyUserControl_btnSubmit"]')))
        submit_button.click()

        time.sleep(5)

    driver.quit()


enrollment, password = prompt_user()
courseForm(enrollment, password)
teacherForm(enrollment, password)
