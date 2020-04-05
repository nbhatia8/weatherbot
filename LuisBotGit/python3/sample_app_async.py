
from luis_sdk import LUISClient

def on_success(res):

    print('---------------------------------------------')
    print('LUIS Response: ')
    print('Query: ' + res.get_query())
    print('Top Scoring Intent: ' + res.get_top_intent().get_name())
    if res.get_dialog() is not None:
        if res.get_dialog().get_prompt() is None:
            print('Dialog Prompt: None')
        else:
            print('Dialog Prompt: ' + res.get_dialog().get_prompt())
        if res.get_dialog().get_parameter_name() is None:
            print('Dialog Parameter: None')
        else:
            print('Dialog Parameter Name: ' + res.get_dialog().get_parameter_name())
        print('Dialog Status: ' + res.get_dialog().get_status())
    print('Entities:')
    for entity in res.get_entities():
        print('"%s":' % entity.get_name())
        print('Type: %s, Score: %s' % (entity.get_type(), entity.get_score()))

def on_failure(err):

    print(err)

try:
    APPID = input('Please enter your app Id:\n')
    APPKEY = input('Please input your subscription key:\n')
    TEXT = input('Please input the text to predict:\n')
    CLIENT = LUISClient(APPID, APPKEY, True)
    CLIENT.predict(TEXT, {'on_success': on_success, 'on_failure': on_failure})
    print('-------\nMain thread finishing!!\n-------')
except Exception as exc:
    print(exc)
