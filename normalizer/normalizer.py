from rasa_nlu.components import Component
from rasa_nlu import utils

import os
import re

NORMALIZER_MODEL_FILE_NAME = "rb_normalizer.pkl"

class RuleBasedNormalizer(Component):

    name = "rule_based_normalizer"
    provides = ["tokens"]
    def __init__(self, component_config = None):
        super(RuleBasedNormalizer, self).__init__(component_config)

    def train(self, training_data, config, **kwargs):
        pass
    
    def process(self, message, **kwargs):

        is_to_lower = self.component_config['isToLower']
        if is_to_lower:
            message.text = message.text.lower()

        replace_from = self.component_config['replace']['from']
        replace_to = self.component_config['replace']['to']
        
        for r_f in replace_from:
            for r_t in replace_to:
                message.text = re.sub(r'\s{0}\s'.format(r_f), ' %s ' % r_t,message.text)
                message.text = re.sub(r'^{0}\s'.format(r_f), ' %s ' % r_t, message.text)
                # message.text = re.sub(r'$\s{0}'.format(r_f), ' %s ' % r_t, message.text)
        # replace whitespace
        message.text = message.text.strip()

        
    def persist(self, model_dir):
        pass 
    


    


