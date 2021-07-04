import json


def main():
    indexes = [3, 2, 1]
    score = [1, 2, 3]
    result = (indexes, score)
    results = [result]
    results_dict = dict()
    results_dict['titles'] = results
    print(results_dict)
    print(json.dumps(results_dict, ensure_ascii=False, indent=2))
    with open('mydata.json', mode='wt', encoding='utf-8') as file:
        json.dump(results_dict, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
