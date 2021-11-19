import random

from PIL import Image
def Rotation(image,dirname,name,isTrue,Stain):
    num = random.randint(0,3)
    if isTrue:
        for i in range(0,360,90):
            if num*90 ==i:
                im = image.rotate(i).save("../Datasets\\Augmented\\"+Stain+" - Test\\"+dirname+"\\"+name+"_"+str(i)+".png")
            else:
                im = image.rotate(i).save("../Datasets\\Augmented\\" + Stain + " - Validation\\" + dirname + "\\" + name + "_" + str(i) + ".png")
    else:
        for i in range(0,360,90):
            im = image.rotate(i).save("../Datasets\\Augmented\\"+Stain+" - Train\\"+dirname+"\\"+name+"_"+str(i)+".png")
    print(name, Stain, isTrue," Done")
names = ["Benign","InSitu","Invasive","Normal"]
labels =["b","is","iv","n"]

for n in range(len(names)):
    setOfNumbers = set()
    while len(setOfNumbers) < 15:
        setOfNumbers.add(random.randint(1, 100))

    for i in range(1,101):
        name = labels[n]
        if i < 10:
            name += "00"
        if i > 9 and i < 100:
            name += "0"
        name += str(i)
        reinhard = name+"Reinhard"
        macenko = name+"Macenko"

        Reinhard = Image.open("../Datasets\\Stain_Norm\\Reinhard\\"+names[n]+"\\"+reinhard+".png")
        Macenko = Image.open("../Datasets\\Stain_Norm\\Macenko\\"+names[n]+"\\"+macenko+".png")
        if setOfNumbers.__contains__(i):
            Rotation(Reinhard,names[n],reinhard,True,"Reinhard")
            Rotation(Macenko, names[n], macenko, True, "Macenko")
        else:
            Rotation(Reinhard, names[n], reinhard, False, "Reinhard")
            Rotation(Macenko, names[n], macenko, False, "Macenko")

