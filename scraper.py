from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time

df = pd.DataFrame()

mainlink = 'https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiz9uTzkdPvAhXRwTgGHchPAEgQPAgI'

find = input("Enter the search terms: ")
driver = webdriver.Chrome('chromedriver.exe')
driver.get(mainlink)
search = driver.find_element_by_name("q")
search.send_keys(find)
search.send_keys(Keys.RETURN)


Page_Number = []
Search_Result_Number = []
Search_Result_Title = []
Search_Result_URL = []
Search_Result_Description = []


def main():
    for i in range(10):
        make_list(num = i+1)
        new = driver.find_element_by_class_name("GyAeWb")
        new = new.find_element_by_class_name("D6j0vc")
        new = new.find_element_by_id("center_col")
        new = new.find_elements_by_tag_name("div")
        j = new[-2]
        j = j.find_element_by_tag_name("span")
        j = j.find_element_by_tag_name("table")
        j = j.find_element_by_tag_name("tbody")
        j = j.find_element_by_tag_name("tr")
        j = j.find_elements_by_tag_name("td")
        for k in j:
            if(k.get_attribute("aria-level")):
                k = k.find_element_by_tag_name("a")
                k = k.get_attribute("href")
                mainlink = k
        driver.get(mainlink)

                        

def make_list(num):
    title = driver.find_element_by_class_name("GyAeWb")
    title = title.find_element_by_class_name("D6j0vc")
    title = title.find_element_by_id("center_col")
    title = title.find_element_by_class_name("eqAnXb")
    title = title.find_element_by_id("search")
    title = title.find_element_by_xpath('//*[@id="search"]/div')
    title = title.find_element_by_xpath('//*[@id="rso"]')
    title = title.find_elements_by_class_name("hlcw0c")

    for thisone in title:
        counter = 1
        temp = thisone.find_elements_by_class_name("g")
        for alsothis in temp:
            temmp = alsothis.find_element_by_class_name("tF2Cxc")
            temmp2 = temmp.find_element_by_class_name("IsZvec")
            temmp2 = temmp2.find_element_by_tag_name("span")
            temmp2 = temmp2.find_elements_by_tag_name("span")

            if(len(temmp2)>1):
                temmp2 = temmp2[1]
                Search_Result_Description.append(temmp2.text)
            elif(len(temmp2)==1):
                temmp2 = temmp2[0]
                Search_Result_Description.append(temmp2.text)
            else:
                Search_Result_Description.append("None")

            temmp = temmp.find_element_by_class_name("yuRUbf")
            temmp = temmp.find_element_by_tag_name("a")

            Search_Result_URL.append(temmp.get_attribute('href'))
            Search_Result_Number.append(counter)
            counter = counter + 1

            temmp = temmp.find_element_by_tag_name("h3")
            temmp = temmp.text

            Search_Result_Title.append(temmp)
            Page_Number.append(num)
        counter = counter + 1


main()

'''This part is fixes the numbering '''
counter = 1
for i in range(len(Page_Number)):
    if(Page_Number[i]==2 or Page_Number[i] == '2'):
        break
    elif(Page_Number[i]==1 or Page_Number[i]=='1'):
        Search_Result_Number[i] = counter
        counter = counter + 1


df['Page_Number'] = Page_Number
df['Search_Result_Number'] = Search_Result_Number
df['Search_Result_Title'] = Search_Result_Title
df['Search_Result_URL'] = Search_Result_URL
df['Search_Result_Description'] = Search_Result_Description



df.to_csv('out.csv',index=False)
