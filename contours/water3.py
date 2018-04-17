
import cv2
import random
import numpy as np

def RandomColor(value):
  others = value // 255
  aa = random.randint(0,others)
  bb = random.randint(0,others)
  cc = random.randint(0,others)
  return (aa,bb,cc)


image = cv2.imread("../sources/wu.jpg")
cv2.imshow("Source", image)


# Mat imageGray;
# cvtColor(image,imageGray,CV_RGB2GRAY);//灰度转换
# GaussianBlur(imageGray,imageGray,Size(5,5),2);   //高斯滤波
# imshow("Gray Image",imageGray);
# Canny(imageGray,imageGray,80,150);
# imshow("Canny Image",imageGray);

# 灰度化，滤波，Canny边缘检测
imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(imgray, (5, 5), 0)
cv2.imshow("Gray", imgray)
edges = cv2.Canny(imageGray, 80, 150)
cv2.imshow("Canny", edges)

#查找轮廓
#vector<vector<Point>> contours;
#vector<Vec4i> hierarchy;
#findContours(imageGray,contours,hierarchy,RETR_TREE,CHAIN_APPROX_SIMPLE,Point());
#Mat imageContours=Mat::zeros(image.size(),CV_8UC1);  //轮廓
#Mat marks(image.size(),CV_32S);   //Opencv分水岭第二个矩阵参数
#marks=Scalar::all(0);
#int index = 0;
#int compCount = 0;
#for( ; index >= 0; index = hierarchy[index][0], compCount++ )
#{
#	//对marks进行标记，对不同区域的轮廓进行编号，相当于设置注水点，有多少轮廓，就有多少注水点
#	drawContours(marks, contours, index, Scalar::all(compCount+1), 1, 8, hierarchy);
#	drawContours(imageContours,contours,index,Scalar(255),1,8,hierarchy);
#}

ret, binary = cv.threshold(edges, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
skinCrCbHist = np.zeros((256, 256, 1), dtype = "uint8")
Mask= cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_8U, 3)
cv.Set(Mask, cv.Scalar(0x00,0x00,0xff))
index = 0
compCount = 0
for x in hierarchy[index][0]
  cv.drawContours(marks, contours, index, Scalar::all(compCount+1), 1, 8, hierarchy)
  cv.drawContours(imageContours, contours, index, Scalar(255),1,8,hierarchy);


//我们来看一下传入的矩阵marks里是什么东西
Mat marksShows;
convertScaleAbs(marks,marksShows);
imshow("marksShow",marksShows);
imshow("轮廓",imageContours);
watershed(image,marks);

//我们再来看一下分水岭算法之后的矩阵marks里是什么东西
Mat afterWatershed;
convertScaleAbs(marks,afterWatershed);
imshow("After Watershed",afterWatershed);

//对每一个区域进行颜色填充
Mat PerspectiveImage=Mat::zeros(image.size(),CV_8UC3);
for(int i=0;i<marks.rows;i++)
{
	for(int j=0;j<marks.cols;j++)
	{
		int index=marks.at<int>(i,j);
		if(marks.at<int>(i,j)==-1)
		{
			PerspectiveImage.at<Vec3b>(i,j)=Vec3b(255,255,255);
		}
		else
		{
			PerspectiveImage.at<Vec3b>(i,j) =RandomColor(index);
		}
	}
}
imshow("After ColorFill",PerspectiveImage);

//分割并填充颜色的结果跟原始图像融合
Mat wshed;
addWeighted(image,0.4,PerspectiveImage,0.6,0,wshed);
imshow("AddWeighted Image",wshed);

waitKey();



