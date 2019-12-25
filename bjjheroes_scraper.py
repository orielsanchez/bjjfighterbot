import requests
from bs4 import BeautifulSoup
from csv import writer

end_page_num = 55

with open('fighters.csv', 'w+') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Fighter', 'Summary', 'Link']
    csv_writer.writerow(headers)
    i = 1
    while i <= end_page_num:

      response = requests.get('https://www.bjjheroes.com/category/bjj-fighters/page/{}'.format(i))
      soup = BeautifulSoup(response.text, 'html.parser')
      fighters = soup.find_all(class_='item-medium post-box-big')
      for fighter in fighters:
        fighter_name = fighter.find(
            class_='entry-title').get_text().replace('\n', '').strip()
        fighter_summary = fighter.find(
            class_='i-summary').get_text().replace('\n', '').strip()
        fighter_link = fighter.find('a')['href']
        csv_writer.writerow([fighter_name, fighter_summary, fighter_link])
      i+=1
