<div align="center">
    <img src="https://github.com/albarji/ballmatro/blob/master/docs/ballmatroLogo.png?raw=true" width="800"><br>
</div>

[![Unit Tests](https://github.com/albarji/ballmatro/actions/workflows/python-tests.yml/badge.svg)](https://github.com/albarji/ballmatro/actions/workflows/python-tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/albarji/ballmatro/badge.svg?branch=master)](https://coveralls.io/github/albarji/ballmatro?branch=master)
![Ruff](https://img.shields.io/badge/Ruff-passing-success?logo=ruff&logoColor=white)

A challenging task for LLMs in which they need to create high-scoring Ballatro-like hands.

## What is BaLLMatro?

BaLLMatro is a portmanteu of "LLM" (Large Language Model) and "Ballatro", the critically acclaimed [videogame](https://www.playbalatro.com/). Inspired by the layers of complexity of such game, this project provides datasets and tools to test the ability of LLMs in finding high-scoring "augmented" poker hands, under increasingly complex scoring rules. Thus, the objective of the project is to find the generalization abilities of LLMs, in a task where both humans and AI models can measure their performance.

## The rules of BaLLMatro

In each game of BaLLMatro you will get a list of cards, and you will have to decide which cards from these list to play. The objective of the game is to play the subset cards that maximizes the score.

### Cards

Similar to standard poker hands, each card is represented as a rank and a suit:
- Ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.
- Suits: ♣, ♦, ♠, ♥. (club, diamond, spade, heart).

Optionally, each card might include a modifier that changes its scoring rules, as we will see later on.

### Poker hands

The way to score points in a BaLLMatro game is to select a subset of cards that make up a **poker hand**. Each poker hand has a specific value in **chips** and a **multiplier** that will count towards the final score.

- **Straight Flush**: 5 cards from the same suit, in consecutive order. 100 chips, 8 multiplier.
> Example: [2♣, 3♣, 4♣, 5♣, 6♣]
- **Four of a Kind**: 4 cards of the same number. 60 chips, 7 multiplier.
> Example: [2♣, 2♦, 2♥, 2♠]
- **Full House**: 3 cards of the same number, and 2 cards of another. 40 chips, 4 multiplier.
> Example: [2♣, 2♦, 2♥, 3♠, 3♥]
- **Flush**: 5 cards from the same suit. 35 chips, 4 multiplier.
> Example: [2♣, 3♣, 5♣, 7♣, J♣]
- **Straight**: 5 cards in consecutive order, regardless of suit. 30 chips, 4 multiplier.
> Example: [2♣, 3♥, 4♣, 5♦, 6♠]
- **Three of a Kind**: 3 cards of the same number. 30 chips, 3 multiplier.
> Example: [2♣, 2♦, 2♥]
- **Two Pair**: 2 pairs of cards of the same number. 20 chips, 2 multiplier.
> Example: [2♣, 2♦, 3♥, 3♠]
- **Pair**: 2 cards of the same number. 10 chips, 2 multiplier.
> Example: [2♣, 2♦]
- **High Card**: a single card. 5 chips, 1 multiplier.
> Example: [A♠]

These poker hands are sorted from highest priority to lowest. When a set of cards is played, the highest priority poker hand will be used for computing the score.

> Example: when playing [2♣, 2♦, 2♥, 3♠, 3♥] it will be considered a Full House, even though the played cards also contain a Three of a Kind and a Pair.

If the played cards do not form any poker hand, the play will be regarded as a **No Poker Hand**, with 0 chips and 0 multiplier. Similarly, if the played cards were not contained in the input cards, the play will be regarded as an **Invalid Hand**, with 0 chips and 0 multiplier.

> Example: [2♦, A♠] -> 0 chips x 0 multiplier.

All the played cards must form part of a poker hand, or equivalently, the set of played cards must not contain cards that will not form part of the poker hand. If this is not met, the play will also be considered a **No Poker Hand**.

> Example: [2♣, 2♦, 2♥, 6♠] ->  0 chips x 0 multiplier, as even though the first three cards form a Three of a Kind, an extra 6♠ card has been played that does not form part of the poker hand.

### Scoring hands

After determining the poker hand that has been played, the total score is computed in three steps.

**Step one**: the number of chips and value of the multiplier are initialized with the corresponding values of the played hand. If an Invalid Hand or No Poker Hand was obtained, the process stops and a final score of 0 is returned.

**Step two**: the specific cards used to build the poker hand are checked in order (from left to right), as they can increase the chips of the played hand:
* Cards with ranks from 2 to 10 add a value chips equal as their rank value.
* Face cards (J, Q, K) are valued 10 chips.
* An ace (A) is valued 11 chips.

If any played card has a modifier, it will also affect the number of chips or the multiplier:
* `+` Bonus cards: +30 chips (on top of those awarded normally by the card rank).
* `x` Mult card: +4 multiplier.

**Step three**: the total number of chips is multiplied by the value of the multiplier, producing the final score.

> Example: the hand [8♣, 9♥, 10♣, J♦, Q♠] is a Straight that has a base value of as 30 chips x 4, and the value of the cards add 8+9+10+10+10 chips, resulting in a total of 47 addicional chips. Thus, the hand score would be (30 + 47) x 4 = 308 points.

> Example: the hand [2♣+, 3♣, 5♣, 7♣, J♣x] is a Flush. A Flush is valued 35 chips x 4, the value of the cards add 2+3+5+7+10, the bonus modifier (+) in 2♣+ adds 30 more chips, and the mult modifier (x) in J♣x adds 4 to the multiplier. This results in (35+2+3+5+7+10+30) x (4+4) = 736 points.

### Jokers

The input list of cards may also contain special joker cards, which are noted by the 🂿 symbol. These cards have neither rank nor suit, instead they feature a name and a description of the joker effect as text.

> Example: a possible input list of cards might be [2♥,3♦,A♠,🂿 Pluto: multiplies by 2 the chips and multiplier of the High Card hand]

Joker cards must not be used as part of the selected cards to be played. Playing a joker card will always result in an Invalid Hand.

Even if not played, joker cards modify the scoring rules following the description of the joker card. Therefore, the presence of a joker might have an impact on which is the best subset of cards that can be played.

> Example: the hand [2♥,2♦,A♠] attains the highest score when playing [2♥,2♦], which results in a Pair scoring 14 chips x 2 = 28. However, when receiving a joker in the list as [2♥,2♦,A♠,🂿 Pluto: multiplies by 2 the chips and multiplier of the High Card hand] the best play now is [A♠], which results in a High Card scoring 21 chips x 2 = 42.

Multiple joker cards may appear in the input list of cards. If two jokers modify the same scoring rule or step of the scoring process, their modifications are applied in the same order as they were presented in the input list of cards.

> Example: the input list of cards [🂿 Mars: multiplies by 2 the chips and multiplier of the Four of a Kind hand,🂿 Mars Shard: adds 1 to the chips and multiplier of the Four of a Kind hand,2♥,2♦,2♠,2♣], when played as [2♥,2♦,2♠,2♣], results in a score of 1935. However, the input list of cards [🂿 Mars Shard: adds 1 to the chips and multiplier of the Four of a Kind hand,🂿 Mars: multiplies by 2 the chips and multiplier of the Four of a Kind hand,2♥,2♦,2♠,2♣], when played as [2♥,2♦,2♠,2♣], results in a score of 2080.

### Input/output format

**Inputs**: you will receive a list of the available cards, each card represented by a rank, a suit, and optionally a modifier. The list will be encloded in square brackets, each card separated by a comma and optional spaces.

**Outputs**: you will need to output a list of the cards to be played, in the same format as the input list. Only cards received in the input can be included in this list. Any list that contains other cards will be scored 0.

Some examples of inputs and outputs are:

<pre>
[2♣, 5♥, 5♥, J♣+, J♣]
[5♥, 5♥, J♣+, J♣]
</pre>

<pre>
[2♣, 3♣, 4♣, 5♣, 6♣]
[2♣, 3♣, 4♣, 5♣, 6♣]
</pre>

<pre>
[2♦, 3♥, 7♠, 10♥, A♠]
[A♠]
</pre>

<pre>
[2♥,2♦,A♠,🂿 Pluto: multiplies by 2 the chips and multiplier of the High Card hand]
[A♠]
</pre>

Your objective is to output the highest scoring hand possible.
Do not generate any other output apart from the list of cards played.

## Datasets and difficulty levels

BaLLMatro datasets are available through [Hugging Face datasets](https://huggingface.co/datasets/albarji/ballmatro), and arranged in difficulty levels that vary the number of available cards and the computational resources required for finding the optimal play:

|Level|Arrangement|Simplest possible solution|
|-----|-----------|--------------------------|
|Level 1|All inputs contain a single card. The task can be reduced to outputting the card present at the input (play as High Card)|Regular expression / Finite automata (`O(1)`)|
|Level 2|All inputs contain a two cards. The agent must identify whether to play both cards (Pair) if possible, or play the best single card (High Card)|Simple heuristics (`O(1)`)|
|Level 3|All inputs contain 1-4 cards. All poker hands are possible|Brute-force search (`O(4!)`)|
|Level 4|All inputs contain 1-8 cards. All poker hands are possible|Brute-force search (`O(8!)`)|

All levels are provided as two folds, a train and a test fold. A fair use of this dataset involves using the test folds only for testing the LLM peformance, which means:
* Not using test data to fine-tune the model in any way.
* Not using test data as few-shot examples, or any other kind of in-context learning or prompting approach that makes use of test examples or informacion about the distribution or nature of test examples.
