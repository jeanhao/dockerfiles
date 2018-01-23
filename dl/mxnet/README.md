# MxNet

The GPU version times out when building on Docker Hub. They have to be built locally and pushed to the Docker Registry.

To build Docker image locally (Note: takes a few hours):
* Python 2: `docker build -t registry.cn-shanghai.aliyuncs.com/russell-hub/mxnet:latest-gpu-py2 -f Dockerfile-py2.gpu .`

To push image to Docker registry:
* Python 2: `docker push registry.cn-shanghai.aliyuncs.com/russell-hub/mxnet:latest-gpu-py2`