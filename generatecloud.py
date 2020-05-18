import csv

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

def main():
    tags = []
    # List all files in a directory using os.listdir
    basepath = 'fetch/output/'
    for entry in os.listdir(basepath):
        dir = os.path.join(basepath, entry)
        if entry != ".DS_Store":
            #print(dir)
            if os.path.isfile(dir):
                data = open(dir, 'rb').read()
                # print(data.find('\x00'))
                #print(data)
                with open(dir, encoding="utf8", errors='ignore') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    cat_pos = 5
                    tag_pos = 7

                    for row in csv_reader:
                        if line_count != 0:
                            # Debugging line: print(f'\t{row[0]} - {row[cat_pos]} - {row[tag_pos]}.')
                            #unicode(str, errors='ignore')
                            tags.extend([x for x in row[tag_pos].split("|") if x != "[none]"])
                        line_count += 1

    text = ",".join(tags)
    print("Generating... Please wait a moment...")
    wordcloud = WordCloud(background_color="white", max_words= 300, height=1440, width=2560).generate(text)
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()
    wordcloud.to_file(os.path.join("fetch/", "cloud.png"))
    print("Generation complete!")

if __name__ == "__main__":
    main()
