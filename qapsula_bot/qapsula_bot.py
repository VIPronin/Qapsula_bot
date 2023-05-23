import vk_api
from vk_api.utils import get_random_id
import configparser
import time
import datetime

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    login = config['auth']['login']
    password = config['auth']['password']
    group = config['destination']['group']
    topic = config['destination']['topic']

    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()

    while True:
        now = datetime.datetime.fromtimestamp(vk.utils.getServerTime())
        # необходимо указать время в формате: часы, минуты, секунды
        if now.hour == 16 and now.minute == 45 and now.second == 1:
            for name in config['registration']['names_list'].split('\n'):
                random_id = get_random_id()
                try:
                    vk.board.createComment(group_id=group, topic_id=topic,
                                           message=name, guid=random_id)
                except Exception as error:
                    with open('errors.txt', 'a') as file:
                        file.write(group + '\n' + str(error) + '\n')
                finally:
                    time.sleep(1/3)
        else:
            time.sleep(1)
