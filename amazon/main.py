import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = input("Enter Link: ")

# link = "https://www.amazon.com/Fortnite-7-Llama-Loot-Plush/dp/B07GJ2MWTZ?pf_rd_r=0WJ5EEY5QMG3E49G21Q3&pf_rd_p=50b1c552-fbbb-4466-acc4-0c0eedd60aba&pd_rd_r=520ca1b9-c349-422d-b5f6-693941f89544&pd_rd_w=CVQJp&pd_rd_wg=91Ube&ref_=pd_gw_unk"
# link = "https://www.amazon.com/Fortnite-FNT0189-Durrr-Burger-Plush/dp/B07L77DMBS/ref=pd_sbs_21_2/132-8052815-0263667?_encoding=UTF8&pd_rd_i=B07L77DMBS&pd_rd_r=d7d6b163-adcf-4344-873d-d2f562bf8762&pd_rd_w=TbKWH&pd_rd_wg=XJSdP&pf_rd_p=b65ee94e-1282-43fc-a8b1-8bf931f6dfab&pf_rd_r=5TNWG7RK2H4CBSPY0EQB&psc=1&refRID=5TNWG7RK2H4CBSPY0EQB"
# link = "https://www.amazon.com/VTech-Kidizoom-Smartwatch-Amazon-Exclusive/dp/B072JXVTKT?pf_rd_r=F9P0YC89QW8XV9N6ZS55&pf_rd_p=4dd821c0-e689-433a-a035-5e03461484eb&pd_rd_r=9d987571-60e0-4caf-9048-093bf08be674&pd_rd_w=8wBaN&pd_rd_wg=hUhUn&ref_=pd_gw_unk"


# -----------------------------------------------
## --- web driver works ---
driver = webdriver.Firefox()
# driver = webdriver.Chrome()

driver.get(link)

xxpath = '//*[@id="imageBlock"]/div[@class="a-fixed-left-grid"]/div[@class="a-fixed-left-grid-inner"]/div[1]/ul/li[4]'
try:
    myElem = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH , xxpath)))
except:
    a=0

# ---
# used to find clickabe images to get real images

html1 = driver.execute_script("return document.documentElement.outerHTML")
soup1 = bs4.BeautifulSoup(html1, 'lxml')

x1 =  soup1.select('#imageBlock_feature_div #imageBlock .a-fixed-left-grid .a-fixed-left-grid-inner #altImages ul .item')

for wew in range(4,len(x1)+4):
    path = '//*[@id="imageBlock"]/div[@class="a-fixed-left-grid"]/div[@class="a-fixed-left-grid-inner"]/div[1]/ul/li[{}]'.format(wew)
    lg = driver.find_element_by_xpath(path)
    driver.execute_script("arguments[0].click();", lg)

# ---
# used for getting the final data
html = driver.execute_script("return document.documentElement.outerHTML")
soup = bs4.BeautifulSoup(html, 'lxml')

driver.close()
# -----------------------------------------------


#title
try:
    print("Title: ",soup.select('#titleSection #title')[0].getText().strip())
except:
    print('Title not found')

#price
try:
    print("\nPrice: ",soup.select('.a-lineitem tr td #priceblock_ourprice')[0].getText().strip())
except:
    print('\nPrice not found')

#details
try:
    details_ini = soup.select('#productOverview_feature_div table tr .a-span3 span')
    details = soup.select('#productOverview_feature_div table tr .a-span9 span')
    if len(details) == 0:
        print("\nDetails: Empty")
    else:
        print("\nDetails: ")
        for ij in range(0,len(details)):
            print(details_ini[ij].getText().strip('').strip('\n')," : ",details[ij].getText().strip('').strip('\n'))

except:
    print('\nDetails not found')

#about
print("\nAbout: ")
try:
    about = soup.select('#featurebullets_feature_div #feature-bullets ul li .a-list-item')
    for ii in range(1,len(about)):
        print(about[ii].getText().strip(' ').strip('\n'))
except:
    print('\nAbout not found')

#image
try:
    img =  soup.select('#main-image-container ul .item img')
    print("\nImages: ")
    for jj in img:
        print(jj.get('src'))

except:
    print('\nImages not found')


# # ------------------------------------------------------------------


