from allennlp import pretrained
import spacy
model = pretrained.neural_coreference_resolution_lee_2017()
results = model.predict(document="Miles is happy. He told me the other day to be quiet.")
print(results)
# import spacy
# import neuralcoref
# nlp = spacy.load('en_core_web_sm')
# neuralcoref.add_to_pipe(nlp)
# doc = nlp(u'My sister has a dog. She loves him.')