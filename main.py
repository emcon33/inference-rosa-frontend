import gradio as gr
import requests

# Set URL
# Run: 
# update REST_API_URL to your backend link (currently not dynamic)
REST_API_URL = "https://inference-rosa-workshop-deleteme.apps.j3k4m7b6.eastus.aroapp.io/api/predict"

# Inference!
def inference(image_path):

    # Load the input image and construct the payload for the request
    image = open(image_path, "rb").read()
    payload = {"image": image}

    # Submit the request
    r = requests.post(REST_API_URL, files=payload).json()

    # Ensure the request was sucessful, format output for visualization
    output = {}
    if r["success"]:
        # Loop over the predictions and display them
        for (i, result) in enumerate(r["predictions"]):
            output[result["label"]] = result["probability"]
            print("{}. {}: {:.4f}".format(i + 1, result["label"],
                result["probability"]))
    else:
        print("Request failed")
    return output

# Define ins outs placeholders
inputs = gr.inputs.Image(type='filepath')
outputs = gr.outputs.Label(type="confidences",num_top_classes=5)

# Define style
title = "ROSA Workshop Gradio Front End"
description = "This is the web front end to add a web interfface to an AI app on ROSA for image classification based on ResNet18. This is a port of an article linked below"
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1512.03385' target='_blank'>ResNet18 Deep Residual Learning for Image Recognition</a> | <a href='https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py' target='_blank'>Github Repo</a></p>"

# Run inference
frontend = gr.Interface(inference, 
            inputs, 
            outputs, 
            examples=["test3.jpeg", "test4.jpeg"], 
            title=title, 
            description=description, 
            article=article,
            analytics_enabled=False)


# Launch app and set PORT
try:
    frontend.launch(server_name="0.0.0.0", server_port=8080)
except KeyboardInterrupt:
    frontend.close()
except Exception as e:
    print(e)
    frontend.close()



