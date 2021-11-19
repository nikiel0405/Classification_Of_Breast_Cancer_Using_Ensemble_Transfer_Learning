import numpy as np
from PIL import Image

from Preprocessing import StainNorm_Reinhard,StainNorm_Macenko
from Preprocessing import StainNorm_utilities as ut

names = ["Benign","InSitu","Invasive","Normal"]
labels =["b","is","iv","n"]
target_files = ["TargetBenign.png","TargetInSitu.png","TargetInvasive.png","TargetNormal.png"]

for n in range(len(names)):

    for i in range(1,101):
        name = labels[n]
        if i < 10:
            name += "00"
        if i > 9 and i < 100:
            name += "0"
        name += str(i)
        target = ut.read_image("../"+target_files[n])
        original = np.array(ut.read_image("../Datasets\\Original\\"+names[n]+"\\"+name+".tif"))

        reinhard = StainNorm_Reinhard.Normalizer()
        reinhard.fit(np.array(target))
        reinhard_output = reinhard.transform(original)

        macenko = StainNorm_Macenko.Normalizer()
        macenko.fit(np.array(target))
        macenko_output = macenko.transform(original)

        Reinhard = Image.fromarray(reinhard_output)
        Macenko = Image.fromarray(macenko_output)


        Reinhard.save("../Datasets\\Stain_Norm\\Reinhard\\"+names[n]+"\\"+name+"Reinhard.png")
        Macenko.save("../Datasets\\Stain_Norm\\Macenko\\"+ names[n] +"\\"+ name +"Macenko.png")
        print(name, "Completed")
