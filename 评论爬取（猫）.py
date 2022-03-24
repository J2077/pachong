# 作者：福尔摩豪
# 日期：2022年03月14日
import csv
import json
def response(flow):
    if'/api/sns/v5/note/comment/list' in flow.request.url:
        js_data = json.loads(flow.response.text)['data']['comments']
        for comment in js_data:
            content=comment['content']
            content = content.replace('\n', ' ')
            jsu_data = comment['user']
            nickname = jsu_data['nickname']
            print(nickname,content)
            with open('猫.txt', 'a', encoding='utf-8') as f:
                f.write(f'{nickname}\t{content}\n')  #TXT格式
