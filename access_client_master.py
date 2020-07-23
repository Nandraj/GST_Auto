import xlrd


def parse_client_excel_file_and_return_dict(excel_file):
    # opening & accessing client data from excel file
    book = xlrd.open_workbook(excel_file)  # , ragged_rows=True)
    sheet = book.sheet_by_index(0)
    num_rows = sheet.nrows

    col_head = [cell for cell in sheet.row_values(1)]

    client_dict = {}

    for n in range(2, num_rows):
        row_values_list = [cell for cell in sheet.row_values(n)]
        client_dict[row_values_list[1]] = {}
        for i in col_head[2:]:
            client_dict[row_values_list[1]
                        ][i] = row_values_list[col_head.index(i)]

    return client_dict


def generate_data_for_clientName_drop_down(search, client_dict):
    client_name_list = []
    if search == "":
        for k in client_dict.keys():
            client_name_list.append(k)
    else:
        for k in client_dict.keys():
            if search.lower() in k.lower():
                client_name_list.append(k)

    # sort client dict A-Z
    client_name_list.sort()
    return client_name_list

#client_name_list = generate_data_for_clientName_drop_down("jewel")
# print(client_name_list)
