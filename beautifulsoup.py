from bs4 import BeautifulSoup
import requests

# fetching webpage content
url = 'https://rdpolytech.blackboard.com/webapps/blackboard/execute/displayLearningUnit?course_id=_51595_1&content_id=_3590326_1#'

response = requests.get(url)
html_content = response.content

#Parse the html content BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract specific elements
table = soup.find(id='simpleTable')

print(table)