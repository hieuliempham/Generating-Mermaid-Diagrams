import pandas as pd
import tabula
import graphviz
import sys
import random
import math

def read_data(file_path):
    if file_path.endswith('.xlsx'):
        # Read Excel file
        df = pd.read_excel(file_path)
    elif file_path.endswith('.pdf'):
        # # Extract data from PDF file
        # Read PDF file using Tabula
        df = tabula.read_pdf(file_path, pages='all', encoding='cp1258')[0]
    else:
        raise ValueError("Invalid file format. Only Excel (.xlsx) and PDF (.pdf) files are supported.")
    
    return df

def generate_mermaid_diagram(data):
    # Get coloumn name
    print(data.columns)

    diagram = 'graph TD\n'
    num_rows = 12  # Set the desired number of rows (12 in this case)
    num_columns = 12  # Set the desired number of columns (12 in this case)
    node_width = 100  # Adjust the node width as needed
    node_height = 100  # Adjust the node height as needed
    row_spacing = 50  # Adjust the row spacing as needed
    column_spacing = 50  # Adjust the column spacing as needed

    color_map = {}

    for index, row in data.iterrows():
        source = row[0]
        target = row[1]
        songHanh = row[2]

        #  Tien Quyet
        if pd.notnull(source) and pd.notnull(target):
            source_color = get_node_color(source, color_map)
            target_color = get_node_color(target, color_map)
           
            row_index = index // num_columns
            col_index = index % num_columns
            source_x = col_index * (node_width + column_spacing)
            source_y = row_index * (node_height + row_spacing)
            target_x = source_x
            target_y = source_y + node_height

            diagram += f'    {source}(({source})) -->|Tien Quyet| {target}(({target}))\n'
            diagram += f'    style {source} fill:{source_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    style {target} fill:{target_color},stroke:#333,stroke-width:4px\n'     
            diagram += f'    classDef {source}Class fill:{source_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    class {source} {source}Class\n'
            diagram += f'    classDef {target}Class fill:{target_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    class {target} {target}Class\n'
            

        # Song Hanh
        elif  pd.notnull(target) and pd.notnull(songHanh):
            target_color = get_node_color(target, color_map)
            songHanh_color = get_node_color(songHanh, color_map)
           
            row_index = index // num_columns
            col_index = index % num_columns
            source_x = col_index * (node_width + column_spacing)
            source_y = row_index * (node_height + row_spacing)
            target_x = source_x
            target_y = source_y + node_height
  
            diagram += f'    {songHanh}(({songHanh})) -->|Song Hanh| {target}(({target}))\n'
            diagram += f'    style {target} fill:{target_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    style {songHanh} fill:{songHanh_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    classDef {target}Class fill:{target_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    class {target} {target}Class\n'
            diagram += f'    classDef {songHanh}Class fill:{songHanh_color},stroke:#333,stroke-width:4px\n'
            diagram += f'    class {songHanh} {songHanh}Class\n'

        # In ra học phần nếu nó không có học phần tiên quyết
        # elif pd.notnull(target):
        #     target_color = get_node_color(target, color_map)
        #     row_index = index // num_columns
        #     col_index = index % num_columns
        #     target_x = col_index * (node_width + column_spacing)
        #     target_y = row_index * (node_height + row_spacing)
        #     diagram += f'    {target}(({target}))\n'
        #     diagram += f'    style {target} fill:{target_color},stroke:#333,stroke-width:4px\n'
        #     diagram += f'    classDef {target}Class fill:{target_color},stroke:#333,stroke-width:4px\n'
        #     diagram += f'    class {target} {target}Class\n'
        else:
            continue

    return diagram


def get_node_color(node_name, color_map):
    if not node_name:
        return ''

    if "(" in node_name and ")" in node_name:
        return node_name[node_name.index("(") + 1: -1]

    prefix = node_name[:3]

    if prefix in color_map:
        return color_map[prefix]

    # Generate random color
    color = f'#{"".join([random.choice("0123456789ABCDEF") for _ in range(6)])}'

    color_map[prefix] = color

    return color


def main():
    if len(sys.argv) != 2:
        print("Usage: python mermaid_app.py <file_path>")
        return
    
    file_path = sys.argv[1]
    
    try:
        if file_path.endswith('.xlsx'):
            data = read_data(file_path)
            # Get coloumn name
            print(data.columns)
            data = data[["Mã HP\nhọc trước", "Mã HP", "Mã HP\nsong hành"]]  # Extract the desired columns
        elif file_path.endswith('.pdf'):
            data = read_data(file_path)
            data = data[["Mă HP.1", "Mă HP"]]  # Extract the desired columns
        else:
            raise ValueError("Invalid file format. Only Excel (.xlsx) and PDF (.pdf) files are supported.")

        diagram = generate_mermaid_diagram(data)
        print(diagram)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()