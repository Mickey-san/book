import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict

def get_grouped_numbers():
    url = "https://tatuo.net/numbers/numbers3/yosou/ysou.php"
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    numbers = []
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        for i, td in enumerate(tds):
            if '次回の' in td.get_text():
                if i + 1 < len(tds):
                    ktup_td = tds[i + 1]
                    text = ktup_td.get_text()
                    numbers = re.findall(r'\b\d{3}\b', text)
                    break
        if numbers:
            break

    grouped = defaultdict(list)
    for num in numbers:
        key = ''.join(sorted(num))
        grouped[key].append(num)

    message_lines = []
    for key, group in grouped.items():
        if len(group) >= 3:
            message_lines.append(f"{key}: {', '.join(group)}")

    if message_lines:
        return "3通り以上ある数字グループ:\n\n" + "\n".join(message_lines)
    else:
        return "該当する数字の組み合わせは見つかりませんでした。"
 # type: ignore