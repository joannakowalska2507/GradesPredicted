num_to_label={
    3:"Bardzo dobry",
    2:"Dobry",
    1:"Dostateczny",
    0:"Niedostateczny"
}
#change to label
def label_from_num(num):
    return num_to_label[num]