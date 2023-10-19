#include <stdio.h>
#include <string.h>
#define MAX 1500
#include <ctype.h>

int main()
{
  while (1)
  {
    char input = fgetc(stdin);
    if (feof(stdin))
    {
      break;
    }

    if (!ispunct(input))
    {
      fputc(tolower(input), stdout);
    }
  }

  return 0;
}