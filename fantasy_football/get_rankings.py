import csv
import json


def main():
    with open('/Users/avarmaraja/Downloads/predraft.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        output = list()
        for row in reader:
            # if row['POS'] in ['WR', 'RB', 'TE']:
            if True:
                if row['T'] != '#N/A':
                    output.append((row['\xef\xbb\xbfNAME'], row['T'], row['VAL'], row['PS']))
        output = sorted(output, key=lambda x:float(x[2]), reverse = True)
        output = sorted(output, key=lambda x:int(x[1]))
        output=output[60:]
        print(output)
        file = open('dump.json', 'w')
        json.dump(output, file, indent=4)



if __name__ == '__main__':
    main()
