import requests

from root import settings


def send_order_notification(full_name, company_name, email):
    token = "7464172711:AAFORUqXKxBTPp-3yKwke5ICyoram2NhKNI"
    chat_id = "-1002195748552"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    msg = f"""
Full name: {full_name}\n
Company name: {company_name}\n
Email: {email}    
    """
    payload = {
        'chat_id': chat_id,
        'text': f"<b>{msg}</b>",
        'parse_mode': 'HTML'
    }

    response = requests.post(url, data=payload)
    return response.json()
