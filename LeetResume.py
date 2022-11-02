# Note to anyone using this, change the lines of os.mkdir/chdir to wherever you'd like for your LeetResume to be saved.
# You will also need to have Selenium installed as well as FireFox. 
# Please note that this is still a work in progress, but I've done my best to error proof LeetResume
# The code should catch most errors, and restart from where it fails... most times. 
# However if for some reason it doesn't catch the error, you can restart the code from where it left off at by inserting values into the argument at line 240
# 'rlist.append(leetResMain())' can take arguments that will be equal to co-ordinates, if you put rlist.append(leetResMain(5,2)) it will resume on problem 4 of the third solved page,
# very rarely code will get stuck on a page, not sure why webdriver.wait doesnt catch this, but simply refresh the webpage
# after reloading page script resumes where it leaves off
# note that as of right now you should not resume on the very last page, as this could cause an error.  
# this is a free resource and I will be updating it regularly.
# currently it takes ~10 seconds from start to finish to download one problem.

# Update 3/27/22, leet resume is much faster after first itteration.
# example: say that a user runs this and downloads ~1k problems, and then at a later date has completed another 20 problems.
# LeetResume will now print to screen that 'prob x is already saved locally, continuing to next problem' rather than over writing and redoing the earlier 1k problems, only downloading the new 20


# planned updates: sort problems by difficulty level when saving to local file (COMPLETED),
# cut down on time (COMPLETED),
# save file type as code it was originally written in instead of .txt (COMPLETED,
# save fastest code rather than first accepted code (DROPPING FROM UPDATES, might add back at a a later time),
# skip over code that's already saved locally to computer which will drastically cut down on time when this is ran again (COMPLETED),
# find out why very rarely code will hang and requires a manual refresh in the browser rather than being caught by my wait conditions, and fix that issue.
# change time.sleep to webdriver wait conditions in earlier portions of code
# take username and password as arguments
# maybe, change file save location to be at C:\Program Files (x86) that way users could simply run program and not be bothered where program is being saved.
# build a GUI? would look better as a project to potential employers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import os
import time
import getpass
import math
#TESTING: remember to set REPEATI to 1 and REPEATJ to 0 when not testing for bugs
REPEATI, REPEATJ = 1, 0
# REFERS TO LINE ABOVE:
# repeati needs to start at 1 as the following line: 'div.odd\:bg-layer-1:nth-child(' + str(i) + ') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)'
# will never need 0 and our if check to repeat the program checks for the existence of repeati
# if for some reason code fails at solved leetcode problem 1 (which has happened, once) the code will restart and resume at problem 1.



# attempt to change viewport size
# reading through forums it seems bot detection uses window size to detect scripts, so changing the viewport size 'might' help.


def viewport_size(browser, width, height):
    window_size = browser.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    browser.set_window_size(*window_size)


# note: the below function numStripper is an attempt to make my code faster by ignoring problems I've already completed and downloaded locally
# I plan to use numStripper on all files already downloaded to my computer, put them within a dictionary
# for o(1) look up time, and then check to see if this problem is already within the dictionary before downloading it.
# I was going to simply check to see if the problem title such as '877. Stone Game' was already downloaded to computer.
# however as of last update, problems are now saved as whatever code they were written, so '877. Stone Game' would be saved with a .py extension
# if a user had written in C++ it would be with a .cpp making it much harder to strip '877. Stone Game.py' with a simple slice.
# I could use regex, but I'd still need to create a map anyways, unless I want to have a lookup time of o(n^n) as I'd have to lookup if it was already saved locally as os.listdir()
# returns a list, and with leetcode having over 2000 problems, that could be an issue. it'll be much more efficent to simply during step 0 create a dictionary of already completed problems.


# expects a string of a number followed by a period and some letters
# the above represents how leetcode titles its problems, example: 877. Stone Game.py
# returns a string of simply the numbers, example: 877
def numStripper(probStr):
    rStr = ''
    for char in probStr:
        if char.isdecimal():
            rStr += char
        else:
            return rStr


# Note to self, I started to make this script much faster by removing the time.sleep() conditions and replacing them
# with the "correct" coding practices to make this run much faster, "EC.invisibility_of_element" and "EC.element_to_be_clickable"
# However, this was too fast and leetcode started to throw recaptchas at me as leetcode realized I was scripting.
# I've since removed the opitmal code and readded the sleep(3) wait condition
# this makes the code run much slower than I'd like it to, but it works and doesn't raise any captchas.

def UandP():
    print('LeetResume')
    print('Please enter username for Leetcode:')
    username = input()
    print('Please enter password for Leetcode:')
    password = getpass.getpass()
    #print('Would you like to save this username and password locally to your computer?')
    return [username, password]




# Currently trying to fix the above comment by making this script fail and then resume where it left off when it is 'caught' by leetcode using wait conditions
def leetResMain(userName, passWord, contI=0, contJ=0):
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


    # save current working directory, will be needed later when writing data    
    workingDir = os.getcwd()


    # build files for problems to be saved to
    try:
        os.mkdir(workingDir + '\\Easy')
        os.mkdir(workingDir + '\\Medium')
        os.mkdir(workingDir + '\\Hard')
    except:
        os.chdir(workingDir)

    # save current working directory, will be needed later when writing data    
    workingDir = os.getcwd()

    # will only populate if user has already run leetcode before and is getting their newly completed problems.
    # goes to each problem file, and creates a list of all problems already saved
    completedProbsList, completedProbsMap = [], {}
    completedProbsFiles = [workingDir + '\\Easy', workingDir + '\\Medium', workingDir + '\\Hard']
    for completedProbs in completedProbsFiles:
        os.chdir(completedProbs)
        completedProbsList += os.listdir()

    # Turn that prob list into a probsMap so that there is an 0(1) look up time.
    for completedProbs in completedProbsList:
        completedProbsMap[numStripper(completedProbs)] = 1

    
    
    
    # build the dictionary where file types will be converted.
    fileMap = {}
    fileMap['c++'] = '.cpp'
    fileMap['java'] = '.java'
    fileMap['python'] = '.py'
    fileMap['python3'] = '.py'
    fileMap['c'] = '.c'
    fileMap['c#'] = '.cs'
    fileMap['javascript'] = '.js'
    fileMap['ruby'] = '.rb'
    fileMap['swift'] = '.swift'
    fileMap['go'] = '.go'
    fileMap['scala'] = '.scala'
    fileMap['kotlin'] = '.kt'
    fileMap['rust'] = '.rs'
    fileMap['php'] = '.php'
    fileMap['typescript'] = '.ts'
    fileMap['racket'] = '.rkt'
    fileMap['erlang'] = '.erl'
    fileMap['elixir'] = '.ex'
    fileMap['oracle'] = '.sql'
    fileMap['mysql'] = '.sql'
    fileMap['ms sql server'] = '.sql'
    fileMap['bash'] = '.sh'

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
    try:
        loginElem = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#id_login')))
        # username below
        loginElem.send_keys(userName)

        loginElemPass = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#id_password')))
        # password below
        loginElemPass.send_keys(passWord)


        # click login page, do it 'live' since .sumbit() wouldn't work
        submitElem = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.btn-content-container__2HVS')))
        submitElem.click()
        time.sleep(5)


        # navigating to problems page
        pageElem = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.navbar-left-container__3-qz > div:nth-child(3) > a:nth-child(1)')))
        pageElem.click()
        time.sleep(3)

        # get the # of completed problems, I can divide this by 50 and
        # use this as my variable to know when to end my program

        #I shouldnt need a webDriverWait portion here, because the page is not changed from the earlier webdriver wait
        solved = int(browser.find_element(By.CSS_SELECTOR, '.pb-0\.5').text)

    except:
        print("Login was unsuccessful, please restart program and try again")
        browser.quit()
        return[-1]

    # we're rounding up as lets say we have 51 problems solved, well 50 solved problems per page, 
    # we're going to need to go to the next page to get the last problem and we're going to want the modulo to get our last i
    solvedModulo = solved % 50
    solved = math.ceil(solved/50)

    # select the "solved" status drop down
    # As of 10/3/22 headless menu button seems to change depending on leetcode webpage,
    # I've seen it be 15, 18, 43, and 39
    # Updated so script now selects the divs css_selector instead.
    # had to also update statusMenuElem
    
    statusmenuElem = browser.find_element(
        By.CSS_SELECTOR, '.space-x-2\.5 > div:nth-child(3) > div:nth-child(1)')
    #By.CSS_SELECTOR, '.space-x-2\.5 > div:nth-child(3) > div:nth-child(1)')))
    #headlessui-menu-button-43
    #headlessui-menu-button-43
    #headlessui-menu-button-39
    #headlessui-menu-button-43
    #headlessui-menu-button-43
    
    statusmenuElem.click()
    time.sleep(3)

    # click on said status
    statusElem = browser.find_element(
        By.CSS_SELECTOR, '#headlessui-menu-item-39 > div:nth-child(1) > div:nth-child(1)')
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

                # get difficulty of problem
                probDiff = browser.find_element(By.CSS_SELECTOR, 'div.odd\:bg-layer-1:nth-child('+ str(i) +') > div:nth-child(5) > span:nth-child(1)').text
                

                

                # check to see if it is already in our files, if it is, simply print that we're skipping this problem
                # else print the name of problem to terminal to let user know what problem they are currently on
                if numStripper(probElem.text) in completedProbsMap:
                    REPEATI += 1
                    i += 1
                    print(probElem.text + ' is already saved locally, continuing to next problem')
                    continue

                else:
                    print(probElem.text)


                
                probname = probElem.text
                probElem.click()
                # time.sleep(3)

                # When at problem page, click submissions to get to list of past submissions
                # the next line confuses me, occasionally it needs to be part of my code or an exception will be thrown, and occasionally it needs to not be there, or an error exception will be thrown.
                # this has been an intermitten problem for quite awhile now, will update if it happens again
                # UPDATE: on 3/18/22 it needed to be there and on 3/19/22 it needs to not be there. I'm getting an error "no such element exception" on 3/19
                # putting a try except block on 3/19 to see if that fixes my issue. 3/27 update: there's been no issue since putting try except block, seems this has resolved my error.
                # looks like it will throw an error, but because its caught, it will simply close geckodriver and restart program, i'm fine with that resolution.
                try:
                    WebDriverWait(browser, 10).until(EC.invisibility_of_element(
                        browser.find_element(By.ID, "initial-loading")))
                except NoSuchElementException as exc:
                    print("hitting an error that has been accounted for: " + exc + " Program may restart, but will resume where it left off")
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
                languageType = WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '#result_language'))).text
                languageType.lower()

                # Go to working directory + difficulty level and save information there. then return to working directory
                os.chdir('C:\\Users\\cvela\\MyPythonScripts\\LeetRes' + '\\' + probDiff)

                # check to see if language is in the fileMap, if it is, append it so that it saves
                # as the correct file type.
                # if it is not in the fileMap for some reason, it will still save as a .txt file
                if languageType in fileMap:
                    solutionfile = open(probname + fileMap[languageType], "w")

                else:
                    solutionfile = open(probname + ".txt", "w")
                
                solutionfile.write(solution.text)
                solutionfile.close()

                os.chdir(workingDir)
                
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
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.flex:nth-child(7)'))).click()
                

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

    # IF code has timed out for some reason, will restart and resume where it last was, on its own. 
    except TimeoutException:
        print("code failed")
        browser.quit()
        print(REPEATI, REPEATJ)
        return [REPEATI, REPEATJ]

    #code was completed correctly, will quit browser, return 0 and the for loop later on will be skipped, and print the exit message
    browser.quit()
    return[0]


rlist = []

#call uandp to get username and password:
uapList = UandP()

# when not testing for bugs, remove arguments from leetResMain()
rlist.append(leetResMain(uapList[0], uapList[1]))
# if rlist[-1][0] == 0 then leetResMain was succesful and skip next block of code
# otherwise it will restart at the 'co-ordinates' of repeati and repeatj
while(rlist[-1][0] > 0):
    print("code failed midway through, resuming at problem " +
          str(rlist[-1][0]) + " on page " + str(rlist[-1][1]))
    print(rlist)
    rlist.append(leetResMain(uapList[0], uapList[1], rlist[-1][0], rlist[-1][1]))
if rlist[-1][0] == 0:
    print("code was successful, closing")
elif rlist[-1][0] == -1:
    print('Please double check spelling, capslock, and special characters.')
