OPENPOSE_URL="http://posefs1.perception.cs.cmu.edu/OpenPose/models/"
FACE_FOLDER="face/"
POSE_FOLDER="pose/"

FACE_MODEL=${FACE_FOLDER}"pose_iter_116000.caffemodel"
wget -c ${OPENPOSE_URL}${FACE_MODEL} -P ${FACE_FOLDER}
wget -c "https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/face/pose_deploy.prototxt" -P ${FACE_FOLDER}

MPI_FOLDER=${POSE_FOLDER}"mpi/"
MPI_MODEL=${MPI_FOLDER}"pose_iter_160000.caffemodel"
wget -c ${OPENPOSE_URL}${MPI_MODEL} -P ${MPI_FOLDER}
wget -c "https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt" -P ${MPI_FOLDER}

COCO_FOLDER=${POSE_FOLDER}"coco/"
COCO_MODEL=${COCO_FOLDER}"pose_iter_440000.caffemodel"
wget -c ${OPENPOSE_URL}${COCO_MODEL} -P ${COCO_FOLDER}
wget -c "https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/pose/coco/pose_deploy_linevec.prototxt" -P ${COCO_FOLDER}