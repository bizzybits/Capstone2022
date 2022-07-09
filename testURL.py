import pprint as pp
import urllib.request, json

def getQuestions(qty,cate,diffi):
    baseUrl = f"https://opentdb.com/api.php?amount={qty}"
    specificUrl = f"https://opentdb.com/api.php?amount={qty}&category={cate}&difficulty={diffi}"
    shortUrl = f"https://opentdb.com/api.php?amount={qty}&difficulty={diffi}"
    with urllib.request.urlopen(specificUrl) as url:
        data = json.loads(url.read().decode())
        print(data)
    return data


def main():
    result = getQuestions(10, 13, "medium")
    #print(result)
    print("###################################")
    #print(result['results'])
    #print(type(result['results']))
    for each in result['results']:
        #print(each)
        category = each['category']
        print(f"Category: {category}")
        typeQ = each['type']
        print(f"Question Type: {typeQ}")
        question = each['question']
        print(f"Question: {question}")
        answerCorrect = each['correct_answer']
        print(f"Correct Answer: {answerCorrect}")
        answersWrong = each['incorrect_answers']
        print(f"Wrong Answers: {answersWrong}")
        print("%%%%%%%%%%%")

main()