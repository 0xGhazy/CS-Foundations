package com.pk;
import java.util.Scanner;

public class Main{
    
    public static void main(String[] args) {

        /*
        ** Vairables area 
        **
        */
        Board board = new Board();
        Scanner reader = new Scanner(System.in);
        int gameCounter = 9;    // max moves in game.
        int playerRound = 0;    // change the player sign each round.
        char playerX = 'X';
        char playerO = 'O';
        char playerSign = ' ';
        int position;
        
        /*
        ** Our program starts here >>
        **
        */

        while(gameCounter >= 0){

            board.drawBoard(); // draw the board
            if (playerRound % 2 == 0){
                playerSign = playerX;
            }else{
                playerSign = playerO;
            }

            // reading position from the user.
            System.out.println("[+] Player (" + playerSign + ") round: ");
            position = reader.nextInt();

            // set the new position on screen
            board.setPosition(playerSign, position);
            // draw the new board.
            board.drawBoard();

            // check if we have a winner :)
            if(board.isWinner(playerSign)){
                System.out.println("\nCongrats! Player " + playerSign + " <3");
                System.out.println("You are the winner !\n");
                break;// end our program
            }else{
                playerRound += 1;
                gameCounter -= 1;
            }
        } // end of loop
    } // end of method
} // end of class