import os

def generate_negative_description_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')



#python
#from cascadeutils import generate_negative_description_file
#generate_negative_description_file()
#exit()


#opencv_annotation -a=pos.txt -i=positive

#opencv_createsamples -info pos.txt -w 50 -h 50 -num 1000 -vec pos.vec

#opencv_traincascade -data cascade/ -vec pos.vec -bg neg.txt -w 200 -h 200 -numPos 15 -numNeg 1000 -numstages 10



