from langdetect import detect, DetectorFactory
import pycountry
import json
DetectorFactory.seed = 0


def detect_all_language(file_title):
    filename = file_title+".txt"

    file = open(filename, encoding="utf8")
    line_list =[]
    different_lang_detect = []


    for line in file:
        if line != '\n' and len(line.split()) > 1:    #does not add blank lines and len of line is greater than 1 line of word
            line_list.append(line)

    file.close()
    # print(line_list)

    for txt in line_list:
        lang = detect(txt)
        lang_type = pycountry.languages.get(alpha_2=lang).alpha_3.lower()
        if lang_type not in different_lang_detect:
            different_lang_detect.append(lang_type)


    dictionaryMap = {
        "File": filename,
        "language": different_lang_detect
    }

    json_obj = json.dumps(dictionaryMap, indent=4)

    with open("sampleJson.json", "w") as outputFile:
        outputFile.write(json_obj)
    return json_obj



detect_all_language('SampleText')












