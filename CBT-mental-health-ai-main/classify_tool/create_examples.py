import cohere
import csv
example_arr = []
with open('Examples.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        example_arr.append({"text":row["Text"],"label":row["Label"]})
    print("Generation done")
    print(example_arr)



COHERE_API_KEY = "Aa3yKEwtz0wRbRRuPTZ6VvPqXrS9Nvgn9uh6cawn"
co = cohere.Client(COHERE_API_KEY)



response = co.classify(
  model='large',
  inputs=["sentance"],
  examples=[{"sentance","sucks"}])
print('The confidence levels of the labels are: {}'.format(response.classifications))