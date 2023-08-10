
from ij import IJ
import glob,os  
path=r"C:\Users\Yansong Han\Desktop\参数提取自动化\pic_mask"
for infile in glob.glob(path+"/*.png"):
    file = os.path.splitext(os.path.basename(infile))[0]
    imp = IJ.openImage(infile)
    IJ.run(imp, "Analyze Regions", "area perimeter circularity max._feret")
    IJ.saveAs("Results", r"C:\Users\Yansong Han\Desktop\参数提取自动化\data"+file+".csv")
