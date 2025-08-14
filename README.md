**Project Overview**

This project is part of my internship tasks. The goal is to scrape the latest top 10 headlines from the Times of India Briefs page and store them in a .txt file for later use.

**It demonstrates skills in:**

-- Web scraping using Python

-- HTML parsing with BeautifulSoup

-- Data storage in a text file

-- Error handling

-- Writing clean and readable Python code

**🛠️ Technologies Used**

***Python 3

Requests – For sending HTTP requests

BeautifulSoup (bs4) – For parsing HTML

Times of India Briefs – Source website for headlines***

**📂 Project Structure**
📁 WebScraping-Headlines
 ├── web_scrap.py              # Main Python script
 ├── news_headlines.txt        # Output file with headlines
 └── README.md                 # Project documentation
 
**📜 How It Works**

The script sends a GET request to the Times of India Briefs page.

It parses the HTML content using BeautifulSoup.

It selects the first 10 headlines from the webpage.

It saves the headlines into news_headlines.txt.

It prints the number of headlines saved.

**Output**
✅ 10 headlines saved to news_headlines.txt
**Example:** 

***Note: -- Headlines may change as the website updates.
-- Make sure you have internet access when running the script.***

-- PM addresses the nation on Independence Day
-- India vs Australia: Test series updates
-- ISRO successfully launches new satellite
-- Government announces new policy reforms
-- Heavy rains cause floods in several states
-- Stock market hits record high
-- Electric vehicle sales rise sharply
-- Global leaders meet for climate summit
-- New education policy approved by cabinet
-- Health ministry issues new COVID guidelines
