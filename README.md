# inference-rosa-workshop
# This is a workshop for deploying a Pytorch & FastAPI project to ROSA on AWS and perform inference.
# This adds a Gradio Frontend to the project 
Upload in your images to see the predictions made by the model in a web interface.
Mod by Andrew Grimes and Jim Garrett of Red Hat 

Forked from this project for a workshop: https://github.com/hasibzunair/imagercg-waiter
ResNet18 https://www.mathworks.com/help/deeplearning/ref/resnet18.html

Containerized app that serves a containerized Resnet18 deep learning image classification model using FastAPI. We used an ImageNet pretrained model that can predict 1000 different classes of general objects, the samples are animals but it will work with anything. See class list [here](https://deeplearning.cms.waikato.ac.nz/user-guide/class-maps/IMAGENET/).


Sample Backend Input Image: 
<p align="left">
  <a href="#"><img src="./sample.jpg" width="600"></a> <br />
  <em> 
  </em>
</p>

Sample Text Output:


OpenShift/ROSA Web Front End instructions (deck to be created) 
1. The URL for the backend is required to be "added" into this image prior to building to work for your account or use case. 

2. Use your github account and fork the project to your account. Make sure your repo is public. 
gh repo clone emcon33/inference-rosa-frontend

3. Collect the URL of your backend web page and update Main.py with your URL and commit
REST_API_URL = "https://inference-rosa-workshop-test2.apps.rosa-wz89j.pbio.p1.openshiftapps.com/api/predict"

4. On ROSA build the front end project from the github page

5. Click on the web page open and upload your images. 





#ArgoCD/Tekton Pipeline 
https://docs.openshift.com/container-platform/4.10/cicd/gitops/setting-up-argocd-instance.html


Original source https://towardsai.net/p/machine-learning/build-and-deploy-custom-docker-images-for-object-recognition
Forked from this github https://github.com/hasibzunair/imagercg-waiter


`