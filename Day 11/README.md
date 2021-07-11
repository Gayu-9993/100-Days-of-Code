# Day 11 of coding : Game of BlackJack

Open the executable file to play the game ~ !

## Rules : 

    1. Both user and dealer get 2 cards each. Ace is worth 11 points, Joker/Jack, Queen, King are all worth 10 points

    2. If either player gets a 21 on their first go, its a Blackjack and they win. In the offchance that both get it, then it will be a draw. 

    3. If there is no blackjack, one card from the dealer's hand is revealed. Then user gets to choose whether they want another card. If they draw another card and their total crosses 21, the user looses. If the total is still under 21, they can draw another card and this goes on until either the total crosses 21 or the user chooses to not draw another card. 

    4. Once the user has had their chance, it is the turn of the dealer. If the total of the dealer's cards is less than 17, then the the user will draw more cards until either the total crosses 21, in which case the dealer is out, or the total crosses 17. 

    5. Should any player's total cross 21, if they have an Ace in their hand, then it will be counted as 1 instead of 11. They will however not be able to draw another card, even if their total is less than 21. 

    6. If there's no blackjack, and the total of individual players is less than 21, then the one with the higher total wins. Or it can be a draw if both the players have the same total and are not out.