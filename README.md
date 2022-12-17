# Sign-Language-Recognition
AI Assistance tool for Sign language using Computer Vision
### Table of Contents  
- [Overview](#Overview)  
- [Problem Solution](#Problem%Solution) 
- [Demo](#Demo) 
- [Installation](#Installation) 
- [Run](#Run) 
- [Technologies Used](#Technologies%Used) 
- [Got a Question](#Got%a%Question%?) 



### Overview
Humans communicate with one another to share their thoughts, feelings and experiences. But this is not the case for the deaf-mute. There are many people who face these disabilities right from birth or because of issues such as Selective mutism, Aphasia syndrome, Alport syndrome, Norrie syndrome etc.A large number of the population is disconnected from the mainstream hearing-dominated society and lie at the risk of being marginalized because people who are limited to using only speech can’t communicate with them. A lack of accessibility to support the conversation between both communities also adds to the problem. Due to this , there is a communication gap between the deaf-mute and those who can speak.To bridge this gap, a non-verbal language called sign language exists. According to the World Federation of the Deaf, there are more than 70 million deaf people worldwide. More than 80% of them live in developing countries. Collectively, they use more than 300 different sign languages. Sign languages are fully fledged natural languages, structurally distinct from spoken languages.In this project, we have implemented a solution for INDIAN SIGN LANGUAGE.


### Problem Solution
- Our solution to this problem is an AI assistance for sign language tool that works based on computer vision and machine learning using technologies like OpenCV,Mediapipe,BERT.etc
- The tool gets the sign language gesture performed by the person as input from the camera and converts that into speech.SImilarly , it converts text to Indian sign language gestures.
- We’ve trained the ML model using the SVM algorithm.
- We have also added features like word autocomplete,Next word prediction and Backspacing

### Demo
![](https://github.com/harikrish-s/Sign-Language-Recognition/blob/main/demo/demo-pic.png)

### Installation

Open your Terminal

a) Create a Virtual Environment
```
virtualenv venv
```
b) Move to venv directory and activate environment
```
cd venv
Scripts\activate
```
c) Clone this Repo
```
git clone https://github.com/harikrish-s/Sign-Language-Recognition.git
```
d) Move into the cloned directory
```
cd Sign-Language-Recognition
```
e) Now install all requirements
```
pip install -r requirements.txt
```
### Run

After Installing the Requirements , Open your terminal and run the command
```
streamlit run Home.py
```
Follow the link that appears !

### Technologies Used


<img src="https://github.com/harikrish-s/Sign-Language-Recognition/blob/main/demo/py-logo.png" width=25% height=25%> <img src="https://github.com/harikrish-s/Sign-Language-Recognition/blob/main/demo/openCV-logo.png" width=10% height=10%> <img src="https://github.com/harikrish-s/Sign-Language-Recognition/blob/main/demo/st-logo.png" width=25% height=25%> <img src="https://github.com/harikrish-s/Sign-Language-Recognition/blob/main/demo/tf-logo.png" width=10% height=10%>



### Got a Question ?

If you have any questions that are bothering you, Please feel free to contact us on LinkedIn - [Harikrishnan S](https://www.linkedin.com/in/harikrishnan-s-580461214/) , [Rohit Arrunachalam](https://www.linkedin.com/in/rohitarrunachalam/). Or if you think a line is redundant or can be removed to make the program better then you can obviously ask us or make a pull request !

