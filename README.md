# iStats - iMessage Statistics

Team Members: Bryce Brooks, Wyatt Harrell, Myra Mullis, John Rawley

Objective: provide analytics on IMessages from IMessage app on MacBook. 

Features:         
  · Read chat History from chat.db file and load into program
	SQLite to pandas 
  · Perform analytics on message history
	Average character count per message 
	Min and max characters per conversation 
	Messages per attachment ratio 
	Timing between replies/responses 
	common phrases used
	etc. 
  · Filter by day, time of day, and person 
  · GUI
	Matplotlib
	Flask
	
Proposed Work Breakout:
1.	GUI, graphics – Lead: Wyatt, Second: John  
2.	Stats – Lead: Bryce, Second: Myra
3.	Data Management – Lead: Myra, Second: Bryce
4.	File read in – Lead: John, Second: Wyatt  

Work So Far:
Due to some API difficulties, we have decided to change our project. Currently we have a semi working functions to read from the chat.db, using sqlite3. We are also working on our Flask front end to display and navigate the various results. Lastly, we are looking into the pros and cons of using the SQL database directly vs creating a new database within the program. 

Timeline:
  · End of June:
  	Have reading from chat.db complete and tested. 
	Complete list of Analytics
	Concrete Data storage
  · Mid July:
	Analytics Complete for testing
	GUI Functional 
  · End of July
	Completed testing and debugging. 
	
Myra
	-min and max characters 
	-average character count per message
	-min and max characters per conversation
	-who you text the most to the least
	-most common phrases

Bryce
	-emojis
	-most common emojis
	-use old Data Structures assignment 
	-most common time of day to send texts


Github slides: https://glfmn.github.io/gh-slides/#/1
