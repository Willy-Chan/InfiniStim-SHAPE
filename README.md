# InfiniStim
## Synopsis
This is a tool for generating a virtually unlimited amount of visual stimuli using minimal components. The current version was primarily developed to supplement [ROAR-Shape](https://roar.stanford.edu/), which is a shape-matching task I developed for the [Yeatman Lab](https://jacobsfoundation.org/fellows/jacobs-foundation-research-fellowship-en/jason-yeatman/) to diagnose and screen for dyslexia. 

However, it can also be broadly used for any similar needs/cognitive experiments involving visual stimuli. The components themselves can be generated via AI (this project leveraged [OpenAI's DALL-E 2 model](https://openai.com/dall-e-2)), and the resulting parts can be stitched together via the provided Python program.

A version of this code written in JavaScript is also provided, in the case of integrating this into a full-stack web application.

## Table of Contents
- [Installation](#installation)
- [Demo](#demo)
- [Usage](#usage)

## Installation

Before you start, ensure you have met **one** of the following requirements:
* You have a **Windows/Linux/Mac** machine running the latest version of **Python**.
* You have a **Javascript** environment setup with **Node.js** installed.

To install InfiniStim Python, follow these steps:
```shell
git clone https://github.com/<your_username>/infinistim.git
cd infinistim
pip install -r requirements.txt
```

To use the JavaScript implementation, install the required packages using npm:
```shell
npm install sharp
npm install shuffle-array
```

## Demo
Sample inputs:  

![image of component 1](https://github.com/Willy-Chan/image-quilter/blob/master/ai_images/11.png?raw=true)
![image of component 2](https://github.com/Willy-Chan/image-quilter/blob/master/ai_images/3.png?raw=true)
![image of component 5](https://github.com/Willy-Chan/image-quilter/blob/master/ai_images/8.png?raw=true)
![image of component 10](https://github.com/Willy-Chan/image-quilter/blob/master/ai_images/12.png?raw=true)

Sample output:  

![image of component 10](https://github.com/Willy-Chan/image-quilter/blob/master/result/11_3_8_12.png?raw=true)

Even with relatively simple inputs, the output can be quite complex! The number of possible stimuli can grow exponentially.

## Usage
To use InfiniStim, simply place the component images in the correct folder and run the main Python function:
```shell
python main.py
```

You can also navigate to the relevant folder and run the JavaScript code:
```shell
generate_shapes.js
```
