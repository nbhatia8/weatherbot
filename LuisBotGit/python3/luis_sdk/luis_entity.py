

class LUISEntity:
    '''
    LUIS Entity Class.
    Describes the LUIS Entity structure.
    '''

    def __init__(self, entity):
        '''
        A constructor for the LUISEntity class.
        :param entity: A dictionary containing the entity data.
        '''
        self._name = entity['entity']
        self._type = entity['type']
        if 'startIndex' in entity:
            self._start_idx = entity['startIndex']
        else:
            self._start_idx = None
        if 'endIndex' in entity:
            self._end_idx = entity['endIndex']
        else:
            self._end_idx = None
        if 'score' in entity:
            self._score = entity['score']
        else:
            self._score = None
        if 'resolution' in entity:
            self._resolution = entity['resolution']
        else:
            self._resolution = None

    def get_name(self):
        '''
        A getter for the entity's name.
        :return: Entity's name.
        '''
        return self._name

    def get_type(self):
        '''
        A getter for the entity's type.
        :return: Entity's type.
        '''
        return self._type

    def get_start_idx(self):
        '''
        A getter for the entity's start index.
        :return: Entity's start index.
        '''
        return self._start_idx

    def get_end_idx(self):
        '''
        A getter for the entity's end index.
        :return: Entity's end index.
        '''
        return self._end_idx

    def get_score(self):
        '''
        A getter for the entity's score.
        :return: Entity's score.
        '''
        return self._score

    def get_resolution(self):
        '''
        A getter for the entity's resolution.
        :return: Entity's resolution.
        '''
        return self._resolution
