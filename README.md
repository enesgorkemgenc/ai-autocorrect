# ai-autocorrect
> AI Autocorrect app that utilizes the collected data from user inputs.
## Demo GIF
![ezgif com-gif-maker](https://user-images.githubusercontent.com/93938698/190847569-ee6a7023-4001-4b81-8f7d-3b4bb702e50c.gif)

## How Does It Work ?

When you make a typo and fix it, It will detect the difference, then a relation between misspelled word and the correction is going to be received or created

If the relation already exists, the count variable in the relation will increase.
That count variable counts how many times someone changed the misspelled word to the accurate word.

It is for showing the best matches to the user.

After every letter you write, you are going to receive top 3 suggestions for the last word in the input area.

![aiautocorrectss1_600x338](https://user-images.githubusercontent.com/93938698/190851332-ecda972f-2708-449b-98fb-4bd7d7e01ee0.png)

For Example;

When someone types "hellp" they would probably fix that to "hello", and assume that this typo has been changed to "hello" 10 times.
But there will also be someone that meant "help", and change the "hellp" to "help", and let's assume that this has been done 5 times

Then the suggestion "hello" is going to be in the first place.

The suggestions are the top 3 words that have the highest value of count variable in their relations with the misspelled word.

### Use Arrow-up ↑ and Arrow-down ↓ to switch between the suggestions.
![switch](https://user-images.githubusercontent.com/93938698/190851029-df084c24-fe3c-4804-8044-f01d1ab2d015.gif)

### Use Enter ↵ to apply the selected suggestion.
![apply](https://user-images.githubusercontent.com/93938698/190851191-1e8c7bc1-c84e-4056-84a2-0adbb0ff18d4.gif)

