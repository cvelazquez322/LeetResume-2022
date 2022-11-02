# LeetResume-2022
The purpose of this project is for there to be a clear and easy way to download solved leetcode questions. 

I started this project when I realized I hadn't uploaded to github in awhile and I wanted to show prospective employers that I had been coding over the last year.

I went to leetcode to download my previous submissions, 
however I soon realized that there was not a way to download my solved questions and that it would be rather monotonous to go through, 
question by question, copy and paste the code of each solved problem into a text editor, and then save it.

So instead I created LeetResume, a quick and efficent way to download my solved problems. 

the following are instructions I've added at the front of my code so that others can use my program as I build it:


 Note to anyone using this, change the lines of os.mkdir/chdir to wherever you'd like for your LeetResume to be saved.
 You will also need to have Selenium and FireFox installed. 
 
 if the above conditions have been satisied, you can simply run the program.
 
 
 Please note that this is still a work in progress, but I've done my best to error proof LeetResume.
 The code should catch most errors, and restart from where it fails, all on its own without any user intervention... most times. 
 However if for some reason it doesn't catch the error, you can restart the code from where it left off at by inserting values into the argument at line 240
 'rlist.append(leetResMain())' can take arguments that will be equal to co-ordinates, if you put rlist.append(leetResMain(5,2)) it will resume on problem 4 of the third solved page,
 
 
 this is a free resource and I will be updating it regularly.
 currently it takes ~10 seconds from start to finish to download one problem, and then move to the next.
 After reloading webpage script resumes where it leaves off.

 planned updates: sort problems by difficulty level when saving to local file (COMPLETED),
      
      Completed by: when getting problem name, select problem difficulty, and save it so that later we can use it to navigate to the difficulty folder.
      had to create difficulty folders in 'Step: 0'
 
 cut down on time (COMPLETED),
      
      Completed by:adding webdriver.wait conditions rather than hard coding time.sleep(x)
 
 save file type as code it was originally written in instead of .txt (COMPLETED),
      
      Completed by: During step 0 created a dictionary which holds language name as key, and their file extensions as values.
      {'Python3' : '.py'} while getting problemSolution information, there's a small section that states what language the problem was solved in.
      We can use this by inputting it into our dictionary, and appending what file type should be use.
 
 save fastest code rather than first accepted code (DROPPING FROM PLANNED UPDATES, might add back at a a later time),
      
      Note: Leetcode can give various time for various code, the same code given multiple times can have worst 5% efficency or highest 90% efficency.
 
 skip over code that's already saved locally to computer which will drastically cut down on time when this is ran again (COMPLETED),
      
      Completed by: during step 0 create a list of all files within the Easy, Medium and Hard subfolders, then strip everything but the numbers from the problem 
      take this list and turn it into a dictionary for faster lookup time. 
      When getting a problems title, check to see if its unique number ID is already within my dictionary. 
 
 
 
 take username and password as arguments (COMPLETED)
 
 protect password by not echoing to the screen what password is being typed in. (COMPLETED)
 
 maybe, change file save location to be at C:\Program Files (x86) that way users could simply run program and not be bothered where program is being saved.
 
 
