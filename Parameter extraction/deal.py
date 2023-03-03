from ij import IJ
import glob,os  
path="/Users/hanyansong/Study/J2/srt/LungNew/pic_over" #这里设置为pic_over的绝对路径
i=0
for infile in glob.glob(path+"/*.png"):
	imp = IJ.openImage(infile)
	IJ.run(imp, "Analyze Regions", "area perimeter circularity max._feret")
	IJ.saveAs("Results", "/Users/hanyansong/Study/J2/srt/LungNew/result/"+str(i)+".csv")
	i+=1