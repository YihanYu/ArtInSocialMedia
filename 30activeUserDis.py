import csv
import os
import MatrixUpdated
for file in os.listdir('/Users/YihanYu/Desktop/ab/comb'):
    filename = os.path.basename(file)
    print filename
    fileInput = "/Users/YihanYu/Desktop/ab/comb" + "//" + filename
    fileOutput='result_'+filename
    with open(fileInput) as csvfile:
        rows = csv.reader(csvfile)
        with open(fileOutput,'w') as f:
            writer = csv.writer(f)
            for row in rows:
                if row[0]=='shot1_id':
                    row.append('dis')
                    writer.writerow(row)
                else:
                    dis=MatrixUpdated.calculateDis(eval(row[2]),eval(row[5]))
                    row.append(str(dis))
                    writer.writerow(row)