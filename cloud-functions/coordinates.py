
def get_cordinate():
    lst = {}
    with open ("./coordinates.txt", 'r') as f:
        t = f.read()
        fl = t.split('\n')
        for i in range(2, len(fl)):
            l = [x.strip(',') for x in fl[i].split("\t")]
            k = [j.strip(" ") for j in l]
            lst[l[0].strip(", the USA")] = k[1:]
        print(lst)

#get_cordinate()

co = {'Northern Mariana Islands': ['15.183333', '145.750000'],'Wisconsin': ['44.500000', '-89.500000'], 'West Virginia': ['39.000000', '-80.500000'], 'Vermont': ['44.000000', '-72.699997'], 'Texas': ['31.000000', '-100.000000'], 'South Dakota': ['44.500000', '-100.000000'], 'Rhode Island': ['41.700001', '-71.500000'], 'Oregon': ['44.000000', '-120.500000'], 'New York': ['43.000000', '-75.000000'], 'New Hampshire': ['44.000000', '-71.500000'], 'Nebraska': ['41.500000', '-100.000000'], 'Kansas': ['38.500000', '-98.000000'], 'Mississippi': ['33.000000', '-90.000000'], 'Illinois': ['40.000000', '-89.000000'], 'Delaware': ['39.000000', '-75.500000'], 'Connecticut': ['41.599998', '-72.699997'], 'Arkansas': ['34.799999', '-92.199997'], 'Indiana': ['40.273502', '-86.126976'], 'Missouri': ['38.573936', '-92.603760'], 'Florida': ['27.994402', '-81.760254'], 'Nevada': ['39.876019', '-117.224121'], 'Maine': ['45.367584', '-68.972168'], 'Michigan': ['44.182205', '-84.506836'], 'Georgia': ['33.247875', '-83.441162'], 'Hawaii': ['19.741755', '-155.844437'], 'Alaska': ['66.160507', '-153.369141'], 'Tennessee': ['35.860119', '-86.660156'], 'Virginia': ['37.926868', '-78.024902'], 'New Jersey': ['39.833851', '-74.871826'], 'Kentucky': ['37.839333', '-84.270020'], 'North Dakota': ['47.650589', '-100.437012'], 'Minnesota': ['46.392410', '-94.636230'], 'Oklahoma': ['36.084621', '-96.921387'], 'Montana': ['46.965260', '-109.533691'], 'Washington': ['47.751076', '-120.740135'], 'Utah': ['39.419220', '-111.950684'], 'Colorado': ['39.113014', '-105.358887'], 'Ohio': ['40.367474', '-82.996216'], 'Alabama': ['32.318230', '-86.902298'], 'Iowa': ['42.032974', '-93.581543'], 'New Mexico': ['34.307144', '-106.018066'], 'South Carolina': ['33.836082', '-81.163727'], 'Pennsylvania': ['41.203323', '-77.194527'], 'Arizona': ['34.048927', '-111.093735'], 'Maryland': ['39.045753', '-76.641273'], 'Massachusetts': ['42.407211', '-71.382439'], 'California': ['36.778259', '-119.417931'], 'Idaho': ['44.068203', '-114.742043'], 'Wyoming': ['43.075970', '-107.290283'], 'North Carolina': ['35.782169', '-80.793457'], 'Louisiana': ['30.391830', '-92.329102']}