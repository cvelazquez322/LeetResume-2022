# LeetResume-2022
The purpose of this project is for there to be a clear and easy way to download solved leetcode questions. 

I started this project when I realized I hadn't uploaded to github in awhile and I wanted to show prospective employers that I had been coding over the last year.

I went to leetcode to download my previous submissions, 
however I soon realized that there was not a way to download my solved questions and that it would be rather monotonous to go through, 
question by question and download each solved problem.

So instead I created LeetResume, a quick and efficent way to download my solved problems. 

the following are instructions I've added at the front of my code so that others can use my program as I build it:


 Note to anyone using this, change the lines of os.mkdir/chdir to wherever you'd like for your LeetResume to be saved.
 You will also need to change loginElem and loginElemPass to whatever your login email and password is. 
 You will also need to have Selenium installed. 
 
 if the above two conditions have been satisied, you can simply run the program by hitting F5 in idle and letting the program run.
 
 
 Please note that this is still a work in progress, but I've done my best to error proof LeetResume.
 The code should catch most errors, and restart from where it fails... most times. 
 However if for some reason it doesn't catch the error, you can restart the code from where it left off at by inserting values into the argument at line 240
 'rlist.append(leetResMain())' can take arguments that will be equal to co-ordinates, if you put rlist.append(leetResMain(5,2)) it will resume on problem 4 of the third solved page,
 note that as of right now you should not resume on the very last page, as this could cause an error.  
 this is a free resource and I will be updating it regularly.
 currently it takes ~10 seconds from start to finish to download one problem, and then move to the next.
 very rarely code will get stuck on a page, not sure why webdriver.wait doesnt catch this, but simply refresh the webpage.
 After reloading webpage script resumes where it leaves off.

 planned updates: username and password taken as input from the user, sort problems by difficulty level when saving to local file, 
 cut down on time, save file type as code it was originally written in instead of .txt,
 save fastest code rather than first accepted code, skip over code that's already saved locally to computer.
