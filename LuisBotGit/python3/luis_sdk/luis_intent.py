

from .luis_action import LUISAction

class LUISIntent:
    '''
    LUIS Intent Class.
    Describes the LUIS Intent structure.
    '''

    def __init__(self, intent):
        '''
        LUIS Intent Class.
        Describes the LUIS Intent structure.
        '''
        self._name = intent['intent']
        self._score = intent['score']
        self._actions = []

        if 'actions' in intent:
            for action in intent['actions']:
                self._actions.append(LUISAction(action))


    def get_name(self):
        '''
        A getter for the intent's name.
        :return: Intent's name.
        '''
        return self._name

    def get_score(self):
        '''
        A getter for the intent's score.
        :return: Intent's score.
        '''
        return self._score

    def get_actions(self):
        '''
        A getter for the entity's actions.
        :return: A list of actions.
        '''
        return self._actions
