# LeetResume-2022
The purpose of this project is for there to be a clear and easy way to download solved leetcode questions. 

I started this project when I realized I hadn't uploaded to github in awhile and I wanted to show prospective employers that I had been coding over the last year.

I went to leetcode to download my previous submissions, 
however I soon realized that there was not a way to download my solved questions and that it would be rather monotonous to go through, 
question by question, copy and paste the code of each solved problem into a text editor, and then save it.

So instead I created LeetResume, a quick and efficent way to download my solved problems. 

the following are instructions I've added at the front of my code so that others can use my program as I build it:


 Note to anyone using this, change the lines of os.mkdir/chdir to wherever you'd like for your LeetResume to be saved.
 You will also need to change loginElem and loginElemPass to whatever your login email and password is. 
 You will also need to have Selenium installed. 
 
 if the above conditions have been satisied, you can simply run the program by hitting F5 in idle and letting the program run.
 
 
 Please note that this is still a work in progress, but I've done my best to error proof LeetResume.
 The code should catch most errors, and restart from where it fails... most times. 
 However if for some reason it doesn't catch the error, you can restart the code from where it left off at by inserting values into the argument at line 240
 'rlist.append(leetResMain())' can take arguments that will be equal to co-ordinates, if you put rlist.append(leetResMain(5,2)) it will resume on problem 4 of the third solved page,
 note that as of right now you should not resume on the very last page, as this could cause an error.  
 this is a free resource and I will be updating it regularly.
 currently it takes ~10 seconds from start to finish to download one problem, and then move to the next.
 very rarely code will get stuck on a page, not sure why webdriver.wait doesnt catch this, but simply refresh the webpage.
 After reloading webpage script resumes where it leaves off.

 planned updates: sort problems by difficulty level when saving to local file (COMPLETED),
 cut down on time (COMPLETED),
 save file type as code it was originally written in instead of .txt (COMPLETED,
 save fastest code rather than first accepted code (DROPPING FROM PLANNED UPDATES, might add back at a a later time),
 skip over code that's already saved locally to computer which will drastically cut down on time when this is ran again (COMPLETED),
 find out why very rarely code will hang and requires a manual refresh in the browser rather than being caught by my wait conditions, and fix that issue.
 change time.sleep to webdriver wait conditions in earlier portions of code
 take username and password as arguments
 maybe, change file save location to be at C:\Program Files (x86) that way users could simply run program and not be bothered where program is being saved.
 build a GUI? would look better as a project to potential employers
