# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]


#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)

census=np.concatenate((data,new_record))


# --------------
#Code starts here
import numpy as np

age=np.array([census[:,0]])

max_age=age.max()
min_age=age.min()
age_mean=np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here
import  numpy as np

race_0=np.empty((0,8),int)
race_1=np.empty((0,8),int)
race_2=np.empty((0,8),int)
race_3=np.empty((0,8),int)
race_4=np.empty((0,8),int)

rows,cols=np.shape(census)

for i in range(0,rows):
    if census[i][2]==0:
        race_0=np.append(race_0,np.vstack(([census[i][:]])),axis=0)
    elif census[i][2]==1:
        race_1=np.append(race_1,np.vstack(([census[i][:]])),axis=0)
    elif census[i][2]==2:
        race_2=np.append(race_2,np.vstack(([census[i][:]])),axis=0)
    elif census[i][2]==3:
        race_3=np.append(race_3,np.vstack(([census[i][:]])),axis=0)
    else:
        race_4=np.append(race_4,np.vstack(([census[i][:]])),axis=0)

#race_3=reshape[][8]
#print(race_3)
len_0,x=race_0.shape
len_1,x=np.shape(race_1)
len_2,x=np.shape(race_2)
len_3,x=np.shape(race_3)
len_4,x=np.shape(race_4)

l=[len_0, len_1, len_2, len_3, len_4]

minority_race=l.index(min(l))
print(minority_race)

#print(l)



# --------------
#Code starts here
senior_citizens=np.empty((0,8))
s=[]
for i in range(0,rows):
    if int(census[i][0])>60:
        senior_citizens=np.append(senior_citizens, np.vstack(([census[i][:]])),axis=0)

l=([sum(x) for x in zip(*senior_citizens)])

working_hours_sum=l[6]
senior_citizens_len, x=senior_citizens.shape
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
high=np.empty((0,8))
low=np.empty((0,8))

for i in range(0,rows):
        if census[i][1]>10:
                high=np.append(high,np.vstack(([census[i][:]])),axis=0)
        else:
                low=np.append(low,np.vstack([census[i][:]]),axis=0)

low_mean=np.mean(low,axis=0)
high_mean=np.mean(high,axis=0)

avg_pay_high=high_mean[7]
avg_pay_low=low_mean[7]

print(avg_pay_high>avg_pay_low)


