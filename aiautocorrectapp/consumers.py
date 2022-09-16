import json
from channels.generic.websocket import WebsocketConsumer
from . import models

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data):

        data_dict = json.loads(text_data)

        if data_dict["type"] == "new_record":

            misspelled_word_text = data_dict["before"]
            accurate_word_text = data_dict["after"]

            if misspelled_word_text.isalpha() and accurate_word_text.isalpha():

                misspelled_word, created1 = models.Word.objects.get_or_create(content = misspelled_word_text)
                accurate_word, created2 = models.Word.objects.get_or_create(content = accurate_word_text)


                relation, relation_created = models.WordRelation.objects.get_or_create(misspelled = misspelled_word, accurate = accurate_word)
                
                if not relation_created:
                    relation.count += 1
                    relation.save()
    
        elif data_dict["type"] == "get_accurates" and data_dict["word"].isalpha():
            word,word_created = models.Word.objects.get_or_create(content = data_dict["word"])
            filtered_rels = models.WordRelation.objects.filter(misspelled = word).order_by("-count")[:3]

            accurates_dict = {}

            for i in range(len(filtered_rels)):
                accurates_dict[f"word{i+1}"] = filtered_rels[i].accurate.content

            self.send(text_data=json.dumps(accurates_dict))
