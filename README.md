# Exploration of Trends In Terrorist Attacks

## Table of Contents
- [Introduction](#introduction)
- [Visualization Design](#visualization-design)
    - [Domain Characterization](#domain-characterization)
    - [Data Abstraction](#data-abstraction)
    - [Visual Encoding and Interaction Design](#visual-encoding-and-interaction-design)
    - [Algorithm Design](#algorithm-design)
- [Running the Application](#running-the-application)
- [Screencast](#screencast)
- [Authors](#authors)
- [References](#references)


## Introduction <a name="introduction"></a>

Terrorist attacks have massive economic and psycological effect on wide range of population. In the sense that the dynamics such as trends over years in target groups, weapon types, dangerous groups, numbers of terrorist attacks are analysed, that could enable policy makers, gorvernments, analysts to prevent them in future. [The Global Terrorism Database (GTD)](https://www.start.umd.edu/gtd/access/) is the source for our data defines a terrorist attack as the threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic, religious, or social goal through fear, coercion, or intimidation. 


The GTD is an event-level database containing more than 200,000 records of terrorist attacks that took place around the world beteween years 1970 and 2019. For each event, a wide range of information is available, including the date and location of the incident, the weapons used, nature of the target, the number of casualties, and – when identifiable – the group or individual responsible. It is maintained by the National Consortium for the Study of Terrorism and Responses to Terrorism (START) at the University of Maryland. 


In this study

## Visualization Design <a name="visualization-design"></a>

### Domain Characterization <a name="domain-characterization"></a>

In our study, we consider the attacks that were attempted either they are succesful or not and classified as not doubted. This approach allow us to evaluate data from broader perspective comprehensively. 
We have used this dataset to visualise the development of terrorist attacks on global over years.

Our target users are the analytic experts who works on international relations especially politics related researchers in think tanks.

The purpose of our visualisation is therefore to give useful information about terrorist attacks to the users in order to help them to conduct their research and prepare analytics to support their article writing processes.

The dashboard includes both Global and Country level statistics, some of them gives them opportunity to compare the data over years. Hence they can easily detect the trends especially in the areas of target type, affiliated attacks and most dangerous groups.

### Data Abstraction <a name="data-abstraction"></a>

### Visual Encoding and Interaction Design <a name="visual-encoding-and-interaction-design"></a>

Example for tables:

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

### Algorithm Design <a name="algorithm-design"></a>

## Running the Application <a name="running-the-application"></a>

In order to run this application on your computer and make changes in it, you should run these steps which are stated below sequentially.

```
git clone https://github.com/Zombobot1/gtd-vis.git
cd path/to/file
npm i
npm start
```

The deployed version of project is accesible over [Github Pages](https://zombobot1.github.io/gtd-vis/)

## Screencast <a name="screencast"></a>

The screencast of the project is accessible over the link given below.

<a href="https://youtu.be/VyhLRJVoIrI" target="_blank">
    <img src="https://img.youtube.com/vi/VyhLRJVoIrI/hqdefault.jpg" alt="Screencast - GTD Data Visualization" width="240" height="180" border="10" />
</a>

## Authors <a name="authors"></a>

- Ali OMAROV
- Esra GÜCÜKBEL
- Evgenia SLIVKO

