#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string names[4];

    names[0] = "EMMA";
    names[1] = "RODRIGO";
    names[2] = "BRIAN"; 
    names[3] = "JAMIE";

    printf("%s\n", names[0]);
    printf("%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3]);
}

