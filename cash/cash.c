#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    float change;
    int coins = 0;

    do
    {
        change = get_float("change owed: ");
    }

    while (change < 0);

    while (change >= 25)
    {
        coins++;
        change = change - 25;
    }

    while (change >= 10)
    {
        coins++;
        change = change - 10;
    }

    while (change >= 5)
    {
        coins++;
        change = change - 5;
    }

    while (change >= 1)
    {
        coins++;
        change = change - 1;
    }

    printf("%d\n", coins);
}
