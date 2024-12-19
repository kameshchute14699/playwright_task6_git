
from utils.extractHtml import getHtml
import pandas as pd

flipUrl = flipUrl = "https://www.flipkart.com/lenovo-chromebook-mediatek-kompanio-520-4-gb-128-gb-emmc-storage-chrome-os-14m868/p/itm4dc67999fe3de?pid=COMGSYYSHRSUEGMG&lid=LSTCOMGSYYSHRSUEGMGL82DZU&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&spotlightTagId=TrendingId_6bo%2Fb5g&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=search-autosuggest&iid=ca214ef2-5054-422b-9941-c9a376741f50.COMGSYYSHRSUEGMG.SEARCH&ppt=sp&ppn=sp&ssid=9ybdp38uog0000001734087623220&qH=312f91285e048e09"
flipHeader = {
       "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-full-version": "\"131.0.6778.110\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.110\", \"Chromium\";v=\"131.0.6778.110\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "T=TI172079069121200297791422555960968590743343772020249886864546710436; rt=null; K-ACTION=null; ud=3.1YH-VQLXEJIPFTR2NXRbtrFBI1Ikpem14K1KL6owcduhQnpAnUc95ihBUewUCT40AUoQ0xOAYyIQ44r5ZXaTwTlzBb05Wggv0EkCmZmnKpLwE7hQn8F_tVkthKIADnx7-mGA_jFhMv-66u-hMU8aCg; _pxvid=1ee808a3-4052-11ef-8b09-72e7961c7e89; vh=730; vw=1536; dpr=1.25; _fbp=fb.1.1729342376358.857185674627723639; _gcl_au=1.1.212419559.1729342376; _ga=GA1.1.46644770.1729342378; _ga_0SJLGHBL81=GS1.1.1729342378.1.0.1729342380.0.0.0; _ga_TVF0VCMCT3=GS1.1.1729342378.1.0.1729342380.58.0.0; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzU2MTcwMTQsImlhdCI6MTczMzg4OTAxNCwiaXNzIjoia2V2bGFyIiwianRpIjoiMDBmZWIxY2EtNTkzOC00MjdiLThhYTYtZTkzMmRkNGQwNGFkIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzIwNzkwNjkxMjEyMDAyOTc3OTE0MjI1NTU5NjA5Njg1OTA3NDMzNDM3NzIwMjAyNDk4ODY4NjQ1NDY3MTA0MzYiLCJrZXZJZCI6IlZJQ0IxNDg2NEJGMEI3NDE0MzhCRjVBQ0M0NkY0Mzk5NEUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJIWUQiLCJtIjp0cnVlLCJnZW4iOjR9.am5XgIbAEYoFqyR0vkfJgYtKbaPc52Ic1wa3xLqrOP4; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20069%7CMCMID%7C69765528605734062334443235370456066265%7CMCAAMLH-1734493808%7C12%7CMCAAMB-1734493808%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1733896208s%7CNONE%7CMCAID%7CNONE; qH=312f91285e048e09; vd=VICB14864BF0B741438BF5ACC46F43994E-1725074162374-40.1733975759.1733975759.158521309; Network-Type=4g; S=d1t13fCkXZD8/Bj8/Pz9QPyMfP+CYdh1NJv2+8lkpmuFxSlswdBCLS16dOF99nE2eA7zIQ8pfK/lQN2yYYytHzL8gKA==; SN=VICB14864BF0B741438BF5ACC46F43994E.TOK952F4124ADEA4CAA918E8C7724C20988.1733975765494.LO"
  
}

if __name__ == '__main__':
    
        flipData = getHtml(websiteUrl=flipUrl,showBrowser=True,screenshotName='lp4')

        allimg = [img.text()for img in flipData.css('div[class="cPHDOP"]')]
        print(allimg)

        allratings = [ratings.text() for ratings in flipData.css('div[class="ISksQ2"]')]
        print(allratings)

        allPrice = [Price.text() for Price in flipData.css('div[class="UOCQB1"]')]
        print(allPrice)

        allMemory = [Memory.text() for Memory in flipData.css('div[class="WGBwfw"]')]
        print(allMemory)

        allData = {
            'img': allimg,
            'ratings': allratings,
            'Price': allPrice,
            'Memory': allMemory,
        }
        
        df = pd.DataFrame(allData)
        df.to_csv('flipkartdata.csv')

        
