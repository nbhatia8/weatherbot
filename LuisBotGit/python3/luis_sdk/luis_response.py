
import json
from .luis_intent import LUISIntent
from .luis_entity import LUISEntity
from .luis_composite_entity import LUISCompositeEntity
from .luis_dialog import LUISDialog

class LUISResponse:
    '''
    LUIS Response Class.
    Describes the response structure, and is the main point
    to access the response sent by LUIS after prediction.
    '''

    def __init__(self, JSONResponse):
        '''
        A constructor for the LUISResponse class.
        :param JSONResponse: A string containing the incoming JSON.
        '''
        if JSONResponse is None:
            raise TypeError('NULL JSON response')
        if not JSONResponse:
            raise ValueError('Invalid App Id')

        if isinstance(JSONResponse, str):
            try:
                response = json.loads(JSONResponse)
            except Exception:
                raise Exception('Error in parsing json')
        else:
            response = JSONResponse

        if 'statusCode' in response:
            raise Exception(u'Invalid Subscription Key')

        self._query = response['query']

        if 'dialog' in response:
            self._dialog = LUISDialog(response['dialog'])
        else:
            self._dialog = None

        self._intents = []
        self._entities = []
        self._composite_entities = []

        self._top_scoring_intent = LUISIntent(response['topScoringIntent'])
        
        if 'intents' in response:
            for intent in response['intents']:
                self._intents.append(LUISIntent(intent))
        else:
            self._intents.append(self._top_scoring_intent)
        
        for entity in response['entities']:
            self._entities.append(LUISEntity(entity))

        if 'compositeEntities' in response:
            for composite_entity in response['compositeEntities']:
                self._composite_entities.append(LUISCompositeEntity(composite_entity))

    def get_query(self):
        '''
        A getter for the response's query.
        :return: Response's query.
        '''
        return self._query

    def get_top_intent(self):
        '''
        A getter for the response's top scoring intent.
        :return: Response's top scoring intent.
        '''
        return self._top_scoring_intent

    def get_intents(self):
        '''
        A getter for the response's intents.
        :return: A list of intents.
        '''
        return self._intents

    def get_entities(self):
        '''
        A getter for the response's entities.
        :return: A list of entities.
        '''
        return self._entities

    def get_composite_entities(self):
        '''
        A getter for the response's composite entities.
        :return: A list of composite entities.
        '''
        return self._composite_entities

    def get_dialog(self):
        '''
        A getter for the response's dialog.
        :return: Response's dialog.
        '''
        return self._dialog
