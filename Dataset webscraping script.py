from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Headless Google Chrome environment for Webscraper
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=r'./chromedriver')

 
#Input and output files
with open('tagine_sitemap_output.txt', 'r') as input:
    data = []
    for line in input:
        data.append(line)
 
#Function to write the output 
def output_writer(Page_data):
    output = open('scrapped_data.txt','a')
    result = str(Page_data)
    output.write(result)
    output.write('\n')
    output.close()

#Webscraper Loop 
for link in data:
    try:
         driver.get(link)
         English_word = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[4]/div[2]/div/article/div[1]/div[2]/div[1]/h2")
         Darija_word_ar = driver.find_element(By.XPATH, "//html/body/div[1]/div/div[4]/div[2]/div/article/div[1]/div[2]/h5")
        # Darija_word_latin = driver.find_element(By.XPATH, "//h5/q")
         Page_data = {   English_word.text, Darija_word_ar.text}#Darija_word_latin.text
         output_writer(Page_data)
    except:
        brokenlinks = open('broken_links.txt','a')
        brokenlinks.write(link)
        brokenlinks.write('\n')
        brokenlinks.close()
 

driver.quit()
input.close()
