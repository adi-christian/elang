from elang.word2vec.builder import build_from_wikipedia
model1 = build_from_wikipedia(n=3, lang="id")
model2 = build_from_wikipedia(slug="Koronavirus", lang="id", levels=2)
print(model1)