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

## Internationalisation and Localisation

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
It uses a familiar design to what each culture is used to when accessing a food app along with the differences catered to each culture.

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