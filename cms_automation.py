import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def login(enrollment, password, campus):
    options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    driver.get("https://cms.bahria.edu.pk/Logins/Student/Login.aspx")

    enrollment_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_tbEnrollment"]'))
    )
    enrollment_field.send_keys(enrollment)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_tbPassword"]'))
    )
    password_field.send_keys(password)

    campus_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_ddlInstituteID"]'))
    )
    campus_dropdown = Select(campus_dropdown)
    campus_dropdown.select_by_visible_text(campus)

    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_btnLogin"]'))
    )
    login_button.click()

    return driver


def submit_survey(driver, question_count, radio_button_ranges):
    for _ in range(question_count):
        survey_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_gvSurveyConducts"]/tbody/tr[1]/td[8]/a'))
        )
        survey_link.click()

        for question_number, radio_button_range in enumerate(radio_button_ranges):
            for i in radio_button_range:
                radio_button_xpath = f'//*[@id="BodyPH_surveyUserControl_repeaterQuestionGroups_repeaterQuestions_{question_number}_rbl_{i}_0_{i}"]'
                radio_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, radio_button_xpath))
                )
                radio_button.click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="BodyPH_surveyUserControl_btnSubmit"]'))
        )
        submit_button.click()

        time.sleep(5)


def studentForm(enrollment, password, campus):
    driver = login(enrollment, password, campus)

    radio_button_ranges = [
        range(3),   # Question 0, 1, 4, 5, 7
        range(4),   # Question 2, 3, 6
        range(2)    # Question 8
    ]

    submit_survey(driver, 7, radio_button_ranges)

    driver.quit()


def teacherForm(enrollment, password, campus):
    driver = login(enrollment, password, campus)

    radio_button_ranges = [
        range(13),  # Question 0
        range(5)    # Question 1
    ]

    submit_survey(driver, 7, radio_button_ranges)

    driver.quit()


enrollment = input("Enter your enrollment number: ie(02-000000-000) ")
password = input("Enter your password: ")
campus = input("Enter your campus ie Karachi Campus, Islamabad Campus, IPP(Karachi): ")

studentForm(enrollment, password, campus)
