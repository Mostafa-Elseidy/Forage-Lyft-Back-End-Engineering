# Rental Fleet’s New Logistics System

Building a component that is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned.
       
![Design](https://github.com/Mostafa-Elseidy/Forage-Lyft-Back-End-Engineering/assets/67195496/5c746454-ded0-4f5b-a4a3-f6e1b1259dfd)

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
