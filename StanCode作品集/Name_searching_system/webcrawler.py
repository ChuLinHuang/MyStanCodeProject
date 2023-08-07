"""
File: webcrawler.py
Name: Chu-Lin Huang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        data = soup.find_all('td')
        int_amount = []
        num = 0
        male_num = 0
        female_num = 0
        for line in data:
            if line.text.isdigit() == 0:
                if line.text.isalpha() == 0:
                    number = line.text  # 數字含有 ','
                    amount = manipulation(number)  # 轉成純數字
                    if amount is not "":
                        int_amount.append(int(amount))  # str 轉成 int

        int_amount.pop()  # 把最後一項不相關的數據刪除
        # print(int_amount)

        for i in range(len(int_amount)):
            if i % 2 == 0:
                male_num += int_amount[i]
            else:
                female_num += int_amount[i]

        print("Male Number: " + str(male_num))
        print("Female Number: " + str(female_num))


def manipulation(number):
    ans = ''
    for ch in number:
        if ch.isdigit():
            ans += ch

    return ans


if __name__ == '__main__':
    main()
