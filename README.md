# Dockerfiles

Collection of Dockerfiles useful for NLP and Deep Learning. To download the docker images
visit: [floydhub's Docker Hub](https://hub.docker.com/r/registry.cn-shanghai.aliyuncs.com/russell-hub/).


## Naming conventions

Dockerfiles are organized into the following directory structure:

```
CATEGORY/PROJECT_NAME/VERSION/Dockerfile-ENV
CATEGORY/PROJECT_NAME/VERSION/Dockerfile-ENV.gpu
```

Automated build scripts will generate the following tags for images based on
the above dockerfile paths:

```
registry.cn-shanghai.aliyuncs.com/russell-hub/PROJECT_NAME:VERSION-ENV
registry.cn-shanghai.aliyuncs.com/russell-hub/PROJECT_NAME:VERSION-ENV-gpu
```

Contains docker images for popular deep learning frameworks including: Tensorflow, PyTorch and Torch.
