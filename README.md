# Software for Global Market 2 CA
### Oscar Canavan (C24425236), Austin Coules (C23444946), Daniel Courage (C23491584)

## Overview
Chow Now is the concept of a food delivery website. In this demo there are three main pages: the landing page, where you
can see a list of restaurants, a restaurant page, where you can see the food options for an individual restaurant, and
the checkout, which shows a receipt of food items, a progress tracker and a support section.

## Cultural Scope
The cultures we targeted were an Irish market, a German market and a Polish market. We identified in phase 1 the
different traits of these markets and found several ways that they would shape the website. These areas include how a
user would navigate restaurant and food selection, how a user would prefer to see how close their delivery is, and how a
user would want to receive support.

## Architecture and Structure
The main structure of the page contains a navbar and the logo of the application in the top left.
The Structure of the pages is as follows: 
a landing page, a restaurant menu page and a checkout page.
The UI for the landing page contains a selection of 3 restaurants catered for each market, each containing a rating and estimated time for delivery.
The UI for the restaurant page contains a selection of 12 items from the restaurant selected along with a sidebar and searchbar. It also has deals and promotions for each market.
The UI for the checkout page displays a window displaying the status of the order and progression symbols that signify what stage the delivery is at.
It also contains a receipt of items purchased along with delivery method. Drop down menus are at the bottom for German and English and an email and phone number for Polish.

## Internationalisation and Localisation
Localisation:
The landing page was designed so that when a certain language is chosen, restaurants catered towards that culture appear on the home menu.
The restaurant page has 6 menu items that change upon changing the language, giving users choices that they are familiar with within their home country.
Filtering options are available towards the German market as they tend to be more specific. Promotional deals are displayed at the top rather at the bottom for the Polish market as they tend to chase trends more.
The checkout page contains a live chat button for the German market, and for the Polish market it contains just an email and a phone number.

Internationalisation:
The landing page contains restaurants that are globally known across each language (E.g., Domino's)
The restaurant page contains 6 menu items that are known internationally and do not change per language.
The checkout page consists of a familiar and easy to read receipt and process stage indicator that can be easily understood by anyone.
## Cultural Adaptation Mechanisms

## Individual Contributions
### Austin
I worked on the checkout page for this website. This involved several sections, including a receipt showing the
purchased items, a progress tracker to show when the food delivery should arrive, and a support section where you could
get help once you have paid for your order. For both the progress tracker and support sections there were several
aspects that I localised to each target culture. I translated this page into German and Polish. I also designed and
implemented the navigation bar, which includes the locale switcher needed to demonstrate the differences in localisation
and translation.

I also set up and managed the GitHub repository, coordinating merges and maintaining the issue tracker.

### Daniel

I authored the HTML and CSS styles for restaurant and designed the webpage for the restaurant menu for Polish, Irish and German markets.
This included menu options, filtering options for the different markets and promotional deals that change based on what user is accessing the webpage.
It uses a familiar design to what each culture is used to when accessing a food app along with the differences catered to each culture, such as food items or promotional deals.

### Oscar

## Running this Project
### Dependencies
``pip install flask flask-babel``

From there just run ``main.py`` and the Flask server will boot. Note that this also compiles the translations into
``.mo`` and this script may need to run twice before Flask detects the change.

## Limitations and Future Work
The biggest limitation was the lack of a backend or any underlying logic. For the scope of the project there was no
ability to fully implement concepts such as the filtering system or a search function. The entire website is static.
In the early stages of this project we considered having concepts such as a dynamic receipt based on the food items you
selected in the restaurant page.

Another limitation was our lack of experience using Git. We especially found trouble when trying to add the translation
binaries, since it was much harder to resolve the merge conflicts once changes were made.

If we were to work on this in the future, implementing more dynamic content such as a dynamic grid of restaurants, food
and a functioning shopping cart system would elevate this project. Becoming more familiar with Git and how to handle
conflicts would make the design much more seamless.