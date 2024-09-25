# CMSC-355-Project
Sprint 1:
The iteration starts with opening up a GUI that will prompt the data entry tab. The data entry tab is used to find a member within the gym system and you can edit, delete, or add a customer to/from the gym system. It contains a search bar where it would match your search and only show the relevant customer(s). Then apart of the data entry tab there is a check-in tab. The check-in tab contains all the member's who have checked in. In order to check in a member we just search them up in the data entry tab and click on check in then their name would pop up along with the time they checked in, in the check-in tab. Lastly to close the tab you would just exit as if it was a normal tab.

Some problems we faced at first was how to get a proper gui to operate. The concept of adding options to choose from and how to add/edit/remove members was difficult at first. Another problem we stumbled upon was the check-in tab especially in how we wanted to implement it and how the customer info would get transferred from the data entry tab to the check-in tab. 

----------------------------------------------

Sprint 2:
In this iteration of the project we were tasked with creating a UML class diagram, two more use cases, and two test cases for the use cases. The two use cases we decided to add to our 'Gym Check-in System' are a "calendar tab" for event planning and a "POS tab" for purchasing items from the gym. 

For the first use case, the calendar system, we implemented a calendar that allows the gym to plan and schedule events. This tab contains a calendar for the month. When the user clicks on a date it allows the user to create and add an event to the day. A challenge we faced implementing this use case was saving the event after the tab was closed.

The second use case, the POS, allows the system to be able to sell items from the gym. The standard process for operating this POS begins with selecting an existing customer in the database. This allows us to keep a purchase history for each customer. Next, we can select the items the customer is purchasing. Finally we can complete the purchase and get payment. The main challenge we had with this use case was figuring out how to use the Java-Swing library to create an intuitive and user-friendly interface.

Overall, during sprint 2 we organized and solidified our plans on what we want our system to be and how we plan on developing it.

----------------------------------------------

Sprint 3:

In this iteration, we decided that our final use case would be a clock-in/out panel. We called the panel "Time Sheet." It contains  search bar at the top, like out other panels, that reacts responsively to the input and shows results that match the given name from the database. The user can click on the desired result and press the "clock in" button to add the name to the list of people currently clocked in, which is displayed in the panel at default when the search functionality is not being used. The time that they clocked in at is displayed on the right side of their name, and then when their shift is over they can select their name from the list and press the "clock out" button. When they do this, the difference between the current time and the time that they clocked in at is calculated, showing them the number of hours that they've clocked for the shift. The biggest challenge we faced here was thinking of a good way to calculate the amount of time that the employee had spent on shift, with the original idea being a timer that displayed on the side, but we faced some issues with Java Swing Timer and Duration library and changed course to calculation on clock-out. 

We also made some improvemenets to the overall design of the application. We altered the code so that any pop-up windows would be centered, rather than appearing in the top left corner of the screen, and changed up the layout of the calender a little bit. So long as everyone who purchases items form the gym uses cash, and so long as the employee can calculate sales tax in their head, the application is ready to use. 
# random-sentence-generator
