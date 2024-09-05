#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string input = get_string("input: ");
    for (int i=0; i < strlen(input); i++)
    {
        printf("%c\n", input[i]);
        printf("%i\n", input[i]);
        printf("%c\n", toupper(input[i]));
        printf("%i\n", toupper(input[i]));
    }
}
