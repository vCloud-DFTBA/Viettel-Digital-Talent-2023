import pandas

df = pandas.read_csv("attendees.csv")

# listAttendees = [row.to_dict() for idx, row in df.iterrows()]
# print(df.size)
listAttendees = [{'name': df.iloc[i, 1], 'school': df.iloc[i, 4]} for i in range(df.shape[0])]
print(listAttendees)
# for row in df:
#     print(row)
