package com.pk;

public class Board{

    private char board[] = {' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};

    // display board on screen
    public void drawBoard(){
        System.out.println(" " + board[6] + " | " + board[7] + " | " + board[8]);
        System.out.println("---+---+---");
        System.out.println(" " + board[3] + " | " + board[4] + " | " + board[5]);
        System.out.println("---+---+---");
        System.out.println(" " + board[0] + " | " + board[1] + " | " + board[2]);
    }


    // append the entred player sign into a next printed board
    public void setPosition(char PlayerSign, int position){
        if(board[position - 1] == ' '){
            board[position - 1] = PlayerSign;
        }else{
            System.out.println("[-] Don't cheating bro :)");
        }
    }

    
    // check if we have a winner line on game board.
    public boolean isWinner(char playerSign){
        if(
            board[0] == playerSign && board[1] == playerSign && board[2] == playerSign || // 123
            board[3] == playerSign && board[4] == playerSign && board[5] == playerSign || // 456
            board[6] == playerSign && board[7] == playerSign && board[8] == playerSign || // 789
            board[0] == playerSign && board[3] == playerSign && board[6] == playerSign || // 147
            board[1] == playerSign && board[4] == playerSign && board[7] == playerSign || // 258
            board[2] == playerSign && board[5] == playerSign && board[8] == playerSign || // 369
            board[0] == playerSign && board[4] == playerSign && board[8] == playerSign || // 159
            board[2] == playerSign && board[5] == playerSign && board[6] == playerSign    // 357
        ){return true;}
        else{return false;}
    } // end of function
} // end of board class
