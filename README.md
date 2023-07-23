# tic-tac-toe-AI
An AI bot that analyzes all game states in order to make the best move. I haven't beat it yet. 


<h1>Tic Tac Toe</h1>
    <h2>Usage: </h2>
    <p> Run 'python3 game.py' in the directory with the files. </p>
    <p> To place your move, follow these rules: </p>
    <ul>
        <li>Use 't', 'm', or 'b' as your first character to indicate top, middle or bottom</li>
        <li>Use 'l' 'm' or 'r' as your second character to indicate left, middle, or right</li>
        <li>For example, to place your move in the top left corner, type 'tl'</li>
        <li>If you don't enter a valid move, the game will halt.</li>
    </ul>
    <h2>File Structure: </h2>
    <p>game.py contains a while loop for the game.</p>
    <p>game_library.py shockingly is a library for my functions.</p>
    <h2>How it works:</h2>
    <h3>The game: </h3>
    <p>game.py contains a loop for the game, getting the human's move, then the computer decides a move, and repeats till an end state is reached.</p>
    <h3>The AI: </h3>
    <p>There are 2 parts to the computers move, <b>blocking</b> and <b>deciding</b>.</p>
    <h4><b>Blocking</b></h4>
    <p>The first thing the AI does is consider if it needs to block a move. If, for instance, the top row is is : "XXb",
        then the computer needs to go in the top right. If a block needs to be made, the computer makes that move and
        doesn't use the second part of the algorithim since blocking means the computer is at risk of a moving state.</p>
    <h4><b>Deciding</b></h4>
    <p>If a block does not need to be made, the algorithim needs to make a guess at <b>which move maximizes the probability of a win state.</b><br> 
    This is calculated by taking a game state, and looking at all possible outcomes from there. The number of
    possible outcomes where the computer wins divided by all the possible outcomes is the probability of a win.<br> When its the computers turn, it looks at every blank square and calculates the probability of a win if it moves there. It moves on the square with the highest probability.
</p>
    