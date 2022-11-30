import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"

def csv_to_list_dict(INPUT_FILE,  delimeter=",", new_line="\n") -> list[dict]:
    list_dict = []
    with open(INPUT_FILE, encoding="utf-8") as input_csv:
        input_csv.readlines()
        for row in enumerate(input_csv):
            row_list = [delimeter.join(row) + new_line]
            header = row_list[0]
            for header, value in row_list[1:]:
                csv_data = {header[element]: value[element] for element in range(len(row_list))}
                list_dict.append(csv_data)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as output_json:
        output_json.write(json.dumps(list_dict))

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
