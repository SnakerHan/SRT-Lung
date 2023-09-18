
from ij import IJ
import glob,os  
import time
path = "C:\\Users\\Yansong Han\\Desktop\\LungAuto\\pic_mask"
for infile in glob.glob(path+"/*.png"):
    file = os.path.splitext(os.path.basename(infile))[0]
    imp = IJ.openImage(infile)
    IJ.run(imp, "Analyze Regions", "area perimeter circularity max._feret")
    IJ.saveAs("Results", "C:\\Users\\Yansong Han\\Desktop\\LungAuto\\data"+"\\"+file+".csv")
IJ.getInstance().exit()
IJ.run("Quit")
