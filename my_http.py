import requests
import re
import json

def request_get(url):
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        })
        print(response.content)
    except:
        print('fail to request')


def request_post(url, body):
    try:
        response = requests.get(url, body, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        })
        print(response.content)
    except:
        print('fail to request')


url_sendMessage = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/sendMessage'

url_getUpdates = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/getUpdates'

url_getChatMember = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/getChatMember'

url_getChatMembersCount = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/getChatMembersCount'

url_getChat = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/getChat'

url_getUserProfilePhotos = "https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/getUserProfilePhotos"

url_getMe = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/getMe'

url_sendChatAction = 'https://api.telegram.org/bot335016706:AAHmUz5E0-HuohsyKE8fyTmcvE3RkNYflLI/sendChatAction'

id1 = "{\"id\":\"pid.1493006551957:588433365848122\",\"data\":\"{\\\"intent\\\":\\\"qry-transactionhistory\\\",\\\"data\\\":{\\\"acctId\\\":\\\"2087776992\\\"}}\"\"}"

body = {'chat_id':'357108441', 'text':'AXIS CASH BACK VISA - xxxx xxxxxx7308', "reply_markup" : {
    "inline_keyboard" : [ [ {
      "text" : "Latest Transactions",
      "callback_data" : json.dumps(id1)
    }
    # ,
    # {
    #   "text" : "Pay Mimimum Amount",
    #   "callback_data" : "pid.1493006551957:991285022486732"
    # },
    # {
    #   "text" : "Pay Outstanding Amount",
    #   "callback_data" : "pid.1493006551957:322349160118556"
    # }
    ] ]
  }}

body1 = {  
   "chat_id":"357108441",
   "user_id":357108441
}

body2 = {  
   "chat_id":"357108441"
}

body3 = {  
   "chat_id":"357108441",
   "action":"typing"
}

# request_get(url_getUpdates)

# request_post(url_sendMessage, body)

# request_post(url_getChatMember, body1)

# request_post(url_getChatMembersCount, body2)

# request_post(url_getUserProfilePhotos, body1)

# request_post(url_getChat, body2)

# request_get(url_getMe)

request_post(url_sendChatAction, body3)