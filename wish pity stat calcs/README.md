# 90 Pity Rates
## The Problem
While engaging in conversation with another member of a community I'm in, I made a claim about the rates at which a specific rare occurance happens and they disagreed. All the numbers involved are concretely defined and finite, but due to the low odds involved and the extremely high number of steps required to find the result, doing a theoretical statistical analysis would be exhausting, and not worth the time of anyone involved.

In 90_pity_rates.py on line 5, an array is defined which contains the probability of success on sucessive steps on all possible steps. It is 0.6% for steps 1-73, and starting on 74, the probability of every new step is 6% higher than the previous. When success is achieved, you are returned to step 1.

The problem was as follows: "How many steps (called wishes) does someone have to take on average to reach 90 pity?"</br>
Additionally there were related problems like "How many successes would someone have on average before reaching 90 pity?"

So the problem is simple: Create a simulation using these odds to calculate concrete stats which settle the disagreement.

## The Solution
Before anything, I needed arrays of the rates that I could use to determine if a random number qualified as a success or not. I made an intermediary script that just printed out what the rates would be at each step and used multi cursor tools to quickly turn it into a single array.

After that it's as simple as looping over some very large number, generating a random number, incrementing the step, and resetting to 0 if a success was generated.

## The Process
After creating the solution it became very apparent that speed and scale was an issue here. To get any kind of consistent or meaningful results, I had to loop over a number in the scale of tens or hundreds of billions.

Given my experience using Python compilation tools like Numba, that's where I turned to first. Compiling a hot loop is probably the single greatest way to gain runtime.</br>
But now I'm running into a different problem. Each run at scale to test the function and visualizations I was developing would take multiple minutes to perform, and during that time I had no feedback on if things were progressing at all, or correctly. Running in the debugger introduces massive overhead that would cost far more time than its worth, so I spent some time creating a psuedo progress bar that would just print out every 10%. For the scope of this script and the scale of these numbers, that is quite sufficient feedback.

Everything after this was simply about organizing data. Record how many times each step (pity) was reached. Record how many times a success occured at each step. Find the rate between them. Time the whole thing. Using various methods I got it to a place where it was far more than enough for the conversation, and the dispute had been resolved with "real" data.

# Theoretical Flat Rates
## The Problem
In a similar conversation that took place around the same time, I mentioned how unfortunate it is that the true rates-per-pity (the previously mentioned array) were so hard for the community to figure out, as the only official data provided was a consolidated rate of 1.6% on all steps.</br>
Someone else said something to the tune of "Well given what they told us about the first step and the consolidated rate, this was basically the only solution"

I took issue with this response, because one of the first things that is taught in statistics is how there are many types of averages that all represent the data in different ways. A mean can only represent so much information in a single number, and it absolutely is ambiguous. I proposed that there could have been much simpler solutions which result in the exact same initial rate and consolidated rate, but did not involve any slow ramping whatsoever.

I was inspired to put this claim to the test, so I started developing this script soon afterwards. The idea for it was always clear: "Find a flat rate and pity where the flat rate could kick in such that the consolidated rate is maintained."

So to contrast the previous problem, instead of being 0.6% for 1-73 then increasing by 6% per step, it could be 0.6% for 0-60, then increase to 10% for every other pull 61-89 then guaranteed at 90 (example numbers, not correct).

## The Solution & Process
This script generates a table with columns for which step the flat increase happens on, and rows for what the rates increase to. Every cell of the table is the consolidated rate found after simulating 200,000 successes, not to dissimilar from the previous script. Using some math to calculate a consolidated rate without doing tracking on the same level as 90_pity_rates. Most of the work was actually on the visualization compared to the calculation.

Making the visualization gave me a chance to use things I've learned from classes and previous projects, such as the advanced format string representations and adding colors/highlights to a terminal output.

Since I wanted to try out many different thresholds and flat rates, I also extracted most of the variables so they would be easy to change and get new results with.

