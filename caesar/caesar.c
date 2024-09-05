#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2 && isdigit(*argv[1]))
    {
        int k = atoi(argv[1]);
        string plaintext = get_string("plaintext : ");
        printf("ciphertext: ");

        for (int letter = 0; letter < strlen(plaintext); letter++)
        {
            if (plaintext[letter] >= 'a' && plaintext[letter] <= 'z')
            {
                printf("%c", (((plaintext[letter] - 'a') + k) % 26) + 'a');
            }
            else if (plaintext[letter] >= 'A' && plaintext[letter] <= 'Z')
            {
                printf("%c", (((plaintext[letter] - 'A') + k) % 26) + 'A');
            }
            else
            {
                printf("%c", plaintext[letter]);
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
}
