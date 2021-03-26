import requests

def main():

    text='こんにちは'
    source='ja'
    target='en'

    res = requests.get('https://script.google.com/macros/s/AKfycbwNkQeRuKNDhQZTsYiGK5JIgQSbNOVMMUaekGWbx2NwVxzGFVCUtEdsCG33FU_qKc1B/exec?text=' + text + '&source=' + source + '&target=' + target)

    print(res.text)

if __name__ == '__main__':
    main()
