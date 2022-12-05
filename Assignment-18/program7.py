"""7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries."""
d1={"ram","Java","Python"}
d2={"C","React",66,34}
d3={"Rahul","Ajay","Roshani"}
d4={"Anuj",77,44,99}
d4.update(d1,d2,d3)
print(d4)