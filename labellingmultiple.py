import numpy as np 

numobjects=4		# these values are normally only knewn by the dimension of the inputs
numpoints=500

# create random SLAM output
points = np.random.random((3,numpoints))
points = points*20
n_p=points.size/3		# calcultes the number of points in the map

# create usual image size
pixels=np.matrix([320,240]) 	# image size

# create random tensor flow output
classes = np.arange(numobjects)
confidences = np.random.random((numobjects,1))
bb = np.random.random((numobjects,4))
bb = bb*0.5
bb[:,1]=bb[:,0]*2*pixels[0,0]
bb[:,3]=bb[:,2]*2*pixels[0,1]
bb[:,0]=bb[:,0]*pixels[0,0]
bb[:,2]=bb[:,2]*pixels[0,1]
n_o=bb.size/4


# create random camera position
T=np.matrix([0.,0.,0.])			# Position of Camera global
T=np.transpose(T)
R=np.matrix([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])		# Rotation Matrix of Camera
f=35.0 					# focal length



##==============================================================================================##
##				Actual skript starts here					##
##==============================================================================================##


def coordtransform(i):
	X=points[:,i]
	XT = (R.T)*(X-T)
	Xu = -np.matrix([[f*XT.item(0)/XT.item(2)],[f*XT.item(1)/XT.item(2)]])+c
	return Xu

def labelling(j,i):
	if Xu.item(0)>bb[j,0] and Xu.item(0)<bb[j,1] and Xu.item(1)>bb[j,2] and Xu.item(1)<bb[j,3]:
		label=1
	else:
		label=0
	return label


def text_label(j,i,distalt):
	center=np.matrix([bb[j,1]-bb[j,0],bb[j,3]-bb[j,2]])
	dist=np.linalg.norm(Xu-center)
	if distalt==999.0:
		lp=i
		distalt=dist
	else:
		if dist<distalt:
			lp=i
			distalt=dist
		else:
			lp=-1
	return [lp,distalt]


# Image Center in Pixels
c=np.matrix([pixels.item(0)/2,pixels.item(1)/2])
c=c.T

labelpoint=np.zeros((3,n_o),dtype=int)
for j in range(n_o):
	label=np.zeros((n_o,n_p),dtype=int)
	distalt=999.0
	for i in range(n_p):
		Xu=coordtransform(i)
		label[j,i]=labelling(j,i)
		label[j,i]=label[j,i]*classes[j]
		[lp_v,distalt]=text_label(j,i,distalt)
		if lp_v==-1:
			lp_v=lp_v
		else:
			lp=lp_v
	labelpoint[:,j]=points[:,lp]
		


print (labelpoint)


	

