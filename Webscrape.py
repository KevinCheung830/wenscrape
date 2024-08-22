import requests
from bs4 import BeautifulSoup
import re
import csv

def extract_contact_email(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all email addresses on the page
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', soup.get_text())
        
        # Find contact email based on common patterns
        contact_email = None
        for email in emails:
            if 'contact' in email or 'support' in email or 'info' in email:
                contact_email = email
                break
        
        return contact_email
    else:
        return None

# Get the URL from the user
url = input("Enter the URL of the website: ")
contact_email = extract_contact_email('url')

if contact_email:
    print(f"The contact email on {url} is: {contact_email}")
    
    # Write the data to a CSV file
    with open('contact_emails.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Website URL', 'Contact Email'])
        writer.writerow([url, contact_email])
        
    print("Data saved to contact_emails.csv.")
else:
    print("Contact email not found or website not accessible.")