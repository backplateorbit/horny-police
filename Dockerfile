FROM python:3.9

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install cmake -y
RUN apt-get install protobuf-compiler -y

RUN pip install --upgrade pip
RUN pip install cmake
RUN pip install nudenet celery tensorflow numpy protobuf typing-extensions ecs_logging
RUN pip install --upgrade setuptools
RUN pip install onnxruntime
RUN pip install discord.py
RUN pip install python-dotenv
RUN pip install ecs_logging

WORKDIR /workspace
VOLUME ["/workspace"]

COPY ./model_data/detector_v2_default_checkpoint.onnx /root/.NudeNet/default/detector_v2_default_checkpoint.onnx
COPY ./model_data/classifier_model.onnx /root/.NudeNet/classifier_model.onnx
COPY ./model_data/detector_v2_default_classes /root/.NudeNet/detector_v2_default_classes
COPY ./model_data/detector.py /usr/local/lib/python3.9/site-packages/nudenet/detector.py
COPY ./model_data/classifier.py /usr/local/lib/python3.9/site-packages/nudenet/classifier.py