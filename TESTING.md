![Want That logo](readme_assets/readme_images/want_that_logo.jpg "Want That logo")

# Testing the 'Want That' app 

## Testing
- HTML validated using [W3C Validator](https://validator.w3.org/) _NOTE: Errors sometimes appear which are relating to external retailer images and their associated code._
- CSS validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
- Python validated using [PEP8 online check](http://pep8online.com/)


## Testing client stories from the UX section of README.md

1. _“I have to go to a wedding in August and need a new outfit. I’m not particularly brand loyal and have been browsing lots of different websites trying to find something. I’ve seen lots of things but can’t keep track of everything! I need **to start a list of all the things I’ve seen online** so I can easily pick something when I'm ready.”_
- This user can achieve their mission in 3 steps: _Click **ENTER** on the welcome page > Click **Create a list** on the My Lists page > Enter details and press **Create List**_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story01.jpg)

2. _“Work has been quiet so I’m spending a lot of time browsing online. I’m not going to have as much money this month as I normally do, so will wait until next payday to treat myself. I have a few favourite brands and want to collate links to their new stuff in one place so when I’ve got money in the bank, I know what I’m going to buy! I will **need to remove items**, depending on how much money I have.”_
- This user can do this in minimum of 3 steps: _Click **ENTER** on the welcome page > Click on their a chosen **list name** on the My Lists page > Filter through their items and click **Delete item**_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story02.jpg)

3. _“I love online shopping because I hate going into actual shops nowadays. I was building a list of things on 'Want That' for my boyfriend’s birthday and have now bought him something. **I need to get rid of the birthday list**.”_
-This user can achieve their mission in 2 steps: _Click **ENTER** on the welcome page > Find their chosen list on the My Lists page then click **Delete list** to remove the list
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story03.jpg)

4. _"I have a lot of free time and spend a lot of time browsing the web. I'm very image conscious and like to keep up to date with fashion and brands and use 'Want That' to collate all the things I've seen. When I'm ready to buy something, **I'll check my list and go to the retailer's site**. I used to forget what I wanted before!"_
-This user can achieve their mission in 3 steps: _Click **ENTER** on the welcome page > Find their chosen list on the My Lists page > Click on an **item name** to be taken to the retailer's site
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story04.jpg)

5. _"I've made a list on WANT THAT and something has now gone on sale. I want to **update the item** with the new price (and buy it as soon as possible before it's sold out)"_
- This user can achieve their mission in 5 steps: _Click **ENTER** on the welcome page > Find their chosen list on the My Lists page > Find their item and click **Edit item** > Enter the amended price in the **input field** > Click on **Update item** at the bottom of the page
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story05.jpg)

6. _"I've got so many lists and it's a nightmare trying to find something in random order. I will **sort lists alphabetically** to make my search easier"_
- This user can achieve their mission in 2 steps: _Click **ENTER** on the welcome page > Click **Sort lists alphabetically** to display results in ascending alphabetical order_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story06.jpg)

7. _"I've got a list of things I want but not all of them are important. I want to **see which items I've marked as 'need urgently'** to buy today."_
- This user can fulfill their mission in 3 steps: _Click **ENTER** on the welcome page > Find their chosen list on the My Lists page > Click on Sort items by: **Urgency** for the results to be displayed with the most urgent results first_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story07.jpg)

8. _"I've been making a list of white trainers and really want to buy the Adidas ones. I will **sort the list alphabetically** to see the Adidas ones first."_
- This user can fulfill their mission in 3 steps: _Click **ENTER** on the welcome page > Find their chosen list on the My Lists page > Click on Sort items by: **Brand name** for the results to be displayed alphabetically_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story08.jpg)

9. _"I want to buy something on my list, but ideally not the most expensive thing. I will **sort the list to show the prices in ascending order**"_
- This user can fulfill their mission in 3 steps: _Click **ENTER** on the welcome page > Find their chosen list on the My Lists page > Click on Sort items by: **Price** for the results to be displayed alphabetically_
- [User journey screenshots here](https://github.com/trisdauvergne/milestone-project-03/blob/master/readme_assets/user_journey_screenshots/user_story09.jpg)

### Manual (logical) testing of all elements and functionality on every page.

#### Navigation bar:
- Click the logo to go back to the welcome page when clicked on
- Click the three destinations in the navigation bar to ensure they go to the correct pages
- Reduce screen size to see the navigation menu items (My lists, Create a list, Add to a list) disappear into a collapsable menu
- Scroll down the page to see the navigation bar stays at the top of the viewport while you scroll down to the bottom
#### Active elements:
- Hover over all elements in the navigation bar to check they have different coloured backgrounds when hovered on a desktop
- Check that active elements in navbar have coloured underlines on screens tablet sized and smaller

### Welcome page:
- Click the enter button to check that it goes to the My Lists page
- Check responsiveness and that four areas of content become two on a mobile sized screen

### My Lists page:
- Check that list names are loaded on the page with a description underneath them and options to add to the list, edit list and delete list
- Click 'sort lists alphabetically' to check that the lists become displayed in alphabetical order by list name 
- Check that when the 'add to the list' button is clicked, it goes to the add item page
- Check that when the 'edit list' button is clicked, it goes to the edit list page
- Check that when 'delete list' is clicked, a confirmation page appears saying the list has been deleted
- Check the row elements in this page remain stacked on all screen sizes

### Create A List page:
- Input information into form and check that form won't submit without both input fields having a value
- Check on the list created confirmation page that the user can click 'go back to lists' and go back to the My Lists page
- Check the elements in this page remain stacked on all screen sizes
- Check in the database that the list has been added to the database 

### Add to List functions:
- Click on 'add to a list' in the navbar and check that it takes you to a page that displays all the existing lists
- Click on 'add to this list' on the My Lists page to check that it opens a page that enables you to add an item and that the list name has been populated from the database
- Input information into form and check that form won't submit without all input fields having a value
- Check that a URL must be input into product link and image link values
- Check that only a number can be input into product price value
- Check that product types, 'how much do I need this?' are dropdowns with a value to select from
- Check in the database that the item has been added as a nested object within the list
- Check that format remains stacked in all screen sizes
- When item is submitted, on the 'item added' confirmation page, check that the option to add another item works
- Also on the 'item added' confirmation page, check that the option to view the list works and that it takes you to the correct list with prepopulated items information
- Refresh a list items page and check in the database to see that the information has been added

### Edit List page:
- Check that the list's current information is populated in the input boxes
- Click submit and on the 'list edited' page, confirm that the link to view items in the list takes you to the list's items page
- Check in the database and refresh the 'My Lists' page to check the information has been updated
- Check the elements in this page remained on all screen sizes

### Delete List function:
- Delete a list from the 'My Lists' page and from an items list page
- Check in the database and on the 'My Lists' page to see that the list and its nested objects have been removed

### List Items page:
- Check that all items from a list are populated from the database on to the page
- Check that the brand name and product type form the item heading, and that when clicked this takes you to the retailer's site
- Click on 'edit item' in an item's row to check that it takes you to the edit item page
- Click on 'delete item' in an item's row, then refresh the page to check in the database to see that item has been deleted
- Click on the 'brand name' option to sort results alphabetically according to the brand name
- Click on the 'price' option to sort results by price, starting with the lowest price
- Click on the 'urgency' option to sort results by urgency, starting with the most urgent items at the top
- Click on 'add to this list' at the bottom of the page to check that it takes you to the add item page
- Click on 'delete this list' to check that it deletes the list and its contents, then check the database and load the 'My Lists' page to check the contents has been removed
- Reduce screen sizes to check that the rows stay intact and the product images bleed off the screen to the left on mobile sized screens

## Further testing:

1. Asked fellow students to look at the site and report any issues they encountered. Issues encountered include:
- No confirmation before deleting a list or item, this will be implemented at a later date.
- Intro copy on welcome page disappeared behind image on wide screen sizes. This has been rectified
2. Friends have tested the site for readability and ease of use
3. The website has been viewed on different browsers, no issues were found