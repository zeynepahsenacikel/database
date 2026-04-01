from sys import argv

def CREATE_TABLE(table_name, columns): #creates new table
    try:
        for a in table:
            if a["name"]==table_name:
                raise ValueError("Table already exists") #if table already exists raise an error
    except ValueError:
        print("Table already exists")
    else:
        column_list=[col.strip() for col in columns.split(',')]
        table1 = {
            "name":table_name,
            "columns":column_list,
            "data":[]
        }
        table.append(table1)
    print("###################### CREATE #########################")
    print(f"Table '{table_name}' created with columns: {columns.split(',')}")
    print("#######################################################")

def INSERT(table_name, data): #inserts data into table
    print("###################### INSERT #########################")
    table2=None
    try: # if table exists assign it to table2, if not print table does not exist
        for a in table:
            if a["name"]==table_name:
                table2 = a
                break
        if not table2:
                raise ValueError(f"Table {table_name} not found") #if table does not exist raise an error
    except ValueError:
        print(f"Table {table_name} not found")
        print(f"Inserted into '{table_name}': {tuple(data.split(','))}")
        print("#######################################################")
        return
    print(f"Inserted into '{table_name}': {tuple(data.split(','))}")

    try:
        e=data.count(',')
        e=e+1
        if e !=len(table2["columns"]):
            raise ValueError("Columns don't match") #if given columns' number doesn't match with table raise error
    except ValueError:
        print("Columns don't match")
        print("#######################################################")
        return

    data1={}
    x=[i.strip() for i in data.split(',')]
    for i in range(len(table2["columns"])):
        data1[table2["columns"][i]]=x[i]
    table2["data"].append(data1)

    print(f"\nTable: {table_name}") # calculate lengths for each column and prints table
    column_lengths=[]
    for s in table2["columns"]:
        max_len=len(s)
        for r in table2["data"]:
            cell=len(str(r[s]))
            if cell>max_len:
                max_len=cell
        column_lengths.append(max_len)
    print("+" ,end='')
    for h in range(len(table2["columns"])):
        print("-"* (column_lengths[h]+2),end='+')
    print()
    print("|" ,end='')
    for h in range(len(table2["columns"])):
        z= table2["columns"][h]
        space_num= " " * (column_lengths[h] - len(z))
        print(f" {z}{space_num} |", end='')
    print()
    print("+", end='')
    for h in range(len(table2["columns"])):
        print("-" * (column_lengths[h] + 2), end='+')
    print()
    for r in table2["data"]:
        print("|" ,end='')
        for k in range(len(table2["columns"])):
            v=str(r[table2["columns"][k]])
            space_num2= " " * (column_lengths[k] - len(v))
            print(f" {v}{space_num2} |", end='')
        print()
    print("+", end='')
    for h in range(len(table2["columns"])):
        print("-" * (column_lengths[h] + 2), end='+')
    print()
    print("#######################################################")

def SELECT(table_name, columns, conditions): #select data according to given conditions
    table2 = None # if table exists assign it to table2, if not print table does not exist
    for a in table:
        if a["name"] == table_name:
            table2 = a
            break
    if table2 is None: #ıf table does not exist print it
        print("###################### SELECT #########################")
        print(f"Table {table_name} not found")
        print(f"Condition: {conditions}")
        print(f"Select result from '{table_name}': None")
        print("#######################################################")
        return

    try:
        if columns== '*': #if * select all data
            columns1=table2["columns"]
        else:
            columns1=[c.strip() for c in columns.split(',')]
            for c in columns1:
                if c not in table2["columns"]:
                    raise ValueError(f"Column {c} does not exists")
    except ValueError: #ıf given column does not exist raise error
        print("###################### SELECT #########################")
        print(f"Column {c} does not exist")
        print(f"Condition: {conditions}")
        print(f"Select result from '{table_name}': None")
        print("#######################################################")
        return

    list1=[] #specify keys and values
    conditions=conditions.strip().strip('{}')
    condition1= conditions.split(',')
    condition_dictionary={}
    for i in condition1:
        key, value=i.split(':')
        key=key.strip().strip('"')
        value=value.strip().strip('"')
        condition_dictionary[key]=value

    try:
        for key in condition_dictionary: #if column does not exist raise error
            if key not in table2["columns"]:
                raise ValueError(f"Column {key} does not exist")
    except ValueError:
        print("###################### SELECT #########################")
        print(f"Column {key} does not exist")
        print(f"Condition: {condition_dictionary}")
        print(f"Select result from '{table_name}': None")
        print("#######################################################")
        return

    for k in table2["data"]:
        controller=True
        for x in range(len(condition_dictionary)):
            key=list(condition_dictionary.keys())[x]
            value=list(condition_dictionary.values())[x]
            if key not in k or str(k[key]) != str(value):
                controller=False
                break
        if controller:
            filtered=[] #selected data
            for d in columns1:
                if d in k:
                    filtered.append(k[d])
            filtered = tuple(filtered)
            list1.append(filtered)
    print("###################### SELECT #########################") #print output
    if list1:
        print(f"Condition: {condition_dictionary}")
        print(f"Select result from '{table_name}': {list1}")
    else:
        print(f"Condition: {condition_dictionary}")
        print(f"Select result from '{table_name}': None")
    print("#######################################################")

def UPDATE(table_name, updates, conditions): #updates data according to given input
    table2 = None
    try:
        for a in table:
            if a["name"] == table_name:
                table2 = a
                break
        if not table2:
            raise ValueError(f"Table {table_name} not found")
    except ValueError:
        updates = updates.strip().strip('{}')
        update1 = updates.split(',')
        update_dictionary = {}
        for i in update1:
            key, value = i.split(':')
            key = key.strip().strip('"')
            value = value.strip().strip('"')
            update_dictionary[key] = value

        conditions = conditions.strip().strip('{}')
        condition1 = conditions.split(',')
        condition_dictionary = {}
        for n in condition1:
            key, value = n.split(':')
            key = key.strip().strip('"')
            value = value.strip().strip('"')
            condition_dictionary[key] = value

        print("###################### UPDATE #########################") #if table does not exist print it
        print(f"Updated '{table_name}' with {update_dictionary} where {condition_dictionary}")
        print(f"Table {table_name} not found")
        print(" 0 rows updated.")
        print("#######################################################")
        return

    updates= updates.strip().strip('{}')
    update1=updates.split(',')
    update_dictionary={}
    for i in update1:
        key, value=i.split(':')
        key=key.strip().strip('"')
        value=value.strip().strip('"')
        update_dictionary[key]=value

    conditions= conditions.strip().strip('{}')
    condition1=conditions.split(',')
    condition_dictionary={}
    for n in condition1:
        key, value=n.split(':')
        key=key.strip().strip('"')
        value=value.strip().strip('"')
        condition_dictionary[key]=value

    for key in condition_dictionary: #print updated table
        if key not in table2["columns"]:
            print("###################### UPDATE #########################")
            print(f"Updated '{table_name}' with {update_dictionary} where {condition_dictionary}")
            print(f"Column {key} does not exist")
            print("0 rows updated.")
            print(f"\n Table: {table_name}")
            column_lengths = [] # calculate lengths for each column and prints table
            for s in table2["columns"]:
                max_len = len(s)
                for r in table2["data"]:
                    cell = len(str(r[s]))
                    if cell > max_len:
                        max_len = cell
                column_lengths.append(max_len)
            print("+", end='')
            for h in range(len(table2["columns"])):
                print("-" * (column_lengths[h] + 2), end='+')
            print()
            print("|", end='')
            for h in range(len(table2["columns"])):
                z = table2["columns"][h]
                space_num = " " * (column_lengths[h] - len(z))
                print(f" {z}{space_num} |", end='')
            print()
            print("+", end='')
            for h in range(len(table2["columns"])):
                print("-" * (column_lengths[h] + 2), end='+')
            print()
            for r in table2["data"]:
                print("|", end='')
                for k in range(len(table2["columns"])):
                    v = str(r[table2["columns"][k]])
                    space_num2 = " " * (column_lengths[k] - len(v))
                    print(f" {v}{space_num2} |", end='')
                print()
            print("+", end='')
            for h in range(len(table2["columns"])):
                print("-" * (column_lengths[h] + 2), end='+')
            print()
            print("#######################################################")
            return

    updated_rows=0 #number of updated rows
    for d in table2["data"]:
        controller2=True
        for key in condition_dictionary:
            if key not in d or str(d[key]) != str(condition_dictionary[key]):
                controller2=False
                break
        if controller2:
            updated_rows+=1
            for key in update_dictionary:
                if key in d:
                    d[key]=update_dictionary[key]

    print("###################### UPDATE #########################") #print update's information
    print(f"Updated '{table_name}' with {update_dictionary} where {condition_dictionary}")
    print(f"{updated_rows} rows updated.")
    print(f"\nTable: {table_name}")

    column_lengths = [] # calculate lengths for each column and prints table
    for s in table2["columns"]:
        max_len = len(s)
        for r in table2["data"]:
            cell = len(str(r[s]))
            if cell > max_len:
                max_len = cell
        column_lengths.append(max_len)
    print("+", end='')
    for h in range(len(table2["columns"])):
        print("-" * (column_lengths[h] + 2), end='+')
    print()
    print("|", end='')
    for h in range(len(table2["columns"])):
        z = table2["columns"][h]
        space_num = " " * (column_lengths[h] - len(z))
        print(f" {z}{space_num} |", end='')
    print()
    print("+", end='')
    for h in range(len(table2["columns"])):
        print("-" * (column_lengths[h] + 2), end='+')
    print()
    for r in table2["data"]:
        print("|", end='')
        for k in range(len(table2["columns"])):
            v = str(r[table2["columns"][k]])
            space_num2 = " " * (column_lengths[k] - len(v))
            print(f" {v}{space_num2} |", end='')
        print()
    print("+", end='')
    for h in range(len(table2["columns"])):
        print("-" * (column_lengths[h] + 2), end='+')
    print()
    print("#######################################################")

def DELETE(table_name, conditions): #deletes data according to given input
    print("###################### DELETE #########################")
    table2 = None
    try: # if table exists assign it to table2, if not print table does not exist
        for a in table:
            if a["name"] == table_name:
                table2 = a
                break
        if not table2:
            raise ValueError(f"Table {table_name} not found")
    except ValueError:
        print(f"Deleted from '{table_name}' where {conditions}")
        print(f"Table {table_name} not found")
        print("0 rows deleted.")
        print("#######################################################")
        return

    if conditions== "*": #if condition is *, delete all data
        deleted_rows = len(table2["data"])
        table2["data"] = []
        print(f"Deleted from {table_name} where *")
        print(f"{deleted_rows} rows deleted.")
        print("#######################################################")
    else:
        condition_dictionary = conditions
        deleted_version = []
        delted_rows = 0
        for key in condition_dictionary:
            if key not in table2["columns"]:  # if condition doesn't match with columns
                print(f"Deleted from '{table_name}' where {conditions}")
                print(f"Column {key} not exist")
                print("0 rows deleted.")
                print(f"\nTable: {table_name}")
                column_lengths = []  # calculate lengths for each column and prints table
                for s in table2["columns"]:
                    max_len = len(s)
                    for r in table2["data"]:
                        cell = len(str(r[s]))
                        if cell > max_len:
                            max_len = cell
                    column_lengths.append(max_len)
                print("+", end='')
                for h in range(len(table2["columns"])):
                    print("-" * (column_lengths[h] + 2), end='+')
                print()
                print("|", end='')
                for h in range(len(table2["columns"])):
                    z = table2["columns"][h]
                    space_num = " " * (column_lengths[h] - len(z))
                    print(f" {z}{space_num} |", end='')
                print()
                print("+", end='')
                for h in range(len(table2["columns"])):
                    print("-" * (column_lengths[h] + 2), end='+')
                print()
                for r in table2["data"]:
                    print("|", end='')
                    for k in range(len(table2["columns"])):
                        v = str(r[table2["columns"][k]])
                        space_num2 = " " * (column_lengths[k] - len(v))
                        print(f" {v}{space_num2} |", end='')
                    print()
                print("+", end='')
                for h in range(len(table2["columns"])):
                    print("-" * (column_lengths[h] + 2), end='+')
                print()
                print("#######################################################")
            else:
                for d in table2["data"]:
                    controller3 = True
                    for key in condition_dictionary:
                        if key not in d or str(d[key]) != str(condition_dictionary[key]):
                            controller3 = False
                            break
                    if controller3:
                        delted_rows += 1
                    else:
                        deleted_version.append(d)
                table2["data"] = deleted_version

                print(f"Deleted from '{table_name}' where {condition_dictionary}")
                print(f"{delted_rows} rows deleted.")
                print(f"\nTable: {table_name}")
                column_lengths = []  # calculate lengths for each column and prints table
                for s in table2["columns"]:
                    max_len = len(s)
                    for r in table2["data"]:
                        cell = len(str(r[s]))
                        if cell > max_len:
                            max_len = cell
                    column_lengths.append(max_len)
                print("+", end='')
                for h in range(len(table2["columns"])):
                    print("-" * (column_lengths[h] + 2), end='+')
                print()
                print("|", end='')
                for h in range(len(table2["columns"])):
                    z = table2["columns"][h]
                    space_num = " " * (column_lengths[h] - len(z))
                    print(f" {z}{space_num} |", end='')
                print()
                print("+", end='')
                for h in range(len(table2["columns"])):
                    print("-" * (column_lengths[h] + 2), end='+')
                print()
                for r in table2["data"]:
                    print("|", end='')
                    for k in range(len(table2["columns"])):
                        v = str(r[table2["columns"][k]])
                        space_num2 = " " * (column_lengths[k] - len(v))
                        print(f" {v}{space_num2} |", end='')
                    print()
                print("+", end='')
                for h in range(len(table2["columns"])):
                    print("-" * (column_lengths[h] + 2), end='+')
                print()
                print("#######################################################")

def JOIN(table_name1, table_name2, columns):
    table1 = None
    table2 = None

    try:
        for i in table: #checks table_name1 exist or not
            if i["name"] == table_name1:
                table1 = i #if exists assign to table1
                break
        if table1 is None: #if does not exist raise error
            raise ValueError(f"Table {table_name1} does not exists")
    except ValueError:
        print("####################### JOIN ##########################")
        print(f"Join tables {table_name1} and {table_name2}")
        print(f"Table {table_name1} does not exist")
        print("#######################################################")
        return

    try:
        for i in table: #checks table_name2 exist or not
            if i["name"] == table_name2:
                table2 = i #if exists assign to table2
                break
        if table2 is None: #if does not exist raise error
            raise ValueError(f"Table {table_name2} does not exists")
    except ValueError:
        print("####################### JOIN ##########################")
        print(f"Join tables {table_name1} and {table_name2}")
        print(f"Table {table_name2} does not exist")
        print("#######################################################")
        return

    try: #checks columns exists or not
        if columns not in table1["columns"] or columns not in table2["columns"]:
            raise ValueError(f"Columns {columns} does not exist")
    except ValueError: #if does not exist print it
        print("####################### JOIN ##########################")
        print(f"Join tables {table_name1} and {table_name2}")
        print(f"Column {columns} does not exist")
        print("#######################################################")
        return

    joined_data = []
    for n in table1["data"]:
        for m in table2["data"]:
            if n[columns] == m[columns]:
                joined_ones = n.copy()
                for key, value in m.items():
                    if key != columns:
                        joined_ones[key] = value
                joined_data.append(joined_ones)

    joined_columns = table1["columns"] + [c for c in table2["columns"] if c != columns]
    joined_columns.append(columns)

    print("####################### JOIN ##########################")
    print(f"Joın tables {table1['name']} and {table2['name']}")
    print(f"Join result ({len(joined_data)} rows):")
    print("\nTable: Joined Table")

    column_lengths = [] # calculate lengths for each column and prints table
    for s in joined_columns:
        max_len = len(s)
        for r in joined_data:
            cell = len(str(r[s])) if s in r else 0
            if cell > max_len:
                max_len = cell
        column_lengths.append(max_len)
    print("+", end='')
    for h in column_lengths:
        print("-" * (h + 2), end='+')
    print()
    print("|", end='')
    for h in range(len(joined_columns)):
        c=joined_columns[h]
        length=column_lengths[h]
        print(f" {c}{' '*(length-len(c))} |", end='')
    print()
    print("+", end='')
    for h in column_lengths:
        print("-" * (h + 2), end='+')
    print()
    for r in joined_data:
        print("|", end='')
        for h in range(len(joined_columns)):
            c = joined_columns[h]
            length = column_lengths[h]
            print(f" {r[c]}{' ' * (length - len(str(r[c])))} |", end='')
        print()
    print("+", end='')
    for h in column_lengths:
        print("-" * (h + 2), end='+')
    print()
    print("#######################################################")

def COUNT(table_name, conditions): #counts data according to conditions
    print("###################### COUNT #########################")
    table2 = None
    try:
        for a in table:
            if a["name"] == table_name:
                table2 = a
                break
        if not table2:
            raise ValueError(f"Table {table_name} not found ") #ıf table does not exist raise error
    except ValueError:
        print(f"Table {table_name} not found")
        print(f"Total number of entries in '{table_name}' is 0")
        print("#######################################################")
        return

    condition_dictionary=conditions
    count=0
    for key in condition_dictionary:
        if key not in table2["columns"]: #if columns does not exist print it
            print(f"Column {key} does not exist")
            print(f"Total number of entries in '{table_name}' is 0")
            print("#######################################################")
            print()
            return


    for d in table2["data"]:
        controller4=True
        for key in condition_dictionary:
            if key not in d or str(d[key]) != str(condition_dictionary[key]):
                controller4 = False
                break
        if controller4:
            count += 1
    print(f"Count: {count}")
    print(f"Total number of entries in '{table_name}' is {count}")
    print("#######################################################")
    print()

def main(): #execute previous functions
    with open(argv[1], 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split(" ", 1)
            command = parts[0].upper()
            rest = parts[1] if len(parts) > 1 else ""

            if command == "CREATE_TABLE":
                table_name, columns = rest.split(" ", 1)
                CREATE_TABLE(table_name, columns)
                print("\n")
            elif command == "INSERT":
                table_name, data = rest.split(" ", 1)
                INSERT(table_name, data)
                print("\n")
            elif command == "SELECT":
                if " WHERE " in rest:
                    table_name, condition_str = rest.split(" WHERE ", 1)
                else:
                    table_name = rest
                    condition_str = ""
                columns = "*"
                if " " in table_name:
                    table_name, columns = table_name.split(" ", 1)
                SELECT(table_name, columns, condition_str)
                print("\n")
            elif command == "UPDATE":
                if " WHERE " in rest:
                    tablename_and_update, conditions = rest.split(" WHERE ", 1)
                    table_name, updates = tablename_and_update.split(" ", 1)
                    UPDATE(table_name, updates, conditions)
                    print("\n")
            elif command == "DELETE":
                table_name, condition_str = rest.split(" WHERE ", 1)
                conditions = eval(condition_str)
                tables = DELETE(table_name, conditions)
                print("\n")
            elif command == "JOIN":
                part, columns = rest.split(" ON ", 1)
                table1, table2 = part.split(",", 1)
                JOIN(table1, table2, columns)
                print("\n")
            elif command == "COUNT":
                table_name, condition_str = rest.split(" WHERE ", 1)
                conditions = eval(condition_str)
                tables = COUNT(table_name, conditions)
                print("\n")

if __name__ == "__main__":  #execute the main function
    table=[] #contains tables which created with create function and updated with other functions
    main()