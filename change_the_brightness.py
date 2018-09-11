import numpy as np
import cv2
def numpy_distance_decay(init_array):
    assert len(init_array.shape)==3 ,"The array's dims  should be 3"
    h,w,_=init_array.shape
    #radius=np.ceil(np.sqrt(h**2+w**2)/2)
    radius=np.ceil(min(h,w)/2)
    ctr_x=int(w/2)
    ctr_y=int(h/2)
    value=init_array[0,0,0]
    for i in range(h):
        for j in range(w):
            if np.sqrt((i-ctr_y)**2+(j-ctr_x)**2)/radius>1:
                init_array[i,j]=0
            else:
                init_array[i,j]=int(value*(1-np.sqrt((i-ctr_y)**2+(j-ctr_x)**2)/radius))
    print(init_array.dtype)
    return init_array.astype(np.uint8)
def local_brightness_increasement(img,increment):
    """
    :param img: image being edited
    :param increment: the increment of brightness
    :return:  the image edited
    """
    assert len(img.shape)==3 ,"the channels must be 3"
    h,w,_=img.shape
    local_h=np.random.randint(2*h/3,h)
    local_w=np.random.randint(2*h/3,w)
    y_start=np.random.randint(0,h-local_h)
    x_start=np.random.randint(0,w-local_w)
    img=img.astype(np.uint8)
    increment=np.ones([local_h,local_w,3],dtype=np.uint8)*increment

    img[y_start:y_start+local_h,x_start:x_start+local_w,:]=cv2.add(img[y_start:y_start+local_h,x_start:x_start+local_w,:],numpy_distance_decay(increment))

    return img

if __name__=="__main__":
    image_path="D:/face/test_cropped/facescrub_aligned/Aaron_Eckhart/Aaron_Eckhart_1.png"

    img=cv2.imread(image_path,1)
    img=local_brightness_increasement(img,increment=300)
    cv2.namedWindow("luzihao")

    cv2.imshow("luzihao",img)
    cv2.waitKey(0)
