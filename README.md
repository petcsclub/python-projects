# python-projects
Python Projects for Intro to Python Section

# How to Use
Preface: everything here will be done on repl.it. You are welcome to do things locally if you'd like too! 

1. Connect GitHub to replit account
	1. Go to https://repl.it/~
	2. You should see an option to connect your GitHub to your repl.it account, click it and follow the instructions
2. Click [![Run on Repl.it](https://repl.it/badge/github/petcsclub/python-projects)](https://repl.it/github/petcsclub/python-projects) This will create a repl in your own personal folder, not on the PETCS folder.
3. Create a new branch
	1. Click the version control menu on the left sidebar (second one down).
	2. You will see a text field that says: "branch: master". Beside that field, you will see a plus sign. Click it to create a new branch, and name it depending on what you're creating (e.g., name the branch battleship if you're making the game battleship)
4. Setup project
	1. If you are just making a simple game with only one variant, you probably only need one file. In that case, just make a file in the root of the repl (e.g., `battleship.py`)
	2. If you are making multiple variants of the game, you should make a folder. Create a new folder in the root of the repl with the appropriate name (e.g., battleship). Then in that folder, make the appropriate files depending on the variants (e.g., `battleship-single-player.py`, `battleship-multi-player.py`)
5. Start coding!
	1. To run the file, run the following command in the terminal: `python directory/filename.py`. Examples: `python battleship.py` (for the first example with only 1 file), `python battleship/battleship-single-player.py` (for the second example with multiple files)
	2. Commits! Make a commit every time you make some sort of small change to your code. That way, it is easier to track your progress over time and make fixes/revert changes if things go wrong (in the chance that they do). The rule of thumb is "commit early, commit often", at least a couple times every hour.  Worry more about making too few commits than too many.
	3. Commit messages: actually make them meaningful and write about what changes you made. More specific = better, but don't go toooo specific.
	4. How to make commits? Again, go to the version control. In the what did you change? text box, write the commit message. Then click the button "commit and push". That's one commit!
	5. Note: if you need to switch between branches, commit all your changes before doing so. Otherwise, all your changes will be lost! :( 
6. Create a pull request
	1. If you think you're done the project, make sure everything is commented and there aren't any visible/obvious errors. Then go to the [website of the repo](https://github.com/petcsclub/python-projects) and create a pull request for your specific branch. Read more here on how to [create one](https://guides.github.com/activities/hello-world/#pr). 
	2. Assign 2 reviewers to your code, assign yourself as the assignee, and set the label to be "enhancement"
	3. Description: write a lil intro, a brief description of the different variants, and anything else you think the reviewers should know! If you have multiple variants, maybe state the ones the reviewers should look at first. 
	4. We'll have a couple people review your code, check it for bugs/flaws, and have you fix up a couple things if you need to. Then we'll merge the pull request. Congrats!
7. How to review pull requests:
	1. If you're assigned to review someone's pull request, congrats! It's a HUGE honor 😄
	2. First of all, it's probably best to switch to the branch you're reviewing either on repl.it or locally. Play both variants of the game for a bit to get a feel on how things are implemented. 
	3. Now it's start to dive deep into the code! Start at the simpler variant. Start from the main game loop to understand how the high level process, what data structures are used for, etc. If that all makes sense, dive into the specific functions to make sure all the logic is correct! After the simpler variant makes sense, take a look at the more complicated ones and repeat the same process. It's okay to not do this all in one shot, especially if the code is long. It takes time to wrap your head around someone's code! If there's something you don't understand or is unclear, make a comment on the pull request (remember to mention the assignee).
	4. Once you're done reviewing the code/while reviewing the code, add your feedback on the pull request. Include everything, both good things and things that could be improved, including formatting, logic, whether more comments would be more appropriate, if there were concepts the assignee used that weren't taught, if there would be a better way to structure things entirely, etc! Do so by clicking the "Review Changes" button, and adding general comments in the review summary (open and close by clicking the "Review Changes" button), as well as inline comments for specific lines of code (hover over the line and click the blue + button that pops up)
	5. If everything looks perfect, click "Approve". If there are changes you'd like the assignee to make, click "Request Changes". If you want to suggest some optional changes, click "Comment"
	6. After the assignee has responded to your feedback and fixed everything up, make sure they've fixed everything properly. If they have, check in with the other reviewer to confirm that everything is spick and span. If both of you think everything looks good, allow the assignee to approve the pull request! YAY! 

If you have any questions, please ask them in the #python channel! 
