# Note to anyone using this, change the lines of os.mkdir/chdir to wherever you'd like for your LeetResume to be saved.
# You will also need to change loginElem and loginElemPass to whatever your login email and password is. 
# You will also need to have Selenium installed. 
# Please note that this is still a work in progress, but I've done my best to error proof LeetResume
# The code should catch most errors, and restart from where it fails... most times. 
# However if for some reason it doesn't catch the error, you can restart the code from where it left off at by inserting values into the argument at line 240
# 'rlist.append(leetResMain())' can take arguments that will be equal to co-ordinates, if you put rlist.append(leetResMain(5,2)) it will resume on problem 4 of the third solved page,
# very rarely code will get stuck on a page, not sure why webdriver.wait doesnt catch this, but simply refresh the page
# after reloading page script resumes where it leaves off
# note that as of right now you should not resume on the very last page, as this could cause an error.  
# this is a free resource and I will be updating it regularly.
# currently it takes ~10 seconds from start to finish to download one problem, and then move to the next.


# planned updates: sort problems by difficulty level when saving to local file, cut down on time, save file type as code it was originally written in instead of .txt,
# save fastest code rather than first accepted code, skip over code that's already saved locally to computer.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import os
import time
import math
#TESTING: remember to set REPEATI to 1 and REPEATJ to 0 when not testing for bugs
REPEATI, REPEATJ = 1, 0
# REFERS TO LINE ABOVE:
# repeati needs to start at 1 as 'div.odd\:bg-layer-1:nth-child(' + str(i) + ') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)'
# will never need 0 and our if check to repeat the program checks for the existence of repeati


# attempt to change viewport size
# reading through forums it seems bot detection uses window size to detect scripts


def viewport_size(browser, width, height):
    window_size = browser.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    browser.set_window_size(*window_size)


# Note to self, I started to make this script much faster by removing the time.sleep() conditions and replacing them
# with the "correct" coding practices to make this run much faster, "EC.invisibility_of_element" and "EC.element_to_be_clickable"
# However, this was too fast and leetcode started to throw recaptchas at me as leetcode realized I was scripting.
# I've since removed the opitmal code and readded the sleep(3) wait condition
# this makes the code run much slower than I'd like it to, but it works and doesn't raise any captchas.

# Currently trying to fix the above comment by making this script fail and then resume where it left off when it is 'caught' by leetcode using wait conditions
def leetResMain(contI=0, contJ=0):
    global REPEATI, REPEATJ
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

    # this next portion of code was an attempt to not be caught by LC, according to some stack overflow threads changing the browser size 
    # helps to remain undetected by recaptchas. I've yet to see a difference, might remove code later.
    viewport_size(browser, 800, 600)

    browser.get('https://leetcode.com/accounts/login/')
    # tried to comment out the next sleep command, intermittenly fails without it.
    time.sleep(3)

    #                           STEP 1 Log In and navigate to problems page

    # Put user name and password in below
    # I tried to use loginElem.submit(), but that failed?
    # "I'll do it live"

    loginElem = browser.find_element(By.CSS_SELECTOR, '#id_login')
    # username below
    loginElem.send_keys('fakeusername')

    loginElemPass = browser.find_element(By.CSS_SELECTOR, '#id_password')
    # password below
    loginElemPass.send_keys('fakepassword')

    # click login page, do it 'live' since .sumbit() wouldn't work
    submitElem = browser.find_element(
        By.CSS_SELECTOR, '.btn-content-container__2HVS')
    submitElem.click()
    time.sleep(5)

    # navigating to problems page
    pageElem = browser.find_element(
        By.CSS_SELECTOR, '.navbar-left-container__3-qz > div:nth-child(3) > a:nth-child(1)')
    pageElem.click()
    time.sleep(3)

    # get the # of completed problems, I can divide this by 50 and
    # use this as my variable to know when to end my program
    solved = int(browser.find_element(By.CSS_SELECTOR, '.pb-0\.5').text)

    # we're rounding up as lets say we have 51 problems solved, well 50 solved problems per page, 
    # we're going to need to go to the next page to get the last problem and we're going to want the modulo to get our last i
    solvedModulo = solved % 50
    solved = math.ceil(solved/50)

    # select the "solved" status drop down
    statusmenuElem = browser.find_element(
        By.CSS_SELECTOR, '#headlessui-menu-button-15')
    statusmenuElem.click()
    time.sleep(3)

    # click on said status
    statusElem = browser.find_element(
        By.CSS_SELECTOR, '#headlessui-menu-item-29 > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    statusElem.click()
    time.sleep(3)

    #                           STEP 2 Get information recursively
    # update: as of last leetcode update the webelement that needs to be incremented has been changed. new code reflects this.
    # change div.odd\:bg-layer-1:nth-child(HERE)
    #
    try:
        # Leetcode forces daily challenge to always be on, I'll have to account for that on the first pass
        # First page is 51 in length, all other pages are 50 problems
        loop = 52
        # J in the next loop is there so that I can see 
        # set j = to 1? currently code is failing when j is 3, and solved is 4 causing it to go through loops again. 
        j = 0
        while( j <  solved):
            # look for above comment on why loop is a variable

            # if script was already running go back to where it last left off.
            while contJ:
                # navigate to set of 50 problems from last run
                browser.find_element(
                    By.CSS_SELECTOR, 'button.flex:nth-child(6)').click()
                j += 1
                contJ -= 1
                time.sleep(3)
                # set loop to 51 because if the presence of contJ exists we are not on the first page This will throw an error if we are on the last page. 
                # I'll think of a way around that later. 
                loop = 51
            time.sleep(3)


            i = 1
            # if broken script, go back to last known completed problem
            if contI:
                i = contI
                contI = 0
            # loop will be decremented after first pass
            while( i < loop):
                # if condition here skips daily challenge and continues on to the first problem actually solved.
                if loop == 52 and i == 1:
                    i += 1
                    continue


                # go to problem #X and load problem webpage
                probElem = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.odd\:bg-layer-1:nth-child(' + str(
                    i) + ') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')))

                print(probElem.text)
                probname = probElem.text
                probElem.click()
                # time.sleep(3)

                # When at problem page, click submissions to get to list of past submissions
                # the next line confuses me, occasionally it needs to be part of my code or an exception will be thrown, and occasionally it needs to not be there, or an error exception will be thrown.
                # this has been an intermitten problem for quite awhile now, will update if it happens again
                # UPDATE: on 3/18/22 it needed to be there and on 3/19/22 it needs to not be there. I'm getting an error "no such element exception" on 3/19
                # putting a try except block on 3/19 to see if that fixes my issue.
                try:
                    WebDriverWait(browser, 10).until(EC.invisibility_of_element(
                        browser.find_element(By.ID, "initial-loading")))
                except NoSuchElementException as exc:
                    print("hitting an error that has been accounted for")
                    print(exc)
                    continue
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'div.css-1lelwtv-TabHeader:nth-child(4) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(2)'))).click()
                # browser.find_element(By.CSS_SELECTOR, 'div.css-1lelwtv-TabHeader:nth-child(4) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(2)').click()
                # time.sleep(3)

                # get all content with 'a' elements
                # then keep only the elements that has their text ==  "Accepted"
                # clicks on first accepted code
                # in future I'll want to see if I can get the best fastest code
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#app > div > div.main__2_tD > div.content__3fR6 > div > div.side-tools-wrapper__1TS9 > div > div.css-1gd46d6-Container.e5i1odf0 > div.css-jtoecv > div > div.tab-pane__ncJk.css-1eusa4c-TabContent.e5i1odf5 > div > div > div > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.status-column__3SUg > a')))
                aElems = browser.find_elements(By.CSS_SELECTOR, 'a')
                # time.sleep(3)
                acceptedElems = []
                for element in aElems:
                    if element.text == "Accepted":
                        acceptedElems.append(element)
                acceptedElems[0].click()
                # time.sleep(3)

                # leetcode forces a new window to open when clicking on accepted solutions,
                # switch to that window, grab information, write to file, close file, close window, switch back
                # saving in .txt format as user could be using any code type and even then leetcode
                # has varrying amount of mixed in other languages, such as SQL, bash.
                browser.switch_to.window(browser.window_handles[1])
                solution = WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '.ace_scroller')))
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
                REPEATI += 1
                WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.odd\:bg-layer-1:nth-child(' + str(
                    i) + ') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')))
                i += 1

            # after first pass, we decrement loop by 1 to no longer account for daily challenge
            if loop == 52:
                loop -= 1

            # navigate to next set of 50 problems
            if j != solved -1:
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.flex:nth-child(6)'))).click()

            time.sleep(3)
            REPEATJ += 1
            REPEATI = 1
            j += 1

            # on final iteration we don't want to go over all '50' solved links as this will result in a timeout error.
            # that time out error will screw up the program as im using timeout errors to fix whenever leetcode captchas catch me
            # example of above bug: if we have 51 solved problems, we will go to page two and attempt to go to problem 2 of second page
            # that will throw an error, as clearly there should only be 1 problem on the second page
            if solved - j == 1:
                loop = solvedModulo + 1
    except TimeoutException:
        print("code failed")
        browser.quit()
        print(REPEATI, REPEATJ)
        return [REPEATI, REPEATJ]
    browser.quit()
    return[0]


rlist = []

#when not testing for bugs, remove arguments from leetResMain()
rlist.append(leetResMain())
# if rlist[-1][0] == 0 then leetResMain was succesful and skip next block of code
# otherwise it will restart at the 'co-ordinates' of repeati and repeatj
while(rlist[-1][0]):
    print("code failed midway through, resuming at problem " +
          str(rlist[-1][0]) + " on page " + str(rlist[-1][1]))
    print(rlist)
    rlist.append(leetResMain(rlist[-1][0], rlist[-1][1]))

print("code was successful, closing")
