from transitions.extensions import GraphMachine

from utils import send_text_message
import requests as rq
from bs4 import BeautifulSoup

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    #condition
    def is_going_to_news_initial(self, event):
        text = event.message.text
        return text.lower() == "看新聞"

    def is_going_to_TVBS_choose_category(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_Apple_choose_category(self, event):
        text = event.message.text
        return text.lower() == "3"
    def is_going_to_Ltn_choose_category(self, event):
        text = event.message.text
        return text.lower() == "4"
    def is_going_to_CNA_choose_category(self, event):
        text = event.message.text
        return text.lower() == "2"

    def is_going_to_initial_TVBS(self, event):
        text = event.message.text
        return text.lower() == "5"
    def is_going_to_TVBS_choose_social(self, event):
        text = event.message.text
        return text.lower() == "2"
    def is_going_to_TVBS_choose_politics(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_TVBS_choose_world(self, event):
        text = event.message.text
        return text.lower() == "3"
    def is_going_to_TVBS_choose_sport(self, event):
        text = event.message.text
        return text.lower() == "4"
    def is_going_back_to_TVBS_choose_category(self, event):
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_initial_CNA(self, event):
        text = event.message.text
        return text.lower() == "5"
    def is_going_to_CNA_choose_social(self, event):
        text = event.message.text
        return text.lower() == "2"
    def is_going_to_CNA_choose_politics(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_CNA_choose_world(self, event):
        text = event.message.text
        return text.lower() == "3"
    def is_going_to_CNA_choose_sport(self, event):
        text = event.message.text
        return text.lower() == "4"
    def is_going_back_to_CNA_choose_category(self, event):
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_initial_Apple(self, event):
        text = event.message.text
        return text.lower() == "5"
    def is_going_to_Apple_choose_social(self, event):
        text = event.message.text
        return text.lower() == "2"
    def is_going_to_Apple_choose_politics(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_Apple_choose_world(self, event):
        text = event.message.text
        return text.lower() == "3"
    def is_going_to_Apple_choose_sport(self, event):
        text = event.message.text
        return text.lower() == "4"
    def is_going_back_to_Apple_choose_category(self, event):
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_initial_Ltn(self, event):
        text = event.message.text
        return text.lower() == "5"
    def is_going_to_Ltn_choose_social(self, event):
        text = event.message.text
        return text.lower() == "2"
    def is_going_to_Ltn_choose_politics(self, event):
        text = event.message.text
        return text.lower() == "1"
    def is_going_to_Ltn_choose_world(self, event):
        text = event.message.text
        return text.lower() == "3"
    def is_going_to_Ltn_choose_sport(self, event):
        text = event.message.text
        return text.lower() == "4"
    def is_going_back_to_Ltn_choose_category(self, event):
        text = event.message.text
        return text.lower() == "1"


    #initial page
    def on_enter_news_initial(self, event):
        print("I'm entering news_initial")
        return_text = "Hi~"+"\n"+"今天想看什麼新聞呢?"+"\n"+"選擇一家媒體:"+"\n"+"1.TVBS"+"\n"+"2.中央社"+"\n"+"3.蘋果日報"+"\n"+"4.自由時報"
        reply_token = event.reply_token

        send_text_message(reply_token, return_text)

    #choose media
    def on_enter_TVBS_choose_category(self, event):
        print("I'm entering TVBS_choose_category")
        return_text = ">_<" + "\n" + "你選擇了TVBS" + "\n" + "選擇要看的分類:" + "\n" + "1.政治 " + "\n" + "2.社會" + "\n" + "3.國際" + "\n" + "4.體育"+ "\n" + "5.返回"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_Apple_choose_category(self, event):
        print("I'm entering TVBS_choose_category")
        return_text = ">_<" + "\n" + "你選擇了蘋果日報" + "\n" + "選擇要看的分類:" + "\n" + "1.政治 " + "\n" + "2.社會" + "\n" + "3.國際" + "\n" + "4.體育"+ "\n" + "5.返回"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    def on_enter_Ltn_choose_category(self, event):
        print("I'm entering TVBS_choose_category")
        return_text = ">_<" + "\n" + "你選擇了自由時報" + "\n" + "選擇要看的分類:" + "\n" + "1.政治 " + "\n" + "2.社會" + "\n" + "3.國際" + "\n" + "4.體育"+ "\n" + "5.返回"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    def on_enter_CNA_choose_category(self, event):
        print("I'm entering CNA_choose_category")
        return_text = ">_<" + "\n" + "你選擇了中央社" + "\n" + "選擇要看的分類:" + "\n" + "1.政治 " + "\n" + "2.社會" + "\n" + "3.國際" + "\n" + "4.體育"+ "\n" + "5.返回"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    #TVBS-----------------------------------------------------------------------------------------------------------------------------
    def on_enter_TVBS_choose_social(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.tvbs.com.tw/local"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_TVBS_choose_politics(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.tvbs.com.tw/politics"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_TVBS_choose_sport(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.tvbs.com.tw/sports"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text += r + "\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    def on_enter_TVBS_choose_world(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.tvbs.com.tw/world"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    #CNA------------------------------------------------------------------------------------
    def on_enter_CNA_choose_social(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://www.cna.com.tw/news/asoc"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_CNA_choose_politics(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://www.cna.com.tw/news/aipl"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_CNA_choose_sport(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://www.cna.com.tw/news/aspt"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text += r + "\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    def on_enter_CNA_choose_world(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://www.cna.com.tw/news/aopl"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    #Apple--------------------------------------------------------------------------------------------------------------
    def on_enter_Apple_choose_social(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://tw.appledaily.com/local"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_Apple_choose_politics(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://tw.appledaily.com/politics"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_Apple_choose_sport(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://tw.appledaily.com/sports"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text += r + "\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    def on_enter_Apple_choose_world(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://tw.appledaily.com/international"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    #Ltn-------------------------------------------------------------------------------------------------
    def on_enter_Ltn_choose_social(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.ltn.com.tw/news/society"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_Ltn_choose_politics(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.ltn.com.tw/news/politics"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)

    def on_enter_Ltn_choose_sport(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://sports.ltn.com.tw/"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text += r + "\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)
    def on_enter_Ltn_choose_world(self, event):
        print("I'm entering CNA_choose_category")
        url = "https://www.google.com/search?q=site:https://news.ltn.com.tw/news/world"
        html_lst = []
        response = rq.get(url=url)
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        new_lst = soup.find_all(class_='kCrYT')
        return_text = "輸入1返回\n\n新聞列表:\n"
        for e in new_lst:
            if e.select_one('a') != None:
                html_lst.append(e.select_one('a').get('href'))
        for e in html_lst:
            e = str(e).replace("/url?q=", "")
            r = str(e)
            r = r[0:r.find("&sa", 0)]
            return_text +=r +"\n"
        reply_token = event.reply_token
        send_text_message(reply_token, return_text)