print("\tWelcome to roshanthecoderr\nThis is Data conversion Program made by ROSHAN KUMAR")
print("\tYou can convert following datas\n\t\tKB to B\n\t\tMB to KB\n\t\tGB to MB\n\t\tTB to GB\n\t\tPB to TB\n\t\tand vice-versa")

# All inputs are here
actual_data = input("Enter actual data form: ")
data = int(input("Enter the data: "))
convert = input("Enter which form you want to convert data: ")

# Data conversion
kilobyte = 1024  # In byte
megabyte = 1024 * kilobyte
gigabyte = 1024 * megabyte
terabyte = 1024 * gigabyte
petabyte = 1024 * terabyte

# actual data in b and convert into other
if actual_data.lower() == "b" or actual_data.lower() == "byte":
    if convert.lower() == "b" or convert.lower() == "byte":
        print(f"{data} BYTE => {data} BYTE")
    elif convert.lower() == "kb" or convert.lower() == "kilobyte":
        print(f"{data} BYTE => {(1/kilobyte)*data} KILOBYTE")
    elif convert.lower() == "mb" or convert.lower() == "megabyte":
        print(f"{data} BYTE => {(1/megabyte)*data} MEGABYTE")
    elif convert.lower() == "gb" or convert.lower() == "GIGABYTE":
        print(f"{data} BYTE => {(1/gigabyte)*data} GIGABYTE")
    elif convert.lower() == "tb" or convert.lower() == "terabyte":
        print(f"{data} BYTE => {(1/terabyte)*data} TERABYTE")
    elif convert.lower() == "pb" or convert.lower() == "petabyte":
        print(f"{data} BYTE => {(1/petabyte)*data} PETABYTE")
# actual data in kb and convert into other
elif actual_data.lower() == "kb" or actual_data.lower() == "kilobyte":
    # Data conversion in kilobyte
    megabyte = 1024
    gigabyte = 1024 * megabyte
    terabyte = 1024 * gigabyte
    petabyte = 1024 * terabyte
    if convert.lower() == "b" or convert.lower() == "byte":
        print(f"{data} KILOBYTE => {kilobyte*data} BYTE")
    elif convert.lower() == "kb" or convert.lower() == "kilobyte":
        print(f"{data} KILOBYTE => {data} KILOBYTE")
    elif convert.lower() == "mb" or convert.lower() == "megabyte":
        print(f"{data} KILOBYTE => {(1/megabyte)*data} MEGABYTE")
    elif convert.lower() == "gb" or convert.lower() == "gigabyte":
        print(f"{data} KILOBYTE => {(1/gigabyte)*data} GIGABYTE")
    elif convert.lower() == "tb" or convert.lower() == "terabyte":
        print(f"{data} KILOBYTE => {(1/terabyte)*data} TERABYTE")
    elif convert.lower() == "pb" or convert.lower() == "petabyte":
        print(f"{data} KILOBYTE => {(1/petabyte)*data} PETABYTE")
# actuall data in mb and convert into other
elif actual_data.lower() == "mb" or actual_data.lower() == "megabyte":
    # Data conversion in megabyte
    gigabyte = 1024
    terabyte = 1024 * gigabyte
    petabyte = 1024 * terabyte
    if convert.lower() == "b" or convert.lower() == "byte":
        print(f"{data} MEGABYTE => {megabyte*data} BYTE")
    elif convert.lower() == "kb" or convert.lower() == "kilobyte":
        print(f"{data} MEGABYTE => {kilobyte*data} KILOBYTE")
    elif convert.lower() == "mb" or convert.lower() == "megabyte":
        print(f"{data} MEGABYTE => {data} MEGABYTE")
    elif convert.lower() == "gb" or convert.lower() == "gigabyte":
        print(f"{data} MEGABYTE => {(1/gigabyte)*data} GIGABYTE")
    elif convert.lower() == "tb" or convert.lower() == "terabyte":
        print(f"{data} MEGABYTE => {(1/terabyte)*data} TERABYTE")
    elif convert.lower() == "pb" or convert.lower() == "petabyte":
        print(f"{data} MEGABYTE => {(1/petabyte)*data} PETABYTE")
# actual data in gb and convert into other
elif actual_data.lower() == "gb" or actual_data.lower() == "gigabyte":
    # Data conversion in gigabyte
    terabyte = 1024
    petabyte = 1024 * terabyte
    if convert.lower() == "b" or convert.lower() == "byte":
        print(f"{data} GIGABYTE => {gigabyte*data} BYTE")
    elif convert.lower() == "kb" or convert.lower() == "kilobyte":
        print(f"{data} GIGABYTE => {megabyte*data} KILOBYTE")
    elif convert.lower() == "mb" or convert.lower() == "megabyte":
        print(f"{data} GIGABYTE => {kilobyte*data} MEGABYTE")
    elif convert.lower() == "gb" or convert.lower() == "gigabyte":
        print(f"{data} GIGABYTE => {data} GIGABYTE")
    elif convert.lower() == "tb" or convert.lower() == "terabyte":
        print(f"{data} GIGABYTE => {(1/terabyte)*data} TERABYTE")
    elif convert.lower() == "pb" or convert.lower() == "petabyte":
        print(f"{data} GIGABYTE => {(1/petabyte)*data} PETABYTE")
# actual data in tb and convert into other
elif actual_data.lower() == "tb" or actual_data.lower() == "terabyte":
    # Data conversion in terabyte
    petabyte = 1024
    if convert.lower() == "b" or convert.lower() == "byte":
        print(f"{data} TERABYTE => {terabyte*data} BYTE")
    elif convert.lower() == "kb" or convert.lower() == "kilobyte":
        print(f"{data} TERABYTE => {gigabyte*data} KILOBYTE")
    elif convert.lower() == "mb" or convert.lower() == "megabyte":
        print(f"{data} TERABYTE => {megabyte*data} MEGABYTE")
    elif convert.lower() == "gb" or convert.lower() == "gigabyte":
        print(f"{data} TERABYTE => {kilobyte*data} GIGABYTE")
    elif convert.lower() == "tb" or convert.lower() == "terabyte":
        print(f"{data} TERABYTE => {data} TERABYTE")
    elif convert.lower() == "pb" or convert.lower() == "petabyte":
        print(f"{data} TERABYTE => {(1/petabyte)*data} PETABYTE")
# actual data in pb and convert into other
elif actual_data.lower() == "pb" or actual_data.lower() == "petabyte":
    if convert.lower() == "b" or convert.lower() == "byte":
        print(f"{data} PETABYTE => {petabyte*data} BYTE")
    elif convert.lower() == "kb" or convert.lower() == "kilobyte":
        print(f"{data} PETABYTE => {terabyte*data} KILOBYTE")
    elif convert.lower() == "mb" or convert.lower() == "megabyte":
        print(f"{data} PETABYTE => {gigabyte*data} MEGABYTE")
    elif convert.lower() == "gb" or convert.lower() == "gigabyte":
        print(f"{data} PETABYTE => {megabyte*data} GIGABYTE")
    elif convert.lower() == "tb" or convert.lower() == "terabyte":
        print(f"{data} PETABYTE => {kilobyte*data} TERABYTE")
    elif convert.lower() == "pb" or convert.lower() == "petabyte":
        print(f"{data} PETABYTE => {data} PETABYTE")
else:
    print("Opps! Please Check your input")
