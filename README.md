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

Terrorist attacks have massive economic and psycological effect on wide range of population. In the sense that the dynamics such as change over years in target groups, weapon types, terrorist groups, numbers of terrorist attacks are analysed, that could enable governments,  policy makers, researchers, analysts extrapolating the useful information from the attacks where they happened in past.

[The Global Terrorism Database (GTD)](https://www.start.umd.edu/gtd/access/) is the source for our data defines a terrorist attack as the threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic, religious, or social goal through fear, coercion, or intimidation. The GTD is an event-level database containing more than 200,000 records of terrorist attacks that took place around the world beteween years 1970 and 2019. For each event, a wide range of information is available, including the date and location of the incident, the weapons used, nature of the target, the number of casualties, and – when identifiable – the group or individual responsible. It is maintained by the National Consortium for the Study of Terrorism and Responses to Terrorism (START) at the University of Maryland. 

## Visualization Design <a name="visualization-design"></a>

### Domain Characterization <a name="domain-characterization"></a>

In our study, we contacted with a researher who working in thinktank which conducts the projects in areas of foreign and security policy or international and European politics. With regarding the needs of our target user(user group) various cases are determined. 

1. The change in number of attacks over years both for global and country based, that would help them to take an overview about the state of last 10 years.
2. Compare and finding correlation between the fatalities and injuries with number of attacks in order to understand whether a country has improvement in their intelligence service. Mostly attacks have a design to target crowds such as after exploding the bombs in first stage, to the points where people escape, another set of bombs are placed, even some of attacks had third stage with weapons.
3. The change in target type, that give insights for future attacks and which type of user groups are vulnerable.
4. Comparing the affiliated and unknown attacks of most attacked countries over years in an effort to have an idea about intelligence service of countries. Affiliated attacks which were carried out by groups were identified by government, however unknown attacks were not.
5. Inspecting the activities of most influential terrorist groups over years. Influential can be described as having much more attacks that were carried out.


In this context, only the attacks that were attempted either they are succesful or not, classified as not doubted and only last 10 years, are taken into account. This approach allow us to evaluate data from broader perspective and obtaining more up-to-date view. The dashboard includes both Global and Country level statistics, some of them gives them opportunity to compare the data over years. Hence they can easily detect the trends especially in the areas of target type, affiliated attacks and most dangerous groups.

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

In order to run this application on your computer and make changes on the project, you should run these steps which are stated below sequentially.

```
git clone https://github.com/Zombobot1/gtd-vis.git
cd path/to/file
npm i
npm start
```

The project is currently deployed to [Github Pages](https://zombobot1.github.io/gtd-vis/).

## Screencast <a name="screencast"></a>

The screencast of the project is accessible over the link given below.

<a href="https://youtu.be/VyhLRJVoIrI" target="_blank">
    <img src="https://img.youtube.com/vi/VyhLRJVoIrI/hqdefault.jpg" alt="Screencast - GTD Data Visualization" width="240" height="180" border="10" />
</a>

## Authors <a name="authors"></a>

- Ali OMAROV
- Esra GÜCÜKBEL
- Evgenia SLIVKO

