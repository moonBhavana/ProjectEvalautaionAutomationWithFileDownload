

#import selenium for automation
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import sys
import time
from time import sleep
from selenium.webdriver.chrome.options import Options



evaluation_num=int(input("Enter the number of projects you wish to evlauate:"))

for i in range(evaluation_num):
       
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(ChromeDriverManager().install()),chrome_options=options)
       

        #engagexurl
        formurl = 'https://engagex.simplilearn.com/#/projects/assigned-projects/pending-evaluation'
        params = {'behavior': 'allow', 'downloadPath': r'C:\Users\Bhavana\Desktop\Downloaded_test_project'}
        driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
        driver.get(formurl) 



        def insertValues(xPath=None, sendKeyData=None):
                            data = driver.find_element_by_xpath(xPath)
                            data.click()
                            data.send_keys(sendKeyData)

        def insertValuesAfterwait(xPath=None, sendKeyData=None):
                            dataWait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,xPath)))
                            dataWait.click()
                            dataWait.send_keys(sendKeyData)

        
        
           

        engagex_mail="email"
        engagex_password="pwd"


        insertValues(xPath='/html/body/app-root/app-login/div/div/form/div[1]/input',sendKeyData=engagex_mail)

        insertValues(xPath='/html/body/app-root/app-login/div/div/form/div[2]/input',sendKeyData=engagex_password)


        

        # #login to engageX
        login_button=driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/form/button')
        login_button.click()
        print("Logged in to enagagex")

        # #Clicking on the projects tab
        projects_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Projects")))
        projects_tab.click()
        print("Clicked on projects Tab")

        # #Clicking on the My projects Tab
        my_projects_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Projects")))
        my_projects_tab.click()
        print("Clicked on my projects Tab")


        # #clicking on evaluate button
        evaluate = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Evaluate")))
        evaluate.click()
        print("Evaluating "+str(i+1)+" project")

        print("Starting to download project file");

        # file_dowbload_click=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="evaluate"]/div/div/div[2]/div/div[2]/div/div/div[2]/div/a'))).click()
        file_dowbload_click=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "File 1")))
        file_dowbload_click.click()

        print("File downloading started")
        print("open the downloads folder to evaluate the project and tell me is the project pass or fail")

        project_result=str(input("enter p for Pass or f for Fail: "))
        if(project_result=='p'):
                
            #clicking on the radio button of pass
            pass_project=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="evaluate"]/div/div/div[2]/div/div[3]/form/div[2]/ul/li[1]/input')))
            pass_project.click()

            #passing the comment
            insertValuesAfterwait(xPath='//*[@id="evaluate"]/div/div/div[2]/div/div[3]/form/div[3]/textarea',sendKeyData="Congratulations !!! Your project is evaluated and approved. Your project is nicely done and you have completed the necessary tasks for this project. Keep it up !! You have done a great job in this project and have put great efforts.")
    
       
            # #Clicking on the evaluate button for final submission
            evaluate_project = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-dashboard-layout/div/div[2]/app-projects-view/app-projects-type-view/app-projects/app-project-detail/div/div/div/div[2]/div/div[3]/form/div[4]/div/button')))
            evaluate_project.click()
            time.sleep(10)
            driver.close()
            print("Passed "+str(i+1)+" projects")

        elif(project_result=='f'):

            # failing a project 
            fail_project=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="evaluate"]/div/div/div[2]/div/div[3]/form/div[2]/ul/li[2]/input')))
            fail_project.click();

            # Failing a project comment
            insertValuesAfterwait(xPath='//*[@id="evaluate"]/div/div/div[2]/div/div[3]/form/div[3]/textarea',sendKeyData="Thank you for the submission. We regret to ifnorm you that the proejct is not accepted please share the complete project work space in a zip file along with the output screenshots.")

            # #Clicking on the evaluate button for final submission
            evaluate_project = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-dashboard-layout/div/div[2]/app-projects-view/app-projects-type-view/app-projects/app-project-detail/div/div/div/div[2]/div/div[3]/form/div[4]/div/button')))
            evaluate_project.click()
            
            print("Failed "+str(i+1)+" projects")
            
    except NoSuchElementException:
               
                print("Nothing found ")
                






    