def TT1():
    name = "Vintage socks"
    tag = "footwear"
    description = "cool design/logo"
    price = "5"
    size = "Men's M"
    folder ="barbarella" #name of folder file is stored in
    info = {"name": name, "tag":tag, "description": description, "size":size, "price": price, "folder":folder}
    return info


def inventory_itemsTT():
    return [TT1()]