from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time

# Note to self, I started to make this script much faster by removing the time.sleep() conditions and replacing them
# with the "correct" coding practices to make this run much faster, "EC.invisibility_of_element" and "EC.element_to_be_clickable"
# However, this was too fast and leetcode started to throw recaptchas at me as leetcode realized I was scripting.
# I've since removed the opitmal code and readded the sleep(3) wait condition
# this makes the code run much slower than I'd like it to, but it works and doesn't raise any cap.



#                           Step 0: Prep Work

# make a directory to save information and go to that directory
# if directory exists, just change to that directory
# load up login page
try:
    os.mkdir('C:\\Users\\cvela\\MyPythonScripts\\LeetRes')
    os.chdir('C:\\Users\\cvela\\MyPythonScripts\\LeetRes')
except:
    os.chdir('C:\\Users\\cvela\\MyPythonScripts\\LeetRes')
    
# Load login page
browser = webdriver.Firefox()
browser.get('https://leetcode.com/accounts/login/')
#tried to comment out the next sleep command, intermittenly fails without it.
time.sleep(3)

#                           STEP 1 Log In and navigate to problems page

# Put user name and password in below
# I tried to use loginElem.submit(), but that failed?
# "I'll do it live" 

loginElem = browser.find_element(By.CSS_SELECTOR, '#id_login')
# username below
loginElem.send_keys('FakeEmail')

loginElemPass = browser.find_element(By.CSS_SELECTOR, '#id_password')
# password below
loginElemPass.send_keys('FakePassword')

#click login page 'live' since .sumbit() wouldn't work
submitElem = browser.find_element(By.CSS_SELECTOR, '.btn-content-container__2HVS')
submitElem.click()
time.sleep(3)

# navigating to problems page
pageElem = browser.find_element(By.CSS_SELECTOR, '.navbar-left-container__3-qz > div:nth-child(3) > a:nth-child(1)')
pageElem.click()
time.sleep(3)

#select the "solved" status drop down
statusmenuElem = browser.find_element(By.CSS_SELECTOR, '#headlessui-menu-button-15')
statusmenuElem.click()
time.sleep(1)

#click on said status
statusElem = browser.find_element(By.CSS_SELECTOR, '#headlessui-menu-item-29 > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
statusElem.click()
time.sleep(1)





#                           STEP 2 Get information recursively
# change bg-overlay-3:nth-child(HERE)
# 

# Leetcode forces daily challenge to always be on, I'll have to account for that on the first pass
# First page is 51 in length, all other pages are 50 problems
loop = 52
# change at a later date, might just write while(True):
# then let code do its thing with a try except block, on fail browser.quit  
for j in range(5):
    #look for above comment on why loop is a variable
    for i in range(1, loop):
        # go to problem #X and load problem webpage
        if loop == 52 and i == 1:
            continue
        probElem =  browser.find_element(By.CSS_SELECTOR, 'div.odd\:bg-overlay-3:nth-child('+ str(i) +') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
        print(probElem.text)
        probname = probElem.text
        probElem.click()
        time.sleep(3)


        # When at problem page, click submissions to get to list of past submissions
        #WebDriverWait(browser, 10).until(EC.invisibility_of_element(browser.find_element(By.ID, "initial-loading")))
        #WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.css-1lelwtv-TabHeader:nth-child(4) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(2)'))).click()
        browser.find_element(By.CSS_SELECTOR, 'div.css-1lelwtv-TabHeader:nth-child(4) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(2)').click()
        time.sleep(3)

        
        # get all content with 'a' elements
        # then keep only the elements that has their text ==  "Accepted"
        # clicks on first accepted code
        # in future I'll want to see if I can get the best fastest code
        aElems = browser.find_elements(By.CSS_SELECTOR, 'a')
        time.sleep(3)
        acceptedElems = []
        for element in aElems:
            if element.text == "Accepted":
                acceptedElems.append(element)        
        acceptedElems[0].click()
        time.sleep(3)

        
        # leetcode force a new window to open when clicking on accepted solutions,
        # switch to that window, grab information, write to file, close file, close window, switch back
        # saving in .txt format as user could be using any code type and even then leetcode
        # has varrying amount of mixed in other laanguages, such as SQL, bash.
        browser.switch_to.window(browser.window_handles[1])
        solution = browser.find_element(By.CSS_SELECTOR, '.ace_scroller')
        solutionfile = open(probname + ".txt", "w")
        solutionfile.write(solution.text)
        solutionfile.close()
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(3)
        
        # return to solved problems page.
        browser.back()
        browser.back()
        time.sleep(3)
    # after first pass, we decrement by 1 to no longer account for daily challenge
    if loop == 52:
        loop -=1
        
    # navigate to next set of 50 problems
    browser.find_element(By.CSS_SELECTOR, 'button.flex:nth-child(6)').click()
    time.sleep(3)

