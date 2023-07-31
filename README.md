# Rental Fleet’s New Logistics System

Building a component that is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned.

## Tasks

1. Software Architecture
2. Refactoring
3. Unit Testing
4. Add some new functionality to the system
    - Upgrade Spindler batteries
    - Add tire servicing

## Criteria for car servicing

Whether or not a car should be serviced depends on two factors at the moment:

- The engine
- The battery

| Part |Service criteria|
|---|---|
|Capulet Engine| Once every 30,000 miles|
|Willoughby Engine| Once every 60,000 miles|
|Sternman Engine| Only when the warning indicator is on|
|Spindler Battery| Once every 2 years|
|Nubbin Battery| Once every 4 years|

There are five car models in Lyft’s fleet, each with a different engine-battery combination.

|Car| Engine| Battery|
|---|---|---|
|Calliope| Capulet | Spindler |
|Glissade| Willoughby | Spindler ||
|Palindrome| Sternman | Spindler |
|Rorschach| Willoughby | Nubbin |
|Thovex| Capulet | Nubbin |

-----

## Draft a new architecture

![Design](https://github.com/Mostafa-Elseidy/Forage-Lyft-Back-End-Engineering/assets/67195496/5c746454-ded0-4f5b-a4a3-f6e1b1259dfd)

## Add Tire servicing

| Part |Service criteria|
|---|---|
|Carrigan tires | one or more of the values in the tire wear array is greater than or equal to 0.9 |
|Octoprime tires | the sum of all values in the tire wear array is greater than or equal to 3 |

|Car| Tires|
|---|---|
|Calliope| Octoprime |
|Glissade| Carrigan |
|Palindrome| Octoprime |
|Rorschach| Octoprime |
|Thovex| Carrigan |
