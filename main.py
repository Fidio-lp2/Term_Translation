#!/usr/bin/python3
import requests
import json
import sys

def main():

    with open('data.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)

        text = sys.argv[1]
        source = data['status']['source']
        target = data['status']['target']

    if sys.argv[1] == 'status':
        slang = [k for k, v in data['languages'].items() if v == source][0]
        tlang = [k for k, v in data['languages'].items() if v == target][0]
        print('Term_Translation\n'+'source:'+slang+'\ntarget:'+tlang)
        
        pass

    elif sys.argv[1] == 'swap':
        tmp = source
        source = target
        target = tmp

        pass

    elif sys.argv[1] == 'set':

        if sys.argv[2] == '-s':
            source = sys.argv[3]

        elif sys.argv[2] == '-t':
            target = sys.argv[3]

        else:
            source = sys.argv[2]
            target = sys.argv[3]

        pass

    else:
        res = requests.get('https://script.google.com/macros/s/AKfycbwNkQeRuKNDhQZTsYiGK5JIgQSbNOVMMUaekGWbx2NwVxzGFVCUtEdsCG33FU_qKc1B/exec?text='+text+'&source='+source+'&target='+target)

        print(res.text)

        pass

def reinsert(data, source, target):
    data['status']['source'] = source
    data['status']['target'] = target


if __name__ == '__main__':
    main()
