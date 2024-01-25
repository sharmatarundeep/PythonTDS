a = "Cisco Switch"
print(a.index("i"))  # find the first occurrence of i
print(a.index("sco"))  # find the index of sco
print(a.count("i"))  # count i
print(a.find("sco"))  # use find or index directly
print(a.find("tarun"))  # return -1 = not found

print(a.lower())
print(a.upper())
print(a)  # string did not change with upper and lower its immutable

print(a.startswith("Cis"))  # True
print(a.endswith("h"))  # True
print(a.endswith("H"))  # False

b = "  Cisco    Switch  "
print(b)
print(b.strip())  # strip extra spaces from beginning and end only

b = "$$Cisco $$ Switch$$"
print(b)
print(b.strip('$'))  # strip # from beginning and end only

b = "Cisco,Arista,Juniper,HP"
print(b.strip(','))  # return list of characters separated by ,

b = "  Cisco    Switch  "
print(b.replace(" ", ""))  # replace spaces with nothing

b = "Cisco Switch"
print("_".join(b))  # C_i_s_c_o_ _S_w_i_t_c_h

l = ["Cisco", "Arista", "Juniper", "HP"]
print(",".join(l))
